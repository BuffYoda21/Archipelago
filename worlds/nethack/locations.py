from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import NHWorld

LOCATION_NAME_TO_ID = {
    "placeholder1": 1
}

class NHLocation(Location):
    game = "NetHack"

def create_all_locations(world: NHWorld) -> None:
    create_locations(world)
    create_events(world)

def create_locations(world: NHWorld) -> None:
    foo = world.get_region("foo")
    foo.add_locations({"placeholder1": 1}, NHLocation)

def create_events(world: NHWorld) -> None:
    pass
