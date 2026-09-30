from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .keys import Keys

if TYPE_CHECKING:
    from .world import OoT3DWorld

def create_and_connect_regions(world: OoT3DWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: OoT3DWorld) -> None:
    root = Region(Keys.ROOT.name, world.player, world.multiworld)
    kokiri_forest = Region(Keys.KOKIRI_FOREST.name, world.player, world.multiworld)
    world.multiworld.regions += [root, kokiri_forest]

def connect_regions(world: OoT3DWorld) -> None:
    root = world.get_region(Keys.ROOT.name)
    kokiri_forest = world.get_region(Keys.KOKIRI_FOREST.name)
    root.connect(kokiri_forest)
