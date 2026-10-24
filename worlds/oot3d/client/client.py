from enum import Enum
from typing import Dict, List, Optional, Set
import asyncio
import traceback
import json
from BaseClasses import ItemClassification
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
from NetUtils import ClientStatus
from .utils import options_to_xml
from .interface import N3DSInterface, ConnectionError
from ..world import OoT3DWorld

"""
Original client code comes from the ALBW AP (https://github.com/randomsalience/albw-archipelago)
"""

# going to focus on US for now but EU support should be trivial to implement
US_TITLE_ID = 0x0004000000033500
EU_TITLE_ID = 0x0004000000033600
RANDOMIZER_APP_TITLE_ID = 0x0000000000000000

triple_addr = ""
is_3ds = False

class AppType(Enum):
    NONE = 0
    GAME = 1
    RANDOMIZER = 2

class AppConnectionStatus(Enum):
    NOT_CONNECTED = 0
    INCOMPATIBLE_VERSION = 1
    WAITING_ON_RANDOMIZER_APP = 2
    AUTHENTICATING = 3
    INVALID_SLOT = 4
    WAITING_TO_CONNECT_TO_MULTIWORLD = 5
    WAITING_ON_MULTIWORLD_DATA = 6
    CONNECTED = 7

def bytes_or(a: bytes, b: bytes) -> bytes:
    return bytes([x | y for x,y in zip(a,b)])

class OoT3DCommandProcessor(ClientCommandProcessor):
    pass

    ## Retail 3DS support not implemented
    # 
    # def _cmd_3ds(self, address):
    #     """Connect to a real 3ds"""
    #     global triple_addr
    #     if triple_addr == "":
    #        triple_addr = address
    #     else:
    #         self.output("Already connected to a 3ds")
    # 
    # def _cmd_3dsdisconnect(self):
    #     """Disconnect from a 3ds"""
    #     global triple_addr
    #     if triple_addr == "":
    #         self.output("Not currently connected to a 3ds")
    #     else:
    #         self.output(f"Disconnected from {triple_addr}.")
    #         triple_addr = ""
    # 
    # def _cmd_3dstimeout(self, timeout):
    #     """Set timeout (in connection attempts) until giving up connection to 3ds (default 200000)"""
    #     global triple
    #     if triple.set_timeout(timeout):
    #         self.output(f"Successfully set timeout to {timeout} attempts")
    #     else:
    #         self.error(f"Invalid timeout: {timeout}")

