from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item

from .item_table import item_table
from .keys import ItemKey

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

def create_item(world: OoT3DWorld, name: str) -> OoT3DItem:
    return OoT3DItem(name, item_table[ItemKey(ITEM_NAME_TO_ID[name])][1], ITEM_NAME_TO_ID[name], world.player)