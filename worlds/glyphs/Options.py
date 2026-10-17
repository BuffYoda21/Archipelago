from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, DeathLink, OptionGroup, OptionSet, Toggle, Range



# Game Options
class Goal(Choice):
    """
    Determines what ending must be reached for Archipelago to consider your game as complete.
    Note: This option does not affect location/item pools so you still may have to complete more of the game than you would think.
    """
    display_name = "Completion Requirements"
    option_false_ending = 1
    option_good_ending = 2
    option_true_ending = 3
    option_all_star_endings = 4
    option_epilogue = 5
    option_all_endings = 6
    default = option_true_ending

class StartingSword(Toggle):
    """
    Start the game with the sword.
    """
    display_name = "Starting Sword"
    default = False

class StartingDash(Toggle):
    """
    Start the game with dash unlocked.
    """
    display_name = "Starting Dash"
    default = False



# Randomization Options
## Possible future addition
# class RandomizeWorldSpawn(Toggle):
#     """
#     Shuffles what save button you start on.
#     If false, you will start at the standard spawn point.
#     """
#     display_name = "Randomize World Spawn"

class RandomShopPrices(Toggle):
    """
    Randomizes the prices of shop items.
    Never exceeds 10 total.
    """
    display_name = "Randomize Shop Prices"
    default = True

class RandomButtonColorPercent(Range):
    """
    Percent of buttons to randomize the color of.
    """
    display_name = "Random Button Colors Percent"
    range_start = 0
    range_end = 100
    default = 0

class ExcludeBlack(Toggle):
    """
    Ensures no buttons are randomized to black.
    """
    display_name = "No Black Buttons"
    default = False

class ButtonSanity(Toggle):
    """
    Adds every button in the game as an item location.
    """
    display_name = "Buttonsanity"
    default = False

class ButtonShardPercent(Range):
    """
    Percent of buttons to be broken and have shards added to the item pool.
    Buttonsanity must be enabled for this to work.
    May be automatically reduced if there are not enough locations in the multiworld.
    """
    display_name = "Button Shard Percent"
    range_start = 0
    range_end = 100
    default = 0

class ShardBundleMinSize(Range):
    """
    Minimum number of shards to include in a shard bundle.
    Bundles of size 1 will be treated as a single shard instead of a bundle.
    """
    display_name = "Shard Bundle Minimum Size"
    range_start = 1
    range_end = 50

class ShardBundleMaxSize(Range):
    """
    Maximum number of shards to include in a shard bundle.
    Bundles of size 1 will be treated as a single shard instead of a bundle.
    """
    display_name = "Shard Bundle Maximum Size"
    range_start = 1
    range_end = 50

class EnableTraps(Toggle):
    """
    Adds traps to the itempool
    """
    display_name = "Enable Traps"
    default = True

class TrapTypes(OptionSet):
    """
    Determines what kinds of traps will be added to the item pool
    Valid Keys:
    Momentum Trap: Launches the player at a random angle
    John Trap: Spawns John for 30 seconds
    Slow Trap: Slows the player down for 30 seconds
    Screen Flip Trap: Flips the player's screen for 30 seconds
    Dash Trap: Slows the player's dash for 30 seconds
    """
    display_name = "Trap Types"
    valid_keys = {
        "Momentum Trap",
        "John Trap",
        "Slow Trap",
        "Screen Flip Trap",
        "Dash Trap",
    }
    default = {
        "Momentum Trap",
        "John Trap",
        "Slow Trap",
        "Screen Flip Trap",
        "Dash Trap",
    }

class HatShuffle(Toggle):
    """
    Include hats in the item pool
    If enabled, hats will replace some junk items and traps
    If disabled, all hats will be included in starting inventory
    """
    display_name = "Shuffle Hats"
    default = True



# Logical Options
class SwordlessCombat(Toggle):
    """
    Swordless combat is considered in logic.
    Ex: Fighting with only dash attacks
    """
    display_name = "Swordless Combat"
    default = False

class DashPuzzlesSolved(Toggle):
    """
    Logic assumes you already have the answer to all the puzzles in the game written down somewhere.
    """
    display_name = "Assume Puzzles Solved"
    default = False

class LogicalWallJumps(Toggle):
    """
    Considers skips utilizing wall jumps in logic.
    """
    display_name = "Wall Jumps in Logic"
    default = False

## Very niche and if it ever ends up being logically relevant, it will probably just be out of logic anyway
# class LogicalWallJumpChains(Toggle):
#    """
#    Considers skips that require multiple consecutive wall jumps (2-3) in logic.
#    Does nothing if "Wall Jumps in Logic" is not enabled.
#    """
#    display_name = "Wall Jump Chains in Logic"

class FlowerPuzzleSkips(Toggle):
    """
    Considers skips utilizing the flower puzzle in logic.
    """
    display_name = "Flower Puzzle in Logic"
    default = False



