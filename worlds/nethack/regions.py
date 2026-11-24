from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import NHWorld

def create_and_connect_regions(world: NHWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: NHWorld) -> None:
    foo = Region("foo", world.player, world.multiworld)
    bar = Region("bar", world.player, world.multiworld)
    world.multiworld.regions += [foo, bar]

def connect_regions(world: NHWorld) -> None:
    foo = world.get_region("foo")
    bar = world.get_region("bar")
    foo.connect(bar)
