from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import OoT3DWorld

LOCATION_NAME_TO_ID = {
    "Placeholder Location 1": 1,
    "Placeholder Location 2": 2,
    "Placeholder Location 3": 3,
    "Placeholder Location 4": 4,
    "Placeholder Location 5": 5,
    "Placeholder Location 6": 6,
}

class OoT3DLocation(Location):
    game = "Ocarina of Time 3D"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: OoT3DWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: OoT3DWorld) -> None:
    menu = world.get_region("Menu")
    menu.add_locations(LOCATION_NAME_TO_ID, OoT3DLocation)

def create_events(world: OoT3DWorld) -> None:
    pass