# Open Settings
class WizardRequirements(Range):
    """
    Determines the number of glyphstones required to trigger the wizard fight
    """
    display_name = "Wizard Glyphstones"
    range_start = 0
    range_end = 3
    default = 3

class WraithRequirements(Choice):
    """
    Determines requirements to enter the Wraith boss room.
    None: Boss room can be entered without any additional items
    Vanilla: Boss room requires 15 silver shards
    Intended: Boss room requires 15 silver shards and 3 glyphstones
    Silver Shards: Boss room requires a configurable number of silver shards
    Gold Shards: Boss room requires a configurable number of gold shards
    Smile Tokens: Boss room requires a configurable number of smile tokens
    Rune Cubes: Boss room requires a configurable number of rune cubes
    Glyphstones: Boss room requires a configurable number of glyphstones
    """
    display_name = "Wraith Requirements"
    option_none = 0
    option_vanilla = 1
    option_intended = 2
    option_silver_shards = 3
    option_gold_shards = 4
    option_smile_tokens = 5
    option_rune_cubes = 6
    option_glyphstones = 7
    default = option_none

class WraithSilverCount(Range):
    """
    The number of silver shards required to enter the wraith boss room.
    """
    display_name = "Wraith Silver Shards"
    range_start = 1
    range_end = 15
    default = 15

class WraithGoldCount(Range):
    """
    The number of gold shards required to enter the wraith boss room.
    """
    display_name = "Wraith Gold Shards"
    range_start = 1
    range_end = 3
    default = 3

class WraithSmileCount(Range):
    """
    The number of smile tokens required to enter the wraith boss room.
    """
    display_name = "Wraith Smile Tokens"
    range_start = 1
    range_end = 10
    default = 10

class WraithRuneCount(Range):
    """
    The number of rune cubes required to enter the wraith boss room.
    """
    display_name = "Wraith Rune Cubes"
    range_start = 1
    range_end = 3
    default = 3

class WraithGlyphstoneCount(Range):
    """
    The number of glyphstones required to enter the wraith boss room.
    """
    display_name = "Wraith Glyphstones"
    range_start = 1
    range_end = 3
    default = 3



@dataclass
class GlyphsOptions(PerGameCommonOptions):
    # Game Options
    Goal:                       Goal
    StartingSword:              StartingSword
    StartingDash:               StartingDash
    DeathLink:                  DeathLink

    # Randomization Options
  # RandomizeWorldSpawn:        RandomizeWorldSpawn
    RandomShopPrices:           RandomShopPrices
    RandomButtonColorPercent:   RandomButtonColorPercent
    ExcludeBlack:               ExcludeBlack
    ButtonSanity:               ButtonSanity
    ButtonShardPercent:         ButtonShardPercent
    ShardBundleMinSize:         ShardBundleMinSize
    ShardBundleMaxSize:         ShardBundleMaxSize
    EnableTraps:                EnableTraps
    TrapTypes:                  TrapTypes
    HatShuffle:                 HatShuffle

    # Logical Options
    SwordlessCombat:            SwordlessCombat
    DashPuzzlesSolved:          DashPuzzlesSolved
    LogicalWallJumps:           LogicalWallJumps
  # LogicalWallJumpChains:      LogicalWallJumpChains
    FlowerPuzzleSkips:          FlowerPuzzleSkips

    # Open Settings
    WizardRequirements:         WizardRequirements
    WraithRequirements:         WraithRequirements
    WraithSilverCount:          WraithSilverCount
    WraithGoldCount:            WraithGoldCount
    WraithSmileCount:           WraithSmileCount
    WraithRuneCount:            WraithRuneCount
    WraithGlyphstoneCount:      WraithGlyphstoneCount

option_groups = [
    OptionGroup(
        "Game Options",
        [
            Goal,
            StartingSword,
            StartingDash,
            DeathLink,
        ]
    ),
    OptionGroup(
        "Randomization Options",
        [
            RandomShopPrices,
            RandomButtonColorPercent,
            ExcludeBlack,
            ButtonSanity,
            ButtonShardPercent,
            ShardBundleMinSize,
            ShardBundleMaxSize,
            EnableTraps,
            TrapTypes,
            HatShuffle,
        ]
    ),
    OptionGroup(
        "Logical Options",
        [
            SwordlessCombat,
            DashPuzzlesSolved,
            LogicalWallJumps,
            FlowerPuzzleSkips,
        ]
    ),
    OptionGroup(
        "Open Settings",
        [
            WizardRequirements,
            WraithRequirements,
            WraithSilverCount,
            WraithGoldCount,
            WraithSmileCount,
            WraithRuneCount,
            WraithGlyphstoneCount,
        ]
    ),
]