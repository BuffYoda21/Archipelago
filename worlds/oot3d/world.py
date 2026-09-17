from collections.abc import Mapping
from typing import Any

from Options import get_option_groups
from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as oot3d_options

class OoT3DWorld(World):
    """
    OoT3D Desc Placeholder...
    """

    game = "Ocarina of Time 3D"
    web = web_world.OoT3DWebWorld()

    options_dataclass = oot3d_options.OoT3DOptions
    options: oot3d_options.OoT3DOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.OoT3DItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data: Mapping[str, Any] = {}
        option_groups = get_option_groups(type(self))

        slot_data["options"] = {
            group_name: self.options.as_dict(*group_options.keys(), toggles_as_bools=True)
            for group_name, group_options in option_groups.items()
        }

        return slot_data
