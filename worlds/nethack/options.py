from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, Toggle

################
# Game Options #
################

class IdentifyItems(Toggle):
    """
    Should all items be identified by the server? Items will not be
    identified in game until you formally identify them but it will
    be very easy to figure out when you get sent an item since the
    identified name will be used by the server.

    Disabling this option is currently expiremental and if stability
    is required, it is recommended to keep toggled on.
    """
    display_name = "Server Identified Items"
    default = True

class Trapsanity(Toggle):
    """
    Randomly placed traps are added as item locations and added to
    the item pool as trap items.
    """
    display_name = "Trapsanity"
    default = False

class NoEarlyPoly(Toggle):
    """
    Prevents poly traps from appearing earlier than they would usually
    generate.

    Only applies if trapsanity is enabled.
    """
    display_name = "No Early Poly Traps"
    default = True

class ItemsPerDlvlMin(Range):
    """
    Min number of AP items to place on each DLVL. If all items cannot
    be placed upon generating the level, they will have a small chance
    of dropping from monsters killed on that level. You can check the
    number of remaining uncollected AP items on a DLVL with #ap
    """
    display_name = "AP Items Per DLVL Min"
    range_start = 1
    range_end = 30
    default = 5

class ItemsPerDlvlMax(Range):
    """
    Max number of AP items to place on each DLVL. If all items cannot
    be placed upon generating the level, they will have a small chance
    of dropping from monsters killed on that level. You can check the
    number of remaining uncollected AP items on a DLVL with #ap
    """
    display_name = "AP Items Per DLVL Max"
    range_start = 1
    range_end = 30
    default = 20

class PercentItemsRandomized(Range):
    """
    Percent of naturally generated items to attempt to convert to AP
    items (if there are items left to convert).
    """
    display_name = "Percent of Items to Randomize"
    range_start = 0
    range_end = 100
    default = 50

class Skillsanity(Toggle):
    """
    Adds skill points to the item pool. You can immediately spend skill
    points on whatever skill you want regardless of how much you have
    trained that specific skill.
    """
    display_name = "Skillsanity"
    default = False

class Dlvlsanity(Toggle):
    """
    To progress deeper in the dungeon, you need progressive DLVL items.
    """
    display_name = "DLVLsanity"
    default = False

class LockObjectClasses(Toggle):
    """
    In order to use any given item, you need to unlock the permit for
    it's object class first (classes are denoted by what glyph the item
    uses).

    WARNING:
    This option will make the early game very difficult. It is
    not recommended unless you have experience playing with
    various conducts, are willing to add some of the permits
    to your starting items, or are prepared to die a lot early
    on.

    Without the cooresponding permit:
    Coins ($): Cannot be picked up
    Amulets ("): Cannot be worn
    Weapons ()): Cannot be wielded or thrown
    Armor ([): Cannot be worn
    Comestibles (%): Cannot be picked up but can be eaten off the floor
    Scrolls (?): Cannot be read
    Spellbooks (+): Cannot be read
    Potions (!): Cannot be quaffed or thrown
    Wands (/): Cannot be zapped or applied
    Tools ((): Cannot be applied, worn, thrown, or wielded
    Gems (*): Cannot be picked up
    """
    display_name = "Item Class Permits"
    default = False

@dataclass
class NHOptions(PerGameCommonOptions):
    # Game Options
    identify_items:                 IdentifyItems
    trapsanity:                     Trapsanity
    no_early_poly:                  NoEarlyPoly
    items_per_dlvl_min:             ItemsPerDlvlMin
    items_per_dlvl_max:             ItemsPerDlvlMax
    percent_items_randomized:       PercentItemsRandomized
    skillsanity:                    Skillsanity
    dlvlsanity:                     Dlvlsanity
    lock_object_classes:            LockObjectClasses

option_groups = [
    
]

option_presets = {
    
}