class OoT3DClientContext(CommonContext):
    command_processor = OoT3DCommandProcessor
    game: Optional[str] = "Ocarina of Time 3D"
    items_handling: Optional[int] = 0b101 # receive remote items and starting inventory
    want_slot_data: bool = True

    interface = N3DSInterface()
    interface_connected: bool
    app_type = AppType.NONE
    app_connection_status: AppConnectionStatus
    initial_connect = False
    authenticating: bool
    server_connected: bool
    initial_delay: bool
    slot_data: Optional[Dict[str, any]]
    invalid: bool
    last_error: str
    show_citra_connect_message: bool
    show_triple_connected_message: bool

    DATA_VERSION: int = 4
    RANDOMIZER_APP_HEADER_LOCATION: int = 0x510000 # may change in the future idk

    # Randomizer App Memory Layout
    AP_PAYLOAD_SIZE: int  = 64 * 1024
    # 0-7 (0x00 - 0x07) identifer
    # 8 (0x08) data version
    # 9 (0x09) listening flag (0 = app not listening, 1 = app listening)
    # 10 (0x0A) lock (0 = safe for proxy to write, 1 = safe for app to read)
    # 11 (0x0B) stage (0 = slot data, 1 = item->location mapping)
    # 12-15 (0x0C - 0x0F) payload size
    # 16 (0x10) payload start
    AP_LOCK_OFFSET: int  = 0x0A
    AP_STAGE_OFFSET: int  = 0x0B
    AP_PAYLOAD_SIZE_OFFSET: int  = 0x0C
    AP_PAYLOAD_OFFSET: int  = 0x10

    # Randomizer App Protocol Stages
    STAGE_SLOT_DATA: int = 0
    STAGE_ITEM_LOCATION_MAPPING: int = 1

    # from ALBW, update with new address when we get there
    AP_HEADER_LOCATION: int = 0x6fe5f8

    def __init__(self, server_address: Optional[str], password: Optional[str]):
        super().__init__(server_address, password)
        self.interface_connected = False
        self.app_connection_status = AppConnectionStatus.NOT_CONNECTED
        self.server_connected = False
        self.authenticating = False
        self.initial_delay = True
        self.slot_data = None
        self.course_flags = []
        self.ravio_scouted = False
        self.to_hint = []
        self.invalid = False
        self.last_error = ""
        self.show_citra_connect_message = True
        self.show_triple_connected_message = True

    def run_gui(self) -> None:
        from kvui import GameManager

        class OoT3DManager(GameManager):
            base_title: str = "Archipelago Ocarina of Time 3D Client"

        self.ui = OoT3DManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")
    
    def error(self, error: str) -> None:
        if error != self.last_error:
            logger.error(error)
            self.last_error = error
        self.invalid = True
    
    async def read_header(self) -> None:
        # logger.info("read memory %s" % ((await self.interface.read(self.RANDOMIZER_APP_HEADER_LOCATION, 27))))
        # logger.info("app_connection_status %s" % (self.app_connection_status.name))
        if (await self.interface.read(self.RANDOMIZER_APP_HEADER_LOCATION, 8)) == b"OOT3RAND":
            await self.connect_app()   
            return
        self.app_connection_status = AppConnectionStatus.NOT_CONNECTED
            
        if (await self.interface.read(self.AP_HEADER_LOCATION, 4)) != b"ARCH":
            self.error("Running incompatible or incorrectly patched game.")
        elif (await self.interface.read_u32(self.AP_HEADER_LOCATION + 0x8)) < self.DATA_VERSION:
            self.error("Version mismatch: update your oot3drandomizer library and re-patch.")
        elif (await self.interface.read_u32(self.AP_HEADER_LOCATION + 0x8)) > self.DATA_VERSION:
            self.error("Version mismatch: update your apworld and restart the client.")
    
    async def connect_app(self) -> None:
        if self.app_connection_status == AppConnectionStatus.NOT_CONNECTED:
            logger.info("Connected to the OoT3D Randomizer app")
            
        if (await self.interface.read(self.RANDOMIZER_APP_HEADER_LOCATION + 0x8, 1)) != self.DATA_VERSION.to_bytes(1, "little"):
            if self.app_connection_status != AppConnectionStatus.INCOMPATIBLE_VERSION:
                self.error("Version mismatch: update and restart your randomzier app and/or client.")
                self.app_connection_status = AppConnectionStatus.INCOMPATIBLE_VERSION
        
        elif (await self.interface.read(self.RANDOMIZER_APP_HEADER_LOCATION + 0x9, 1)) == b'\x00': # randomizer app is not listening
            if self.app_connection_status != AppConnectionStatus.WAITING_ON_RANDOMIZER_APP:
                logger.info("Select \"Archipelago Multiworld\" in the Randomizer App to send randomizer data")
                self.app_connection_status = AppConnectionStatus.WAITING_ON_RANDOMIZER_APP

        elif not self.server or self.server.socket.closed:
            if self.app_connection_status != AppConnectionStatus.WAITING_TO_CONNECT_TO_MULTIWORLD:
                logger.info("Waiting to connect to the multiworld...")
                self.app_connection_status = AppConnectionStatus.WAITING_TO_CONNECT_TO_MULTIWORLD

        elif not self.server_connected:
            self.app_connection_status = AppConnectionStatus.AUTHENTICATING
        
        elif not self.slot_data:
            if self.app_connection_status != AppConnectionStatus.WAITING_ON_MULTIWORLD_DATA:
                logger.info("Waiting for the multiworld to send slot data...")
                self.app_connection_status = AppConnectionStatus.WAITING_ON_MULTIWORLD_DATA

        elif self.app_connection_status != AppConnectionStatus.CONNECTED:
            logger.info("Sending slot data to the OoT3D Randomizer app...")
            self.app_connection_status = AppConnectionStatus.CONNECTED
            await self.send_slot_data()
    
    async def send_slot_data(self) -> None:
        if self.slot_data is None:
            logger.info("No slot data to send")
            return

        await self.send_payload(options_to_xml(self.slot_data["options"]).encode("utf-8"), self.STAGE_SLOT_DATA)

    async def send_payload(self, payload: bytes, stage: int) -> None:
        while (await self.interface.read(self.RANDOMIZER_APP_HEADER_LOCATION + self.AP_LOCK_OFFSET, 1)) != b"\x00":
            await asyncio.sleep(0)

        current_stage = await self.interface.read_u32(self.RANDOMIZER_APP_HEADER_LOCATION + self.AP_STAGE_OFFSET)
        if current_stage != stage:
            logger.warning(f"Tried to send payload at stage {stage}, but current stage is {current_stage}")
            return

        for offset in range(0, len(payload), self.AP_PAYLOAD_SIZE):
            segment = payload[offset:offset + self.AP_PAYLOAD_SIZE]

            # Clear payload region to prevent stale data.
            await self.interface.write(self.RANDOMIZER_APP_HEADER_LOCATION + self.AP_PAYLOAD_OFFSET,
                                       bytes(self.AP_PAYLOAD_SIZE))

            # Write payload
            await self.interface.write(self.RANDOMIZER_APP_HEADER_LOCATION + self.AP_PAYLOAD_OFFSET, segment)

            # Write payload size
            await self.interface.write(self.RANDOMIZER_APP_HEADER_LOCATION + self.AP_PAYLOAD_SIZE_OFFSET,
                                       len(segment).to_bytes(4, "little"))

            if offset + len(segment) == len(payload):
                # Increment current_stage to tell the app that the payload is complete
                await self.interface.write(self.RANDOMIZER_APP_HEADER_LOCATION + self.AP_STAGE_OFFSET,
                                           bytes([(current_stage + 1) & 0xFF]))

            # set lock to 1 to tell the app it is safe to read
            await self.interface.write(self.RANDOMIZER_APP_HEADER_LOCATION + self.AP_LOCK_OFFSET, b"\x01")

            if offset + len(segment) != len(payload):
                while (await self.interface.read(self.RANDOMIZER_APP_HEADER_LOCATION + self.AP_LOCK_OFFSET, 1)) != b"\x00":
                    await asyncio.sleep(0)

    async def validate_save(self) -> None:
        pass

    async def validate_seed(self) -> None:
        if not self.server_connected or not self.slot_data:
            self.invalid = True

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect(game=self.game)
    
    def on_package(self, cmd: str, args: dict) -> None:
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            self.server_connected = True

    async def is_in_game(self) -> bool:
        return False

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        await super().disconnect(allow_autoreconnect)
        self.server_connected = False
        self.slot_data = None
        self.app_connection_status = AppConnectionStatus.NOT_CONNECTED
        self.authenticating = False

