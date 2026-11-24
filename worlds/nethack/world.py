from collections.abc import Mapping
from typing import Any

from Options import get_option_groups
from worlds.AutoWorld import World
from .web_world import NHWebWorld
from .options import NHOptions
from .locations import LOCATION_NAME_TO_ID, create_all_locations
from .items import ITEM_NAME_TO_ID, NHItem, create_all_items, create_item, randomize_item_appearances
from .regions import create_and_connect_regions
from .rules import set_all_rules

class NHWorld(World):
    """
    NetHack Desc Placeholder...
    """

    game = "NetHack"
    web = NHWebWorld()

    options_dataclass = NHOptions
    options: NHOptions

    location_name_to_id = LOCATION_NAME_TO_ID
    item_name_to_id = ITEM_NAME_TO_ID

    origin_region_name = "foo"

    randomized_appearances: Mapping[str, str]

    def generate_early(self) -> None:
        if not self.options.identify_items.value:
            randomize_item_appearances(self)
        print(self.randomized_appearances)
        
    def create_regions(self) -> None:
        create_and_connect_regions(self)
        create_all_locations(self)

    def set_rules(self) -> None:
        set_all_rules(self)

    def create_items(self) -> None:
        create_all_items(self)

    def create_item(self, name: str) -> NHItem:
        return create_item(self, name)

    # TODO
    #def get_filler_item_name(self) -> str:
    #    return get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data: Mapping[str, Any] = {}
        option_groups = get_option_groups(type(self))

        slot_data["options"] = {
            group_name: self.options.as_dict(*group_options.keys(), toggles_as_bools=True)
            for group_name, group_options in option_groups.items()
        }
        slot_data["randomized_appearances"] = self.randomized_appearances

        return slot_data
