from collections.abc import Mapping
from typing import Any

from Options import OptionError, get_option_groups
from worlds.AutoWorld import World
from .client.utils import options_to_xml

from .keys import Keys
from .item_table import item_table
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

    origin_region_name = Keys.ROOT.name

    def generate_early(self) -> None:
        self.validate_options()

    def validate_options(self) -> None:
        NOVICE = 1
        INTERMEDIATE = 2
        ADVANCED = 3
        EXPERT = 4
        HERO = 5

        def clamp(glitch: oot3d_options.Glitch, max_value: int):
            if glitch.value > max_value:
                glitch.value = max_value

        clamp(self.options.restricted_items, NOVICE)
        clamp(self.options.super_stab, NOVICE)
        clamp(self.options.infinite_sword_glitch, ADVANCED)
        clamp(self.options.bomb_hover, ADVANCED)
        clamp(self.options.ocarina_items_bomb, EXPERT)
        clamp(self.options.hover_boost, ADVANCED)
        clamp(self.options.extend_super_slide, EXPERT)
        clamp(self.options.megaflip, HERO)
        clamp(self.options.a_slide, EXPERT)
        clamp(self.options.hammer_slide, INTERMEDIATE)
        clamp(self.options.ledge_cancel, ADVANCED)
        clamp(self.options.action_swap, ADVANCED)
        if self.options.action_swap.value == INTERMEDIATE:
            self.options.quick_put_away.value = NOVICE # This specific glitch doesn't have an intermediate value
        clamp(self.options.quick_put_away, EXPERT)
        clamp(self.options.hookshot_clip, INTERMEDIATE)
        clamp(self.options.hookshot_jump_bonk, ADVANCED)
        clamp(self.options.hookshot_jump_boots, ADVANCED)
        clamp(self.options.cutscene_dives, ADVANCED)
        clamp(self.options.navi_dive_stick, ADVANCED)
        clamp(self.options.triple_slash_clip, EXPERT)
        clamp(self.options.ledge_clip, ADVANCED)
        clamp(self.options.seam_walk, HERO)

        if self.options.rupoor_trap.value != self.options.rupoor_trap.option_off:
            self.options.rupoor_trap_toggle.value = True
        else:
            self.options.rupoor_trap_toggle.value = 0

        if self.options.rupoor_trap_toggle.value == 0:
            self.options.rupoor_trap.value = self.options.rupoor_trap.option_off

        if bool(self.options.set_dungeon_types.value):
            mq_dungeon_options: list[oot3d_options.OoT3DChoice] = [
                self.options.deku_tree_dungeon_type,
                self.options.dodongos_cavern_dungeon_type,
                self.options.jabu_jabus_belly_dungeon_type,
                self.options.forest_temple_dungeon_type,
                self.options.fire_temple_dungeon_type,
                self.options.water_temple_dungeon_type,
                self.options.spirit_temple_dungeon_type,
                self.options.shadow_temple_dungeon_type,
                self.options.bottom_of_the_well_dungeon_type,
                self.options.ice_cavern_dungeon_type,
                self.options.training_grounds_dungeon_type,
                self.options.ganons_castle_dungeon_type,
            ]
            mq_count = 0
            for option in mq_dungeon_options:
                mq_count += option.value
            self.options.mq_dungeon_count.value = mq_count

        if (self.options.forest_open.value == self.options.forest_open.option_closed and
            self.options.starting_age.value == self.options.starting_age.option_adult):
            if bool(self.options.autocorrect_yaml.value):
                self.options.forest_open.value = self.options.forest_open.option_closed_deku
            else:
                raise OptionError("Starting as adult is incompatible with closed forest")

        if (self.options.starting_age.value == self.options.starting_age.option_adult and
            self.options.door_time_open.value == self.options.door_time_open.option_intended and
            self.options.shuffle_ocarinas.value == False and
            self.options.start_inventory.value.get(items.get_item_name(Keys.PROGRESSIVE_OCARINA), 0) == 0):
            if bool(self.options.autocorrect_yaml.value):
                self.options.start_inventory.value.update({items.get_item_name(Keys.PROGRESSIVE_OCARINA): 1})
            else:
                raise OptionError("\nStarting as adult is incompatible with\n" +
                                  "intended door of time and unshuffled\n" +
                                  "ocarinas unless you have a progressive\n" +
                                  "ocarina in your starting inventory")

        maxHearts = 20
        if self.options.item_pool.value == self.options.item_pool.option_minimal:
            maxHearts = 3
        elif self.options.item_pool.value == self.options.item_pool.option_scarce:
            maxHearts = 12

        heartErrorMessage = ("\nNot enough Hearts in pool!\n\n" +
                             "Please choose a different Item Pool\n" + 
                             "setting or lower the Hearts requirement.")
        
        if self.options.bridge_open.value == self.options.bridge_open.option_hearts and self.options.bridge_heart_count.value > maxHearts:
            if bool(self.options.autocorrect_yaml.value):
                self.options.bridge_heart_count.value = maxHearts
            else:
                raise OptionError(heartErrorMessage)
            
        if self.options.shuffle_ganons_boss_key.value == self.options.shuffle_ganons_boss_key.option_LACS_hearts and self.options.shuffle_lacs_heart_count.value > maxHearts:
            if bool(self.options.autocorrect_yaml.value):
                self.options.shuffle_lacs_heart_count.value = maxHearts
            else:
                raise OptionError(heartErrorMessage)

        if (self.options.gloom_mode.value != self.options.gloom_mode.option_off and
           (self.options.bridge_open.value == self.options.bridge_open.option_hearts or
            self.options.shuffle_ganons_boss_key.value == self.options.shuffle_ganons_boss_key.option_LACS_hearts)):
            if bool(self.options.autocorrect_yaml.value):
                self.options.gloom_mode.value = self.options.gloom_mode.option_off
            else:
                raise OptionError("\nGloom Mode is incompatible with Heart\n" + 
                                  "requirements for LACS or Rainbow Bridge.")

        if (self.options.mq_dungeon_count.value != 0 and self.options.logic.value != self.options.logic.option_no_logic and 
           (self.options.shuffle_enemy_souls.value == self.options.shuffle_enemy_souls.option_all_enemies or bool(self.options.enemy_randomizer.value))):
            if bool(self.options.autocorrect_yaml.value):
                self.options.mq_dungeon_count.value = 0
                self.options.set_dungeon_types.value = False
            else:
                raise OptionError("\nThe following features currently do not\n" +
                                  "support logic for Master Quest dungeons.\n" +
                                  "To use them you must disable Logic OR\n" +
                                  "set MQ Dungeon Count to 0.\n\n" +
                                  "- Enemy Randomizer\n" +
                                  "- Shuffle Enemy Souls")
        
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.OoT3DItem:
        return items.create_item(self, name)
    
    #def get_filler_item_name(self) -> str:
    #    return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data: Mapping[str, Any] = {}
        option_groups = get_option_groups(type(self))

        slot_data["options"] = {
            group_name: self.options.as_dict(*group_options.keys(), toggles_as_bools=True)
            for group_name, group_options in option_groups.items()
        }
        slot_data["option_xml"] = options_to_xml(slot_data["options"]) # debug

        return slot_data
