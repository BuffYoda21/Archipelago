from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item

from .item_table import item_table
from .keys import Keys

if TYPE_CHECKING:
    from .world import OoT3DWorld

ITEM_NAME_TO_ID = {name: key.value for key, (name, _) in item_table.items()}

class OoT3DItem(Item):
    game = "Ocarina of Time 3D"

# placeholder
def create_all_items(world: OoT3DWorld) -> None:
    # Base Itempool
    itempool: list[Item] = [
        create_item(world, world.random.choice(list(ITEM_NAME_TO_ID.keys()))) for _ in range(len(world.multiworld.get_unfilled_locations(world.player)))
    ]

    world.multiworld.itempool += itempool

def create_item(world: OoT3DWorld, item: str | int) -> OoT3DItem:
    if isinstance(item, str):
        return create_item(world, ITEM_NAME_TO_ID[item])
    return OoT3DItem(item_table[Keys(item)][0], item_table[Keys(item)][1], item, world.player)

def get_item_name(item: int) -> str:
    return item_table[Keys(item)][0]