async def game_watcher(ctx: OoT3DClientContext) -> None:
    global triple_addr
    global is_3ds
    while not ctx.exit_event.is_set():
        try:
            ctx.invalid = False
            if triple_addr == "" and is_3ds:
                ctx.interface_connected = False
                ctx.interface.disconnect()
            if not ctx.interface_connected:
                title_id = RANDOMIZER_APP_TITLE_ID
                if triple_addr != "":
                    if await ctx.interface.connect(triple_addr, title_id):
                        if ctx.show_triple_connected_message:
                            logger.info("3ds connected!")
                        ctx.initial_connect = True
                        is_3ds = True
                        ctx.interface_connected = True
                        ctx.show_citra_connect_message = False
                        ctx.show_triple_connected_message = False
                    else:
                        logger.info("Couldn't connect to 3ds.")
                        ctx.interface_connected = False
                        ctx.interface.disconnect()
                        triple_addr = ""
                else:
                    ctx.interface.disconnect()
                    ctx.show_triple_connected_message = True
                    is_3ds = False
                    if ctx.show_citra_connect_message:
                        logger.info("Connecting to game...")
                    ctx.show_citra_connect_message = False
                    ctx.interface_connected = False
                    if not await ctx.interface.connect("127.0.0.1", title_id):
                        await asyncio.sleep(1)
                    else:
                        ctx.interface_connected = True
                        ctx.initial_connect = True
                        logger.info("Emulator connected!")
                if ctx.initial_connect:
                    if title_id == RANDOMIZER_APP_TITLE_ID:
                        ctx.app_type = AppType.RANDOMIZER
                    else:
                        ctx.app_type = AppType.GAME
            else:
                if ctx.initial_connect or ctx.app_type == AppType.RANDOMIZER:
                    await ctx.read_header()
                if not ctx.invalid:
                    ctx.initial_connect = False
                    await ctx.validate_seed()
                if not ctx.invalid:
                    if await ctx.is_in_game():
                        await ctx.validate_save()
        except ConnectionError as e:
            logger.error(e)
            ctx.interface.disconnect()
            ctx.interface_connected = False
            ctx.last_error = ""
            ctx.show_citra_connect_message = True
            ctx.show_triple_connected_message = True
        except Exception as e:
            logger.error(e)
            logger.error(traceback.format_exc())
            await ctx.disconnect()
            ctx.interface_connected = False
            ctx.server_connected = False
            ctx.last_error = ""
            ctx.show_citra_connect_message = True
            ctx.show_triple_connected_message = True
        await asyncio.sleep(0.25)

def launch_client(*launch_args) -> None:
    async def main():
        parser = get_base_parser()
        args = parser.parse_args(launch_args)

        ctx = OoT3DClientContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        watcher_task = asyncio.create_task(game_watcher(ctx), name="GameWatcher")

        try:
            await watcher_task
        except Exception as e:
            logger.error("".join(traceback.format_exception(e)))

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama
    colorama.init()
    asyncio.run(main())
    colorama.deinit()