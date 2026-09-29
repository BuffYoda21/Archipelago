from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import OoT3DWorld

def create_and_connect_regions(world: OoT3DWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: OoT3DWorld) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions += [menu]

def connect_regions(world: OoT3DWorld) -> None:
    pass
