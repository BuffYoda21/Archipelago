from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from .keys import Keys
from .location_table import location_table

if TYPE_CHECKING:
    from .world import OoT3DWorld

LOCATION_NAME_TO_ID = {name: key.value for key, (name, _) in location_table.items()}

class OoT3DLocation(Location):
    game = "Ocarina of Time 3D"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: OoT3DWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: OoT3DWorld) -> None:
    root = world.get_region(Keys.ROOT.name)
    kokiri_forest = world.get_region(Keys.KOKIRI_FOREST.name)
    for location_key, (location_name, region_key) in location_table.items():
        if region_key == Keys.ROOT:
            pass #root.add_locations({location_name: location_key}, OoT3DLocation)
        elif region_key == Keys.KOKIRI_FOREST:
            kokiri_forest.add_locations({location_name: location_key}, OoT3DLocation)

def create_events(world: OoT3DWorld) -> None:
    pass
