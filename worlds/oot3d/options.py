from dataclasses import dataclass

from Options import T, Choice, NamedRange, OptionGroup, OptionSet, PerGameCommonOptions, Range, Toggle

#################
# Open Settings #
#################

class OpenForest(Choice):
    """
    Open:
    Mido no longer blocks the path to the Deku Tree,
    and the Kokiri boy no longer blocks the path out
    of the forest.

    Closed Deku:
    The Kokiri boy no longer blocks the path out of
    the forest, but Mido still blocks the path to the
    Deku Tree, requiring Kokiri Sword and Deku Shield
    to access the Deku Tree.

    Closed:
    Beating Deku Tree is logically required to leave
    the forest area (Kokiri Forest/Lost Woods/Sacred
    Forest Meadow/Deku Tree), while the Kokiri Sword
    and a Deku Shield are required to access the Deku
    Tree. Items needed for this will be guaranteed
    inside the forest area. This setting is
    incompatible with starting as adult.
    """
    display_name = "Forest"
    option_open = 1
    option_closed_deku = 2
    option_closed = 3
    default = option_open

class OpenKakarikoGate(Choice):
    """
    Open:
    The gate is always open instead of needing
    Zelda's Letter. The Happy Mask Shop opens upon
    obtaining Zelda's Letter without needing to show
    it to the guard.

    Closed:
    The gate and the Happy Mask Shop both remain
    closed until showing Zelda's Letter to the guard
    in Kakariko.
    """
    display_name = "Kakariko Gate"
    option_open = 1
    option_closed = 2
    default = option_closed

class OpenDoorOfTime(Choice):
    """
    Open:
    The Door of Time starts opened instead of needing
    to play the Song of Time.

    Closed:
    Only an Ocarina and the Song of Time need to be
    found to open the Door of Time.

    Intended:
    The Ocarina of Time, the Song of Time, and
    all Spiritual Stones need to be found to
    open the Door of Time.
    """
    display_name = "Door of Time"
    option_open = 1
    option_closed = 2
    option_intended = 3
    default = option_open

class OpenZorasFountain(Choice):
    """
    Normal:
    King Zora obstructs the way to Zora's Fountain.
    Ruto's Letter must be shown as child in order to
    move him for both eras.

    Adult:
    King Zora is always moved in the adult era. This
    means Ruto's Letter is only required to access
    Zora's Fountain as child.

    Open:
    King Zora starts as moved in both the child and
    adult eras. This also removes Ruto's Letter from
    the pool since it can't be used.
    """
    display_name = "Zora's Fountain"
    option_normal = 1
    option_adult = 2
    option_open = 3
    default = option_normal

class OpenJabuJabu(Choice):
    """
    Open:
    Jabu-Jabu's mouth is always open.

    Closed:
    Jabu-Jabu's mouth stays closed until a fish is
    fed.
    """
    display_name = "Jabu-Jabu"
    option_open = 1
    option_closed = 2
    default = option_closed

class OpenGerudoFortress(Choice):
    """
    Normal:
    All 4 carpenters can be rescued.

    Fast:
    Only the bottom left carpenter must be rescued.

    Open:
    The carpenters are rescued from the start of the
    game, and if Shuffle Gerudo Card is disabled,
    the player starts with the Gerudo Card in the
    inventory allowing access to Gerudo Training
    Grounds.
    """
    display_name = "Gerudo Fortress"
    option_normal = 1
    option_fast = 2
    option_open = 3
    default = option_normal

class OpenRainbowBridge(Choice):
    """
    Open:
    The Rainbow Bridge is always present.

    Vanilla:
    The Rainbow Bridge requires Shadow and Spirit
    Medallions as well as Light Arrows.

    Stones/Medallions/Rewards/Tokens/Hearts:
    The Rainbow Bridge requires collecting a
    configurable number of Spiritual Stones,
    Medallions, Dungeon Rewards, Gold Skulltula
    Tokens, or Hearts.

    Dungeons:
    The Rainbow Bridge requires completing a
    configurable number of Dungeons.

    Dungeons are considered complete when Link steps
    into the blue warp at the end of them.
    """
    display_name = "Rainbow Bridge"
    option_open = 1
    option_vanilla = 2
    option_stones = 3
    option_medallions = 4
    option_rewards = 5
    option_dungeons = 6
    option_tokens = 7
    option_hearts = 8
    default = option_medallions

class BridgeStoneCount(Range):
    """
    Set the number of Spiritual Stones required to
    spawn the Rainbow Bridge.
    """
    display_name = "Rainbow Bridge Stone Count"
    range_start = 0
    range_end = 3
    default = 3

class BridgeMedallionCount(Range):
    """
    Set the number of Medallions required to spawn
    the Rainbow Bridge.
    """
    display_name = "Rainbow Bridge Medallion Count"
    range_start = 0
    range_end = 6
    default = 6

class BridgeDungeonRewardsCount(Range):
    """
    Set the number of Dungeon Rewards (Spiritual
    Stones and Medallions) required to spawn the
    Rainbow Bridge.
    """
    display_name = "Rainbow Bridge Dungeon Reward Count"
    range_start = 0
    range_end = 9
    default = 9

class BridgeDungeonCount(Range):
    """
    Set the number of completed dungeons required to
    spawn the Rainbow Bridge.
    """
    display_name = "Rainbow Bridge Dungeon Count"
    range_start = 0
    range_end = 8
    default = 8

class BridgeTokenCount(Range):
    """
    Set the number of Gold Skulltula Tokens required
    to spawn the Rainbow Bridge.
    """
    display_name = "Rainbow Bridge Token Count"
    range_start = 0
    range_end = 100
    default = 100

class BridgeHeartCount(Range):
    """
    Set the number of Hearts required to spawn the
    Rainbow Bridge.
    """
    display_name = "Rainbow Bridge Heart Count"
    range_start = 0
    range_end = 20
    default = 20

class RandomGanonsTrials(Toggle):
    """
    Sets a random number of required trials to enter
    Ganon's Tower.
    """
    display_name = "Random Ganon's Trials"
    default = True

class TrialCount(Range):
    """
    Set the number of trials required to enter
    Ganon's Tower. Trials will be randomly selected.
    """
    display_name = "Trial Count"
    range_start = 0
    range_end = 6
    default = 6

##################
# World Settings #
##################

class StartingAge(Choice):
    """
    Choose which age Link will start as.
    
    Only the child option is compatible with Closed
    Forest.

    Child will also be forced if Door of Time is set
    to intended and ocarinas are unshuffled unless you
    start with an ocarina already in your inventory.
    """
    display_name = "Starting Age"
    option_child = 1
    option_adult = 2
    default = option_child

class ShuffleEntrances(Toggle):
    """
    Shuffle where the entrances between areas lead to
    If turned on, select which kinds of entrances you
    want shuffled in the options below. Note that some
    types of entrances can have wildly varying
    generation times.
    """
    display_name = "Shuffle Entrances"
    default = False

class ShuffleDungeonEntrances(Choice):
    """
    Shuffle the pool of dungeon entrances, including
    Bottom of the Well, Ice Cavern, and Gerudo
    Training Grounds. Shuffling Ganon's Castle can
    be enabled separately.
    
    Additionally, the entrances of Deku Tree, Fire
    Temple, Bottom of the Well and Gerudo Training
    Ground are opened for both adult and child.
    """
    display_name = "Shuffle Dungeon Entrances"
    option_off = 1
    option_on = 2
    option_on_plus_ganon = 3
    default = option_off

    @classmethod
    def get_option_name(cls, value: T) -> str: # type: ignore
        if value == cls.option_on_plus_ganon:
            return "On + Ganon"
        return super().get_option_name(value) # type: ignore
        

class ShuffleBossEntrances(Choice):
    """
    Shuffle the pool of dungeon boss entrances.
    This affects the boss rooms of all stone and
    medallion dungeons.
    
    Child and adult boss rooms can be shuffled
    separately.
    Child may be expected to defeat Phantom Ganon
    and/or Bongo Bongo.
    """
    display_name = "Shuffle Boss Entrances"
    option_off = 1
    option_age_restricted = 2
    option_full = 3
    default = option_off

class ShuffleOverworldEntrances(Choice):
    """
    Shuffle the pool of Overworld entrances, which
    corresponds to almost all loading zones between
    Overworld areas.
    
    Some entrances are unshuffled to avoid issues:
    - Hyrule Castle Courtyard and Garden entrance
    - Both Market Back Alley entrances
    - Gerudo Valley to Lake Hylia (unless entrances
      are decoupled)
    """
    display_name = "Shuffle Overworld Entrances"
    option_off = 1
    option_on = 2
    default = option_off

class ShuffleInteriorEntrances(Choice):
    """
    Off:
    Interior entrances will not be shuffled.

    Simple:
    Shuffle the pool of interior entrances which
    contains most Houses and all Great Fairies.

    All:
    An extended version of 'Simple' with some extra
    places:
    - Windmill
    - Link's House
    - Temple of Time
    - Kakariko Potion Shop.
    """
    display_name = "Shuffle Interior Entrances"
    option_off = 1
    option_simple = 2
    option_all = 3
    default = option_off

class ShuffleGrottosEntrances(Choice):
    """
    Shuffle the pool of grotto entrances, including
    all graves, small Fairy Fountains and the Lost
    Woods Stage.
    """
    display_name = "Shuffle Grottos Entrances"
    option_off = 1
    option_on = 2
    default = option_off

class ShuffleOwlDrops(Choice):
    """
    Randomize where Kaepora Gaebora (the Owl) drops
    you at when you talk to him at Lake Hylia or at
    the top of Death Mountain Trail.
    """
    display_name = "Shuffle Owl Drops"
    option_off = 1
    option_on = 2
    default = option_off

class ShuffleWarpSongs(Choice):
    """
    Randomize where each of the 6 warp songs leads to.
    """
    display_name = "Shuffle Warp Songs"
    option_off = 1
    option_on = 2
    default = option_off

class ShuffleOverworldSpawns(Choice):
    """
    Randomize where you start as Child or Adult when
    loading a save in the Overworld. This means you
    may not necessarily spawn inside Link's House or
    Temple of Time.
    
    This stays consistent after saving and loading the
    game again.
    """
    display_name = "Shuffle Overworld Spawns"
    option_off = 1
    option_on = 2
    default = option_off

class MixedEntrancePools(Toggle):
    """
    Shuffle entrances into a mixed pool instead of
    separate ones. For example, enabling the settings
    to shuffle grotto, dungeon, and overworld
    entrances and selecting grotto and dungeon
    entrances here will allow a dungeon to be inside a
    grotto or vice versa, while overworld entrances
    are shuffled in their own separate pool and
    indoors stay vanilla.
    """
    display_name = "Mixed Entrance Pools"
    default = False

class MixDungeons(Toggle):
    """
    Dungeon entrances will be part of the mixed pool.
    """
    display_name = "Mix Dungeons"
    default = False

class MixOverworld(Toggle):
    """
    Overworld entrances will be part of the mixed
    pool.
    """
    display_name = "Mix Overworld"
    default = False

class MixInterior(Toggle):
    """
    Interior entrances will be part of the mixed pool.
    """
    display_name = "Mix Interior"
    default = False

class MixGrottos(Toggle):
    """
    Grotto entrances will be part of the mixed pool.
    """
    display_name = "Mix Grottos"
    default = False

class DecoupleEntrances(Toggle):
    """
    Decouple entrances when shuffling them. This means
    you are no longer guaranteed to end up back where
    you came from when you go back through an
    entrance. This also adds the one-way entrance from
    Gerudo Valley to Lake Hylia in the pool of
    overworld entrances when they are shuffled.
    Boss entrances are currently excluded from this
    and remain coupled regardless.
    """
    display_name = "Decouple Entrances"
    default = False

class BombchusInLogic(Toggle):
    """
    Bombchus are properly considered in logic.
    They can be replenished in shops, or through
    bombchu drops, if those are enabled.
    
    Bombchu Bowling is opened by bombchus.
    """
    display_name = "Bombchus in Logic"
    default = False

class AmmoDrops(Choice):
    """
    On:
    Bombs, arrows, seeds, nuts, sticks and
    magic jars appear as normal.

    On + Bombchu:
    Bombs, arrows, seeds, nuts, sticks and
    magic jars appear as normal.
    Bombchus can sometimes replace bomb drops.

    Off:
    All ammo drops will be replaced by blue rupees,
    except for Deku Sticks.
    Ammo upgrades will only refill ammo by 10 units.
    """
    display_name = "Ammo Drops"
    option_on = 1
    option_on_plus_bombchu = 2
    option_off = 3
    default = option_on_plus_bombchu

    @classmethod
    def get_option_name(cls, value: T) -> str: # type: ignore
        if value == cls.option_on_plus_bombchu:
            return "On + Bombchu"
        return super().get_option_name(value) # type: ignore

class HeartDropsAndRefills(Choice):
    """
    On:
    Heart drops will appear as normal.
    Health upgrades fully heal Link when picked up.
    Fairies heal Link as normal.

    No Drop:
    Heart drops will be replaced by green rupees.
    Health upgrades fully heal Link when picked up.
    Fairies heal Link as normal.

    No Refill:
    Heart drops will appear as normal.
    Health upgrades don't heal Link when picked up.
    Fairies heal Link by only 3 hearts.

    Off:
    Heart drops will be replaced by green rupees.
    Health upgrades don't heal Link when picked up.
    Fairies heal Link by only 3 hearts.
    """
    display_name = "Heart Drops and Refills"
    option_on = 1
    option_no_drop = 2
    option_no_refill = 3
    option_off = 4
    default = option_on

class MQDungeonCount(Range):
    """
    Specify the number of Master Quest dungeons to
    appear in the game. Which dungeons become Master
    Quest will be chosen at random.
    """
    display_name = "MQ Dungeon Count"
    range_start = 0
    range_end = 12
    default = 0

class SetDungeonTypes(Toggle):
    """
    If set, you can choose specific dungeons to be
    vanilla, MQ, or random
    """
    display_name = "Set Dungeon Types"
    default = False

class DekuTreeDungeonType(Choice):
    display_name = "Deku Tree Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class DodongosCavernDungeonType(Choice):
    display_name = "Dodongo's Cavern Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class JabuJabusBellyDungeonType(Choice):
    display_name = "Jabu Jabu's Belly Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class ForestTempleDungeonType(Choice):
    display_name = "Forest Temple Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class FireTempleDungeonType(Choice):
    display_name = "Fire Temple Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class WaterTempleDungeonType(Choice):
    display_name = "Water Temple Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class SpiritTempleDungeonType(Choice):
    display_name = "Spirit Temple Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class ShadowTempleDungeonType(Choice):
    display_name = "Shadow Temple Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class BottomOfTheWellDungeonType(Choice):
    display_name = "Bottom of the Well Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class IceCavernDungeonType(Choice):
    display_name = "Ice Cavern Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class TrainingGroundsDungeonType(Choice):
    display_name = "Training Grounds Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class GanonsCastleDungeonType(Choice):
    display_name = "Ganon's Castle Dungeon Type"
    option_vanilla = 0
    option_master_quest = 1
    default = "random"

class TriforceHunt(Toggle):
    """
    Pieces of the Triforce have been scattered around
    the world. Find some of them to beat the game.
    
    Game is saved on completion, and Ganon's Castle
    key is given if beating the game again is desired.
    """
    display_name = "Triforce Hunt"
    default = False

class TriforcePieces(Range):
    """
    Set the total number of pieces that will appear
    in the world.
    """
    display_name = "Total Triforce Pieces"
    range_start = 1
    range_end = 200
    default = 30

class RequiredTriforcePieces(Range):
    """
    Set the number of pieces required to beat the
    game.
    """
    display_name = "Required Triforce Pieces"
    range_start = 1
    range_end = 100
    default = 20

####################
# Enemy Randomizer #
####################

class EnemyRandomizer(Toggle):
    """
    Randomize most enemies in the game.
    WARNING: Incompatible with Master Quest Logic.
    """
    display_name = "Enemy Randomizer"
    default = False

global random_enemy_docstring
random_enemy_docstring = """
Randomized:
This enemy will be included in the pool of
random enemies.

Vanilla:
This enemy will be excluded from the random pool,
but it will appear at its vanilla locations.

Removed:
This enemy will be excluded from the random pool,
and it won't appear at randomized locations.
Exception: if all possible options for a location
are removed, that location will revert to using
its vanilla enemy.
"""

class RandomizedEnemy(Choice):
    __doc__ = random_enemy_docstring
    option_randomized = 1
    option_vanilla = 2
    option_removed = 3
    default = option_randomized

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__doc__ is None:
            cls.__doc__ = random_enemy_docstring

class Anubis(RandomizedEnemy):
    display_name = "Anubis"
    
class Armos(RandomizedEnemy):
    display_name = "Armos"

class Bari(RandomizedEnemy):
    display_name = "Bari"

class Beamos(RandomizedEnemy):
    display_name = "Beamos"

class Biri(RandomizedEnemy):
    display_name = "Biri"

class BubbleBlue(RandomizedEnemy):
    display_name = "Bubble (Blue)"

class BubbleFire(RandomizedEnemy):
    display_name = "Bubble (Fire)"

class BubbleGreen(RandomizedEnemy):
    display_name = "Bubble (Green)"

class BubbleWhite(RandomizedEnemy):
    display_name = "Bubble (White)"

class DarkLink(RandomizedEnemy):
    display_name = "Dark Link"

class DeadHandsHand(RandomizedEnemy):
    display_name = "Dead Hand's Hand"

class DekuBabaSmall(RandomizedEnemy):
    display_name = "Deku Baba (Small)"

class DekuBabaBig(RandomizedEnemy):
    display_name = "Deku Baba (Big)"

class DekuBabaWithered(RandomizedEnemy):
    display_name = "Deku Baba (Withered)"

class DekuScrub(RandomizedEnemy):
    display_name = "Deku Scrub"

class Dinolfos(RandomizedEnemy):
    display_name = "Dinolfos"

class DodongoNormal(RandomizedEnemy):
    display_name = "Dodongo (Normal)"

class DodongoBaby(RandomizedEnemy):
    display_name = "Dodongo (Baby)"

class FlareDancer(RandomizedEnemy):
    display_name = "Flare Dancer"

class Floormaster(RandomizedEnemy):
    display_name = "Floormaster"

class FlyingFloorTile(RandomizedEnemy):
    display_name = "Flying Floor Tile"

class FlyingPot(RandomizedEnemy):
    display_name = "Flying Pot"

class Freezard(RandomizedEnemy):
    display_name = "Freezard"

class GerudoFighter(RandomizedEnemy):
    display_name = "Gerudo Fighter"

class Gibdo(RandomizedEnemy):
    display_name = "Gibdo"

class GohmaLarva(RandomizedEnemy):
    display_name = "Gohma Larva"

class Guay(RandomizedEnemy):
    display_name = "Guay"

class IronKnuckle(RandomizedEnemy):
    display_name = "Iron Knuckle"

class KeeseNormal(RandomizedEnemy):
    display_name = "Keese (Normal)"

class KeeseFire(RandomizedEnemy):
    display_name = "Keese (Fire)"

class KeeseIce(RandomizedEnemy):
    display_name = "Keese (Ice)"

class Leever(RandomizedEnemy):
    display_name = "Leever"

class LikeLike(RandomizedEnemy):
    display_name = "Like Like"

class Lizalfos(RandomizedEnemy):
    display_name = "Lizalfos"

class MadScrub(RandomizedEnemy):
    display_name = "Mad Scrub"

class MoblinClub(RandomizedEnemy):
    display_name = "Moblin (Club)"

class MoblinSpear(RandomizedEnemy):
    display_name = "Moblin (Spear)"

class Octorok(RandomizedEnemy):
    display_name = "Octorok"

class Peahat(RandomizedEnemy):
    display_name = "Peahat"

class PeahatLarva(RandomizedEnemy):
    display_name = "Peahat Larva"

class Poe(RandomizedEnemy):
    display_name = "Poe"

class Redead(RandomizedEnemy):
    display_name = "Redead"

class Shabom(RandomizedEnemy):
    display_name = "Shabom"

class ShellBlade(RandomizedEnemy):
    display_name = "Shell Blade"

class Skulltula(RandomizedEnemy):
    display_name = "Skulltula"

class Skullwalltula(RandomizedEnemy):
    display_name = "Skullwalltula"

class SkullKid(RandomizedEnemy):
    display_name = "Skull Kid"

class Spike(RandomizedEnemy):
    display_name = "Spike"

class Stalchild(RandomizedEnemy):
    display_name = "Stalchild"

class Stalfos(RandomizedEnemy):
    display_name = "Stalfos"

class StingerFloor(RandomizedEnemy):
    display_name = "Stinger (Floor)"

class StringerWater(RandomizedEnemy):
    display_name = "Stringer (Water)"

class Tailpasaran(RandomizedEnemy):
    display_name = "Tailpasaran"

class TektiteBlue(RandomizedEnemy):
    display_name = "Tektite (Blue)"

class TektiteRed(RandomizedEnemy):
    display_name = "Tektite (Red)"

class TorchSlug(RandomizedEnemy):
    display_name = "Torch Slug"

class Wallmaster(RandomizedEnemy):
    display_name = "Wallmaster"

class Wolfos(RandomizedEnemy):
    display_name = "Wolfos"

####################
# Shuffle Settings #
####################

class ShuffleDungeonRewards(Choice):
    """
    End of Dungeon:
    Medallions and Spiritual Stones will be given as
    rewards for beating dungeons.
    
    This setting will force Link's Pocket to be a
    Medallion or Spiritual Stone.

    Any Dungeon:
    Medallions and Spiritual Stones can only appear
    inside of dungeons.

    Overworld:
    Medallions and Spiritual Stones can only appear
    outside of dungeons.

    Anywhere:
    Medallions and Spiritual Stones can appear
    anywhere."
    """
    display_name = "Shuffle Dungeon Rewards"
    option_end_of_dungeon = 1
    option_any_dungeon = 2
    option_overworld = 3
    option_anywhere = 4
    default = option_end_of_dungeon

class LinksPocket(Choice):
    """
    Dungeon Reward:
    Link will start with a Dungeon Reward in his
    inventory.

    Advancement:
    Link will receive a random advancement item at the
    beginning of the playthrough.

    Anything:
    Link will receive a random item from the item pool
    at the beginning of the playthrough.

    Nothing:
    Link will start with a very useful green rupee.
    """
    display_name = "Link's Pocket"
    option_dungeon_reward = 1
    option_advancement = 2
    option_anything = 3
    option_nothing = 4
    default = option_dungeon_reward

class ShuffleSongs(Choice):
    """
    Song Locations:
    Songs will only appear at locations that normally
    teach songs.

    Dungeon Rewards:
    Songs appear at the end of dungeons. For major
    dungeons, they will be at the boss heart container
    location. The remaining 4 songs are placed at:
    - Zelda's Lullaby Location
    - Ice Cavern's Serenade of Water Location
    - Bottom of the Well's Lens of Truth Location
    - Gerudo Training Ground's Ice Arrow Location

    Anywhere:
    Songs can appear in any location.
    """
    display_name = "Shuffle Songs"
    option_song_locations = 1
    option_dungeon_rewards = 2
    option_anywhere = 3
    default = option_song_locations

class Shopsanity(NamedRange):
    """
    Off:
    All shop items will be the same as vanilla.

    0-4:
    Vanilla shop items will be shuffled among
    different shops, and each shop will contain
    X non-vanilla shop items.

    Random Per Shop:
    Vanilla shop items will be shuffled among
    different shops, and each shop will contain
    a random number of non-vanilla shop items.
    """
    display_name = "Shopsanity"
    range_start = 0
    range_end = 4
    special_range_names = {
        "off": -1,
        "random per shop": -2,
    }
    default = -1

class ShopsanityPrices(Choice):
    """
    Random Price:
    Prices of shuffled shop items are random
    varying between 0 and 295 rupees.

    Affordable:
    Prices of shuffled shop items are 10 rupees.
    
    Child:
    Prices of shuffled shop items are random
    varying between 0 and 99 rupees.

    Adult:
    Prices of shuffled shop items are random
    varying between 0 and 200 rupees.

    Giant:
    Prices of shuffled shop items are random
    varying between 0 and 500 rupees.

    Tycoon:
    Prices of shuffled shop items are random
    varying between 0 and 999 rupees.
    """
    display_name = "Shopsanity Prices"
    option_random_price = 0
    option_affordable = 1
    option_child = 2
    option_adult = 3
    option_giant = 4
    option_tycoon = 5
    default = option_random_price

class Tokensanity(Choice):
    """
    Off:
    GS locations will not be shuffled.

    Dungeon:
    This only shuffles the GS locations that are
    within dungeons, increasing the value of most
    dungeons and making internal dungeon exploration
    more diverse.

    Overworld:
    This only shuffles the GS locations that are
    outside of dungeons.

    All Tokens:
    Effectively adds 100 new locations for items to
    appear.
    """
    display_name = "Tokensanity"
    option_off = 0
    option_dungeon = 1
    option_overworld = 2
    option_all_tokens = 3
    default = option_off

class ScrubShuffle(Choice):
    """
    Off:
    Only the 3 Scrubs that give one-time items in the
    vanilla game (PoH, Deku Nut capacity, and Deku
    Stick capacity) will have random items.

    Affordable:
    All Scrub prices will be reduced to 10 rupees each.

    Expensive:
    All Scrub prices will be their vanilla prices.
    This will require spending over 1000 rupees on
    Scrubs.

    Random Prices:
    All Scrub prices will be between 0-95 rupees. This
    will on average be very, very expensive overall.
    """
    display_name = "Scrub Shuffle"
    option_off = 0
    option_affordable = 1
    option_expensive = 2
    option_random_prices = 3
    default = option_off

class ShuffleCows(Toggle):
    """
    Enabling this will let cows give you items upon
    performing Epona's song in front of them. There
    are 9 cows, and an extra in MQ Jabu.
    """
    display_name = "Shuffle Cows"
    default = False

class ShuffleKokiriSword(Toggle):
    """
    Enabling this shuffles the Kokiri Sword into the
    item pool.
    
    This will require extensive use of sticks until
    the sword is found.
    """
    display_name = "Shuffle Kokiri Sword"
    default = False

class ShuffleMasterSword(Toggle):
    """
    Enabling this shuffles the Master Sword into the
    item pool.
    
    Adult Link will start with a second free item
    instead of the Master Sword. If you haven't found
    the Master Sword before facing Ganon, you won't
    receive it during the fight.
    """
    display_name = "Shuffle Master Sword"
    default = False

class ShuffleOcarinas(Toggle):
    """
    Enabling this shuffles the Fairy Ocarina and the
    Ocarina of Time into the item pool.
    
    This will require finding an Ocarina before being
    able to play songs.
    """
    display_name = "Shuffle Ocarinas"
    default = False

class ShuffleWeirdEgg(Toggle):
    """
    Enabling this shuffles the Weird Egg from Malon
    into the item pool.
    This will require finding the Weird Egg to talk to
    Zelda in Hyrule Castle, which in turn locks
    rewards from Impa, Saria, Malon, and Talon.
    """
    display_name = "Shuffle Weird Egg"
    default = False

class ShuffleZeldasLetter(Toggle):
    """
    Enabling this shuffles Zelda's Letter into the
    item pool.
    This will require finding the letter to open the
    Happy Mask Shop and the gate in Kakariko if it is
    set to closed.
    """
    display_name = "Shuffle Zelda's Letter"
    default = False

class ShuffleGerudoToken(Toggle):
    """
    Enabling this shuffles the Gerudo Token into the
    item pool.
    
    The Gerudo Token is required to enter the Gerudo
    Training Ground.
    """
    display_name = "Shuffle Gerudo Token"
    default = False

class ShuffleMagicBeans(Toggle):
    """
    Enabling this adds a pack of 10 beans to the item
    pool and changes the Magic Bean Salesman to sell a
    random item at a price of 60 rupees.
    """
    display_name = "Shuffle Magic Beans"
    default = False

class ShuffleMerchants(Choice):
    """
    Off:
    Enabling this changes Medigoron, Granny and the
    Carpet Salesman to sell a random item once at a
    high price (100 for Granny, 200 for the others).
    A Giant's Knife and a pack of Bombchus will be
    added to the item pool, and one of the bottles
    will contain a Blue Potion.

    On:
    These hints will make the merchants tell you
    which item they're selling.
    
    The Hint Clarity setting will affect how they
    refer to the item.
    """
    display_name = "Shuffle Merchants"
    option_off = 0
    option_on_no_hints = 1
    option_on_with_hints = 2
    default = option_off

class ShuffleAdultTrade(Toggle):
    """
    Enabling this adds all of the adult trade quest
    items to the pool, each of which can be traded
    for a unique reward. You will be able to choose
    which of your owned adult trade items is visible
    in the inventory by selecting the item and using
    the L and R buttons. If disabled, only the Claim
    Check will be found in the pool.
    """
    display_name = "Shuffle Adult Trade"
    default = False

class ShuffleChestMinigame(Choice):
    """
    The 5 key chests in the Treasure Chest Shop will
    be randomized, and the 6 keys will be added to the
    pool. The rupee chests will be replaced by traps.
    Also, the shop owner is on vacation, so he can't
    close any chests or doors once you leave.
    
    If you choose the \"pack\" option, you will get
    all the keys at once, in a single item.
    """
    display_name = "Shuffle Chest Minigame"
    option_off = 0
    option_on_seperate = 1
    option_on_pack = 2
    default = option_off

    @classmethod
    def get_option_name(cls, value: T) -> str: # type: ignore
        if value == cls.option_on_seperate:
            return "On (Seperate)"
        elif value == cls.option_on_pack:
            return "On (Pack)"
        return super().get_option_name(value) # type: ignore

class ShuffleFrogRupees(Toggle):
    """
    Enabling this adds 5 Purple Rupees to the item\n
    pool and shuffles the rewards from playing Zelda's
    Lullaby, Epona's Song, Saria's Song, Sun's Song,
    and Song of Time to the frogs in Zora's River.
    """
    display_name = "Shuffle Frog Rupees"
    default = False

class ShuffleEnemySouls(Choice):
    """
    Enemies will be invincible until you find their
    \"soul\".
    Each enemy type will have a soul added into the
    item pool.
    
    You can exclude some enemies by adding their
    souls in the Starting Inventory.

    WARNING: Incompatible with Master Quest Logic.
    """
    display_name = "Shuffle Enemy Souls"
    option_off = 0
    option_all_enemies = 1
    option_bosses_only = 2
    default = option_off

class ShuffleOcarinaButtons(Toggle):
    """
    Enabling this locks all Ocarina inputs, and adds
    5 new items to find that each unlock one of the 5
    Ocarina notes.
    
    They can also be added to the Starting Inventory.
    """
    display_name = "Shuffle Ocarina Buttons"
    default = False

class ShuffleStandingRupees(Toggle):
    """
    Shuffles all freestanding visible rupees
    that are placed in the world without player
    intervention. So it does include Rupees that are
    placed in other objects like boulders, but it
    doesn't include Wonder Items or Rupees that spawn"
    from the Goron City spinning pot or the pots in
    Shadow Temple.
    """
    display_name = "Shuffle Standing Rupees"
    default = False

class ShuffleRecoveryHearts(Toggle):
    """
    Shuffles all freestanding visible recovery hearts
    that are placed in the world without player
    intervention.
    """
    display_name = "Shuffle Recovery Hearts"
    default = False

class ShuffleBigPoes(Toggle):
    """
    The 10 Big Poes in Hyrule Field will drop random
    items.
    Their bottled spirits will be added to the item
    pool, and won't require a bottle to be obtained.
    Speak to the Poe Collector to get his reward after
    finding the required amount.
    """
    display_name = "Shuffle Big Poes"
    default = False

#########################
# Shuffle Dungeon Items #
#########################

class ShuffleMapsAndCompasses(Choice):
    """
    Start With:
    Maps and Compasses are given to you from the
    start. This will add a small amount of money and
    refill items to the pool.

    Vanilla:
    Maps and Compasses will appear in their vanilla
    locations.

    Own Dungeon:
    Maps and Compasses can only appear in their
    respective dungeon.

    Any Dungeon:
    Maps and Compasses can only appear in a dungeon,
    but not necessarily the dungeon they are for.

    Overworld:
    Maps and Compasses can only appear outside of
    dungeons.

    Anywhere:
    Maps and Compasses can appear anywhere in the
    world.
    """
    display_name = "Maps/Compasses"
    option_start_with = 1
    option_vanilla = 2
    option_own_dungeon = 3
    option_any_dungeon = 4
    option_overworld = 5
    option_anywhere = 6
    default = option_own_dungeon

class ShuffleSmallKeys(Choice):
    """
    Start With:
    Small Keys are given to you from the start so you
    won't have to worry about locked doors. An easier
    mode.

    Vanilla:
    Small Keys will appear in their vanilla locations.
    You start with 3 keys in Spirit Temple MQ because
    the vanilla key layout is not beatable in logic.

    Own Dungeon:
    Small Keys can only appear in their respective
    dungeon. If Fire Temple is not a Master Quest
    dungeon, the door to the Boss Key chest will be
    unlocked.

    Any Dungeon:
    Small Keys can only appear inside of any dungeon,
    but won't necessarily be in the dungeon that the
    key is for. A difficult mode since it is more
    likely to need to enter a dungeon multiple times.

    Overworld:
    Small Keys can only appear outside of dungeons.
    You may need to enter a dungeon multiple times to
    gain items to access the overworld locations with
    the keys required to finish a dungeon.

    Anywhere:
    Small Keys can appear anywhere in the world. A
    difficult mode since it is more likely to need to
    enter a dungeon multiple times.
    """
    display_name = "Small Keys"
    option_start_with = 1
    option_vanilla = 2
    option_own_dungeon = 3
    option_any_dungeon = 4
    option_overworld = 5
    option_anywhere = 6
    default = option_own_dungeon

class ShuffleGerudoFortressKeys(Choice):
    """
    Vanilla:
    Gerudo Fortress Keys will appear in their vanilla
    location, dropping from fighting Gerudo guards
    that attack when trying to free the jailed
    carpenters.

    Any Dungeon:
    Gerudo Fortress Keys can only appear inside of
    dungeons.

    Overworld:
    Gerudo Fortress Keys can only appear outside of
    dungeons.

    Anywhere:
    Gerudo Fortress Keys can appear anywhere in the
    world.
    """
    display_name = "Gerudo Fortress Keys"
    option_vanilla = 1
    option_any_dungeon = 2
    option_overworld = 3
    option_anywhere = 4
    default = option_vanilla

class ShuffleBossKeys(Choice):
    """
    Start With:
    Boss Keys are given to you from the start so you
    won't have to worry about boss doors. An easier
    mode.

    Vanilla:
    Boss Keys will appear in their vanilla locations.

    Own Dungeon:
    Boss Keys can only appear in their respective
    dungeon.

    Any Dungeon:
    Boss Keys can only appear inside of any dungeon,
    but won't necessarily be in the dungeon that the
    key is for. A difficult mode since it is more
    likely to need to enter a dungeon multiple times.

    Overworld:
    Boss Keys can only appear outside of dungeons.
    You may need to enter a dungeon without the boss
    key to get items required to find the key in the
    overworld.

    Anywhere:
    Boss Keys can appear anywhere in the world. A
    difficult mode since it is more likely to need to
    enter a dungeon multiple times.
    """
    display_name = "Boss Keys"
    option_start_with = 1
    option_vanilla = 2
    option_own_dungeon = 3
    option_any_dungeon = 4
    option_overworld = 5
    option_anywhere = 6
    default = option_own_dungeon

class ShuffleGanonsBossKey(Choice):
    """
    Start With:
    Ganon's Castle Boss Key is given to you from the
    start and you don't have to worry about finding it

    Vanilla:
    Ganon's Castle Boss Key will appear in the vanilla
    location.

    Own Dungeon:
    Ganon's Castle Boss Key can only appear inside
    Ganon's Castle.

    Any Dungeon:
    Ganon's Castle Boss Key can only appear inside of
    a dungeon, but not necessarily Ganon's Castle.

    Overworld:
    Ganon's Castle Boss Key can only appear outside of
    dungeons.

    Anywhere:
    Ganon's Castle Boss Key can appear anywhere in the
    world.

    Light Arrow Cutscene:
    These settings put the boss key on the Light Arrow
    Cutscene location, from Zelda in Temple of Time as
    adult, with differing requirements.
    """
    display_name = "Ganon's Boss Key"
    option_start_with = 1
    option_vanilla = 2
    option_own_dungeon = 3
    option_any_dungeon = 4
    option_overworld = 5
    option_anywhere = 6
    option_LACS_vanilla = 7
    option_LACS_medallions = 8
    option_LACS_stones = 9
    option_LACS_rewards = 10
    option_LACS_dungeons = 11
    option_LACS_tokens = 12
    option_LACS_hearts = 13
    default = option_own_dungeon

class LACSMedallionCount(Range):
    """
    Set the number of Medallions required to trigger
    the Light Arrow Cutscene.
    """
    display_name = "LACS Medallion Count"
    range_start = 0
    range_end = 6
    default = 6

class LACSStoneCount(Range):
    """
    Set the number of Spiritual Stones required to
    trigger the Light Arrow Cutscene.
    """
    display_name = "LACS Stone Count"
    range_start = 0
    range_end = 3
    default = 3

class LACSRewardCount(Range):
    """
    Set the number of Dungeon Rewards (Spiritual
    Stones and Medallions) required to trigger the
    Light Arrow Cutscene.
    """
    display_name = "LACS Reward Count"
    range_start = 0
    range_end = 9
    default = 9

class LACSDungeonCount(Range):
    """
    Set the number of completed dungeons required to
    trigger the Light Arrow Cutscene.
    
    Dungeons are considered complete when Link steps
    into the blue warp at the end of them
    """
    display_name = "LACS Dungeon Count"
    range_start = 0
    range_end = 8
    default = 8

class LACSTokenCount(Range):
    """
    Set the number of Gold Skulltula Tokens required
    to trigger the Light Arrow Cutscene.
    """
    display_name = "LACS Token Count"
    range_start = 0
    range_end = 100
    default = 100

class LACSHeartCount(Range):
    """
    Set the number of Hearts required to trigger the
    Light Arrow Cutscene.
    """
    display_name = "LACS Heart Count"
    range_start = 0
    range_end = 20
    default = 20

class KeyRings(OptionSet):
    """
    Selected key ring dungeons will have all of their
    keys found at once in a ring rather than
    individually.

    For example, instead of shuffling 5 Forest Temple
    small keys into the pool, you will find a single
    key ring which will give you all 5 keys at once.
    """
    display_name = "Key Rings"
    valid_keys = {
        "Gerudo Fortress",
        "Forest Temple",
        "Fire Temple",
        "Water Temple",
        "Spirit Temple",
        "Shadow Temple",
        "Bottom of the Well",
        "GTG",
        "Ganon's Castle",
    }
    default = {}

######################
# Timesaver Settings #
######################

class SkipChildStealth(Toggle):
    """
    The crawlspace into Hyrule Castle goes straight to
    Zelda, skipping the guards.
    """
    display_name = "Skip Child Stealth"
    default = True

class SkipTowerEscape(Toggle):
    """
    The tower escape sequence between Ganondorf and
    Ganon will be skipped.
    """
    display_name = "Skip Tower Escape"
    default = True

class SkipEponaRace(Toggle):
    """
    Epona can be summoned with Epona's Song without
    needing to race Ingo.
    """
    display_name = "Skip Epona Race"
    default = False

class SkipMinigamesRepetitions(Toggle):
    """
    Completing the second objective in the Dampe Race
    and Gerudo Archery on the first attempt will give
    both rewards at once for that minigame.
    """
    display_name = "Minigames Repetitions"
    default = False

class FreeScarecrow(Toggle):
    """
    Pulling out the Ocarina near a spot at which
    Pierre can spawn will do so, without needing
    the song.
    """
    display_name = "Free Scarecrow"
    default = False

class SkipFourPoesCutscene(Toggle):
    """
    The cutscene with the 4 poes in Forest Temple will
    be skipped. If the cutscene is not skipped, it can
    be exploited to reach the basement early.
    """
    display_name = "Four Poes Cutscene"
    default = True

class LakeHyliaOwl(Toggle):
    """
    The owl flight cutscene in Lake Hylia will be
    skipped. This cutscene lets you see what item
    is on top of the laboratory roof.
    """
    display_name = "Lake Hylia Owl"
    default = True

class BigPoeTargetCount(Range):
    """
    The Poe Collector will give a reward for turning
    in the chosen number of Big Poes.
    """
    display_name = "Big Poe Target Count"
    range_start = 1
    range_end = 10
    default = 1

class CuccosToReturn(Range):
    """
    The cucco lady will give a reward for returning
    this many of her cuccos to the pen.
    """
    display_name = "Cuccos to Return"
    range_start = 0
    range_end = 7
    default = 0

class KingZoraSpeed(NamedRange):
    """
    Set the exact number of shuffles King Zora will
    take to move out of the way.
    """
    display_name = "King Zora Speed"
    range_start = 1
    range_end = 128
    special_range_names = {
        "fast": 1,
        "vanilla": 26,
    }
    default = 1

class CompleteMaskQuest(Toggle):
    """
    Once the happy mask shop is opened, all masks
    will be available to be borrowed.
    """
    display_name = "Complete Mask Quest"
    default = False

#################
# Logic Options #
#################

class Logic(Choice):
    """
    Glitchless:
    No glitches are required, but may require some
    minor tricks. Add minor tricks to consider for
    logic in Logical Tricks.

    Glitched:
    The glitches you enable at the set difficulty
    or below may be required.
    
    WIP feature. Allows glitch logic for the entire
    overworld and the following vanilla dungeons:
    Deku Tree, Dodongo's Cavern, Jabu Jabu, and
    Forest, Water, and Fire Temple.

    No Logic:
    Maximize randomization, All locations are
    considered available. MAY BE IMPOSSIBLE TO BEAT.

    Vanilla:
    Go play the base randomizer if you want this
    option. If I implement it here you will not
    interact with archipelago at all ¯\\_(ツ)_/¯
    """
    display_name = "Logic"
    option_glitchless = 1
    option_glitched = 2
    option_no_logic = 3
    default = option_glitchless

class NightSkultullasExpectSun(Toggle):
    """
    GS Tokens that can only be obtained during the
    night expect you to have Sun's Song to collect
    them. This prevents needing to wait until night
    for some locations.
    """
    display_name = "Night GSs Expect Sun's"
    default = False

class LogicalTricks(OptionSet):
    """
    See <insert link> for a list of valid options
    and their descriptions.
    """
    display_name = "Logical Tricks"
    valid_keys = {
        "Grotto Access w/o Shard of Agony",
        "Go Through Visible One-Way Collisions",
        "Fewer Tunic Requirements",
        "LW Adult Tree GS w/o Magic Beans",
        "LH Lab Dive w/o Gold Skale",
        "LH Lab Wall GS w/ Jump Slash",
        "GY Crate PoH w/ Boomerang",
        "GY Second Dampe Race as Child",
        "GV Hammer Chest w/o Hammer",
        "GF Through Kitchen w/ Nothing",
        "GF Top Floor as Child",
        "Haunted Wasteland w/o Lens of Truth",
        "Haunted Wasteland in Reverse",
        "Colossus Hill GS w/ Hookshot",
        "Outside GaC GS w/ Jump Slash",
        "Kak Roof Guy w/o Hookshot",
        "Windmill PoH w/ Hookshot",
        "DMT Wall Chest w/ Strength",
        "DMT Soil GS w/o Opening DC",
        "DMT Summit w/ Hover Boots",
        "DMC Scarecrow Rupee circle w/ Nothing",
        "GoC Adult Goron w/ Din's Fire",
        "GoC Maze Left Chest w/ Hover Boots",
        "GoC Goron Vase PoH w/ Bombchu",
        "GoC Goron Vase PoH w/ Strength",
        "GoC Child Goron w/ Strength",
        "DMC Bean PoH w/ Hover Boots",
        "DMC Deliver Eyedrops w/ Bolero of Fire",
        "ZR Lower PoH w/ Nothing",
        "ZR Upper PoH w/ Nothing",
        "ZR Under Waterfall rupees w/o Iron Boots",
        "ZF Great Fairy w/o Explosives",
        "DT B1 Web w/ Bow",
        "DT B1 Navigation w/o Slingshot",
        "DT B1 Vines GS w/ Jump Slash",
        "DC Staircase w/ Bow",
        "DC Spike Trap Room w/o Hover Boots",
        "DC Eye Switches w/o Slingshot",
        "DC Scarecrow GS w/ Armos Statue",
        "JJB Deku Scrub as Adult",
        "FoT East Scarecrow w/ Hover Boots",
        "FoT East Yard GS w/ Boomerang",
        "FiT Boss Door w/o Hover Boots",
        "FiT Climb Block w/o Strength",
        "FiT East Tower w/o Scarecrow",
        "FiT Firewall Maze w/ Nothing",
        "FiT SoT Room GS w/o SoT",
        "WaT Torch Longshot Shortcut",
        "WaT Boss Ledge w/ Bombs",
        "WaT Bow Target w/o Longshot/Hover",
        "WaT Center Room GS w/ Farore's Wind",
        "WaT Cracked Wall w/ Nothing",
        "WaT Cracked Wall w/ Hover Boots",
        "WaT B1 North Area w/ Hover Boots",
        "WaT Boss Key Room w/o Iron Boots",
        "WaT Boss Key Rooms w/ Precise Jump",
        "WaT Whirlpool Up w/o Iron Boots",
        "WaT Whirlpool w/o Iron Boots",
        "WaT River GS w/o Iron Boots",
        "WaT Waterfall GS w/ Hookshot",
        "SpT Ceiling Switch w/ Bombs",
        "SpT Child Bridge w/ Bombchu",
        "SpT Shifting Wall w/ Nothing",
        "SpT Main Room GS w/ Boomerang",
        "SpT Map Chest w/ Bow",
        "SpT Sun Bloock Room w/ Bow",
        "ShT Stone Umbrella w/ Hover Boots",
        "ShT Skull Vase Key w/ Bombchu",
        "ShT River Statue w/ Bombchu",
        "ShT Bongo w/o Projectiles",
        "BotW Deadhand w/o Sword",
        "GTG West Silver Rupee w/o Hookshot",
        "GTG Invisible Wall w/ Hover Boots",
        "SpT Navigate w/o Lens of Truth",
        "ShT Early Rooms w/o Lens of Truth",
        "ShT Later Rooms w/o Lens of Truth",
        "BotW Navigate w/o Lens of Truth",
        "GTG Navigate w/o Lens of Truth",
        "GaC Navigate w/o Lens of Truth",
        "JJB MQ Navigate w/o Lens of Truth",
        "SpT MQ Navigate w/o Lens of Truth",
        "ShT MQ Early Rooms w/o Lens of Truth",
        "ShT MQ Later Rooms w/o Lens of Truth",
        "BotW MQ Navigate w/o Lens of Truth",
        "GTG MQ Navigate w/o Lens of Truth",
        "GaC MQ Navigate w/o Lens of Truth",
        "Spirit Trial w/o Hookshot",
        "Open chests through flame circles",
    }

############
# Glitches #
############

class Glitch(NamedRange):
    range_start = 0
    range_end = 5
    special_range_names = {
        "disabled": 0,
        "novice": 1,
        "intermediate": 2,
        "advanced": 3,
        "expert": 4,
        "hero": 5,
    }
    default = 0

class RestrictedItems(Glitch):
    """
    Swapping an item that can normally be used in an
    area with one that would be dimmed will let you
    use that item for 1 frame after closing your
    inventory. This can be useful on its own or in
    combination with other glitches.

    Novice:
    You may be required to use restricted items.
    """
    display_name = "Restricted Items"

class SuperStab(Glitch):
    """
    Forcing sticks to unequip during a crouch stab by
    breaking it and moving them in your inventory has
    the effect of hitting all spherical collision.

    Novice:
    You may be expected to hit switches or kill gold
    skulltulas with a super stab.
    """
    display_name = "Super Stab"

class InfiniteSwordGlitch(Glitch):
    """
    Shortened to ISG, allows Link's melee weapon to
    be in a constant swinging state. Simply touching
    objects with this causes them to get hit.    
    Putting away the weapon while ISG is on hits
    any object with a spherical hitbox,        
    such as small skulltulas. It is initiated by
    interrupting a crouch stab.

    Novice:
    ISG may be required to kill certain enemies,
    or to Bomb Hover when enabled.

    Intermediate:
    You may be required to use a bomb to activate ISG.

    Advanced:
    You may be required to use a bomb to activate ISG
    repeatedly or while under attack.
    """
    display_name = "Infinite Sword Glitch"

class BombHover(Glitch):
    """
    Hovering allows Link to consecutively backflip
    in the air without falling. By shielding 
    damage with ISG on, Link will stay in midair.
    While bombs aren't always required, this option
    will always expect them to be used.        
    
    Requires ISG to be enabled.

    Novice:
    Only bombchus are required for hovering.

    Intermediate:
    Some hovers may require that you start from flat
    terrain, which requires somewhat precise timing.

    Advanced:
    Usage of regular bombs will now also be expected,
    which may require consecutive precise timings.
    """
    display_name = "Bomb Hover"

class OcarinaItemsBomb(Glitch):
    """
    Allowing a bomb to explode in Link's hands while
    moving and then attempting to pull out a cutscene
    item on a specific frame will cause Link to play
    an invisible ocarina instead.
    This will only work if bombs are not dimmed on the
    frame you use the cutscene item.

    Novice:
    You may be expected to use ocarina items with a
    bomb to play warp songs.

    Intermediate:
    You may be expected to use ocarina items with a
    bomb to play the ocarina where Link's position
    matters.

    Advanced:
    You may be expected to use restricted items to use
    the cutscene item or make the bombs usable on
    the correct frame.

    Expert:
    You may be expected to use restricted items to
    preform ocarina items where Link's position isn't
    particularly lenient.
    """
    display_name = "Ocarina Items (Bomb)"

class HoverBoost(Glitch):
    """
    Equipping hover boots when Link takes damage will
    cause him to keep the high knockback speed and
    lets him traverse large gaps.
    If performed at the edge of a platform Link will
    instead perform a mega jump which has less range
    but more height than a hover boost.

    Novice:
    Hover boosts that do not need maximum speed
    may be required.

    Intermediate:
    Hover boosts that do need maximum speed may be
    required.

    Advanced:
    Hover boosts that use more complex movement during
    the hover may be required.
    """
    display_name = "Hover Boost"

class ExtendedSuperSlide(Glitch):
    """
    Holding the circle pad just outside the dead zone
    will cause Link to turn on the spot which locks
    his speed. This can be used to preserve high
    speeds indefinitely.

    Novice:
    Forward extended super slides (FESSes) where Link
    is damaged by an explosion may be required.

    Intermediate:
    Hammer exteneded super slides where recoil from
    a hammer crouch stab may be required.

    Advanced:
    Hyper Extended Super Slides (HESSes) and
    damageless FESSes where Link rolls into a bomb may
    be required.

    Expert:
    HESSes with more precise movement may be required.
    """
    display_name = "Extended Super Slide"

class Megaflip(Glitch):
    """
    A backflip or sidehop with high speed from an
    attack hitting your shield during i-frames. This
    is normally achieved by rolling into an explosion.
    Equipping hover boots to preserve the high speed
    when landing is known as a hoverflip.

    Novice:
    You may be expected to preform megaflips on flat
    ground with bombs.

    Intermediate:
    You may be expected to preform megaflips in small
    areas, distance megaflips, or hoverflips with a
    bomb.

    Advanced:
    You may be expected to preform hoverflips with
    difficult midair movement, or distance megaflips
    under time pressure with a bomb.

    Additionally, you may be expected to preform
    novice megaflips with a bombchu.

    Expert:
    You may be expected to preform intermediate
    megaflips with a bombchu.

    Hero:
    You may be expected to preform any megaflip with a
    bombchu.
    """
    display_name = "Megaflip"

class ASlide(Glitch):
    """
    An A-slide is performed the same as a megaflip
    except without pressing the A button at the end.
    This causes child Link's collision to glitch below
    the ground and lets him bypass certain actors.

    Novice:
    You may be expected to preform A-slides to pass
    actors you can't press A to interact with.

    Intermediate:
    You may be expected to preform A-slides quickly or
    around actors that can be interacted with.

    Advanced:
    You may be expected to preform novice A-slides
    with a bombchu.

    Expert:
    You may be expected to preform intermediate A-slides
    with a bombchu.
    """
    display_name = "A-Slide"

class HammerSlide(Glitch):
    """
    Equipping hover boots after a hammer crouch stab
    against a wall preserves the recoil speed which
    allows Link to cross larger gaps than usual.

    Novice:
    Simple hammer slides may be required.

    Intermediate:
    Hammer slides which require good movement and high
    speed may be required.
    """
    display_name = "Hammer Slide"

class LedgeCancel(Glitch):
    """
    Climbing a short ledge and shielding damage will
    prevent the ledge climbing state from ending.
    This state allows Link to walk through some actors
    such as boulders and NPCs.

    Novice:
    You may be expected to preform ledge cancels using
    bombs as a damage source.

    Intermediate:
    You may be expected to preform ledge cancels in
    places with little room.

    Advanced:
    You may be expected to preform ledge cancels using
    bombchus as a damage source.
    """
    display_name = "Ledge Cancel"

class ActionSwap(Glitch):
    """
    Action swap allows Link to switch between 2 held
    items without the put away/equip animations.
    This can be exploited to produce various effects.

    Novice:
    You may be expected to use shallow water to set up
    action swap.

    Advanced:
    You may be expected to use bombchus to set up
    action swap.
    """
    display_name = "Action Swap"

class QuickPutAway(Glitch):
    """
    Certain events can cancel putting away an item
    which later lets Link put it away without an 
    animation. This can be used with sticks to access
    a glitched damage value with the properties of
    hammer and fire arrows, or with a bottle to store
    a cutscene for ocarina items.

    Novice:
    You may be expected to get QPA using the boots
    animation to delay putting away the item and a
    bomb.

    Intermediate:
    You may be expected to get QPA using only a bomb.

    Advanced:
    You may be expected to get QPA using a ledge grab
    to interrupt putting away the item.

    Expert:
    You may be expected to get QPA from enemy attacks.
    """
    display_name = "Quick Put Away"

class HookshotClip(Glitch):
    """
    Hookshot Clipping allows Link to hookshot through
    certain walls, which is useful if a valid
    target is on the other side.

    Novice:
    Basic hookshot clipping may be required.

    Intermediate:
    Hookshot clips with precise andles and poor
    visibility may be required.
    """
    display_name = "Hookshot Clip"

class HookshotJumpBonk(Glitch):
    """
    A Hookshot Jump is an umbrella term for techniques
    that launch Link into the sky using the Hookshot
    in various ways, sometimes together with
    other items. The bonk method only requires the
    Hookshot itself.

    Novice:
    Simple hookshot jumps against large flat walls of
    hookshottable surfaces may be required.

    Intermediate:
    Less lenient hookshot jumps may be required.

    Advanced:
    Hookshot jumps with precise midair movement may be
    required.
    """
    display_name = "Hookshot Jump (Bonk)"

class HookshotJumpBoots(Glitch):
    """
    This Hookshot Jump technique is one of the easier
    ones, and require any pair of boots.

    Novice:
    Only relatively short Hookshot Jumps with boots
    may be required.

    Intermediate:
    Higher Hookshot Jumps with boots, where you look
    further up or downwards may be required.

    Advanced:
    Hookshot Jumps that require a lot of height and
    precise midair movement may be required.
    """
    display_name = "Hookshot Jump (Boots)"

class CutsceneDives(Glitch):
    """
    Water physics won't effect Link if he enters the
    water while a cutscene is playing, allowing him
    to sink to the bottom.

    Novice:
    Attempting to use Farore's Wind (when it's already
    set) with another magic item active prevents the
    water from clearing the FW cutscene until the
    other effect ends.
    You may be expected to use Nayru's Love as the
    other magic effect.

    Intermediate:
    You can catch something in a bottle while standing
    over water using the hover boots to fall through
    the water during teh catch cutscene.

    Advanced:
    You may be expected to use magic arrows to preform
    Farore's Wind cutscene dives.
    """
    display_name = "Cutscene Dives"

class NaviDiveStick(Glitch):
    """
    A Navi dive is a type of cutscene dive achieved by
    falling off a ledge while talking to Navi. While
    the usual method for achieving this is a TSC, it
    is also possible to perform using a jump attack
    with deku sticks.

    Novice:
    You may be expected to enter BotW with a stick
    Navi dive.

    Intermediate:
    You may be expected to use the LH to ZD shortcut
    with a stick Navi dive.

    Advanced:
    You may be expected to use the LW to ZR shortcut
    with a stick Navi dive.
    """
    display_name = "Navi Dive (Stick)"

class TripleSlashClip(Glitch):
    """
    When doing a three-slash-combo with either the
    Kokiri Sword or the Master Sword and put it away,
    Link will be placed back a small distance.    
    If, while slashing, you use the recoil of hitting
    a wall and then put away the sword, Link may clip
    into a wall behind him if angled correctly.

    Novice:
    Basic Triple Slash Clipping may be required.

    Intermediate:
    Some more complex OoB movement may be required.

    Advanced:
    Very precise OoB movement may be required.

    Expert:
    Very precise TSCs may be required.
    """
    display_name = "Triple Slash Clip"

class LedgeClip(Glitch):
    """
    A Ledge Clip allows Link to fall through a floor
    or pass through an object by facing a wall
    and dropping down to the left in various ways.
    These only work as an adult.

    Novice:
    Basic Ledge Clips may be required.
    Some require that you let go of the ledge with
    a specific timing.

    Intermediate:
    Certain harder clips may also be required.

    Advanced:
    Ledge clips with complex OoB movement may be
    required.
    """
    display_name = "Ledge Clip"

class SeamWalk(Glitch):
    """
    Where 2 walls come together they form a seam that
    Link can stand on. It is possible to use these to
    gain height and reach normally inaccessible areas.
    Additionally these seams can reach far above the
    walls that form them, creating invisible seams.

    Novice:
    Short seam walks up visible walls with ISG may be
    required.

    Intermediate:
    Short seam walks up visible walls without ISG or
    longer seam walks with ISG may be required.

    Advanced:
    Longer seam walks without ISG may be required.

    Expert:
    Very precise seam walks may be required.

    Hero:
    Crossing Gerudo Valley as child by walking up a
    wall with the cucco may be required.
    """
    display_name = "Seam Walk"

class MiscGlitches(OptionSet):
    """
    See <insert link> for a list of valid options
    and their descriptions.
    """
    display_name = "Misc Glitches"
    valid_keys = {
        "WWT Kokiri Forest Escape",
        "Enter GV Tent as Child",
        "Sneak Past the GF Guard",
        "Cross the HW w/o Items",
        "Occam's Statue",
        "ZD OoB w/ Jump Slash",
        "Enter Jabu w/o Bottle",
        "Enter Jabu as Adult",
        "Break Walls w/ Blue Fire",
        "Classic Halfie",
        "Modern Halfie",
        "Jabu Switch w/ CS item",
        "Forest Temple BK Skip",
        "Fire Temple Grunz Clip",
    }
    default = {}

#################
# Misc Settings #
#################

class Racing(Toggle):
    """
    Overrides personalization options that could
    affect how fast a seed is beaten.
    """
    display_name = "Racing"
    default = False

class GossipStoneHints(Choice):
    """
    Gossip Stones can be made to give hints about
    where items can be found.
    Different settings can be chosen to decide which
    item is needed to speak to Gossip Stones. Choosing
    to stick with the Mask of Truth will make the
    hints very difficult to obtain.
    Hints for 'on the way of the hero' are locations
    that contain items that are required to beat the
    game.
    """
    display_name = "Gossip Stone Hints"
    option_no_hints = 0
    option_need_nothing = 1
    option_mask_of_truth = 2
    option_shard_of_agony = 3
    default = option_need_nothing

class HintDistribution(Choice):
    """
    Useless:
    Only junk hints.

    Balanced:
    Recommended hint spread.

    Strong:
    More useful hints.

    Very Strong:
    Many powerful hints.
    """
    display_name = "Hint Distribution"
    option_useless = 0
    option_balanced = 1
    option_strong = 2
    option_very_strong = 3
    default = option_balanced

class MiscHints(OptionSet):
    """
    Temple of Time Altar:
    The Temple of Time altar will reveal the locations
    of the Spiritual Stones as child and the
    Medallions as adult, but only if Compasses Show
    Rewards is disabled.
    
    It will also always reveal the requirements for
    the Door of Time as child, and for Ganon Boss Key
    and Rainbow Bridge as adult.

    Ganondorf:
    Talking to Ganondorf in his boss room will tell
    you the location of the Light Arrows and, if it
    was shuffled, the Master Sword.             
                                                
    When trials are on, Sheik will appear to relay
    these hints in Ganon's Castle.

    Dampe's Diary:
    Reading Dampe's diary will reveal the location
    of a single progressive hookshot.

    House of Skulltula:
    Talking to a cursed House of Skulltula resident
    will tell you the reward they will give you for
    removing their curse.

    Fishing Prizes:
    The aquarium at the fishing pond will show what
    reward you can win as your current age.
    """
    display_name = "Miscellaneous Hints"
    valid_keys = {
        "Temple of Time Altar",
        "Ganondorf",
        "Dampe's Diary",
        "House of Skulltula",
        "Fishing Prizes",
    }
    default = valid_keys

class HintClarity(Choice):
    """
    Sets the difficulty of hints.

    Obscure:
    Hints are unique for each thing, but
    the writing may be confusing.
    E.g. Kokiri Sword > a butter knife

    Ambiguous:
    Hints are clearly written, but may
    refer to more than one thing.
    E.g. Kokiri Sword > a sword

    Clear:
    Hints are clearly written and are unique
    for each thing.
    E.g. Kokiri Sword > the Kokiri Sword
    """
    display_name = "Hint Clarity"
    option_obscure = 0
    option_ambiguous = 1
    option_clear = 2
    default = option_obscure

class CompassesShowRewards(Toggle):
    """
    Obtaining a dungeon compass will hint at the
    location of a Spiritual Stone or Medallion.
    
    If rewards are at the end of dungeons, the compass
    for dungeon X will show what reward is at X.
    Otherwise, it will show the area for the reward
    that, in the vanilla game, is located at X.
    
    These hints will appear in the Gear menu on the
    empty reward slots.
    """
    display_name = "Compasses Show Rewards"
    default = False

class CompassesShowWotH(Toggle):
    """
    The in-game menu will reveal whether each
    dungeon is on the Way of the Hero, a barren
    location, or neither, if the compass for that
    dungeon has been collected.
    """
    display_name = "Compasses Show WotH"
    default = True

class MapsShowDungeonModes(Toggle):
    """
    If any Master Quest dungeons will be randomly
    shuffled, the in-game menu will reveal whether
    it is in its Vanilla or Master Quest form, if
    the map for the dungeon has been collected.
    Ganon's Castle and Gerudo Training Grounds are
    always revealed, as they do not have maps.
    """
    display_name = "Maps Show Dungeon Modes"
    default = True

class StartingTime(Choice):
    """
    Change up Link's sleep routine.
    """
    display_name = "Starting Time"
    option_day = 0
    option_night = 1
    default = option_day

class ChestAnimations(Choice):
    """
    Choose if you want the slow animation to play
    if a chest contains a major item.
    """
    display_name = "Chest Animations"
    option_always_fast = 0
    option_match_contents = 1

class ChestAppearanceMod(Choice):
    """
    Vanilla:
    Chests will appear as they do in the base game.

    Texture:
    Chest texture will reflect its contents
    regardless of size.                   
                                          
    Major Items           ->    Gilded Chests
    Boss Keys             ->    Fancy Chests
    Small Keys            ->    Silver Chests
    Hearts                ->    Heart Chests
    Gold Skulltula Tokens ->    Webbed Chests
    Everything else       ->    Wooden Chests

    Size + Texture:
    In addition to the texture change, major items
    and boss keys will be in big chests, and
    everything else will be in small chests.

    Classic CSMC:
    This is the behavior of CSMC in previous   
    versions of the randomizer.                
                                               
    Major Items           ->   Big Wooden Chests
    Lesser Items          ->   Small Wooden Chests
    Boss Keys             ->   Big Fancy Chests
    Small Keys            ->   Small Fancy Chests
    """
    display_name = "Chest Appearance Mod"
    option_vanilla = 0
    option_texture = 1
    option_major_items = 2
    option_size_and_texture = 3
    option_classic_csmc = 4
    default = option_vanilla

    @classmethod
    def get_option_name(cls, value: T) -> str: # type: ignore
        if value == cls.option_size_and_texture:
            return "Size + Texture"
        return super().get_option_name(value) # type: ignore

class ChestAgony(Toggle):
    """
    The Chest Appearance Mod will only apply
    after obtaining the Shard of Agony.
    """
    display_name = "Need Shard of Agony"
    default = False

class KeepExtraShields(Choice):
    """
    Allow keeping more than 1 Deku and Hylian shield
    in the inventory, so if you lose one you can then
    re-equip it immediately. The shield count will be
    displayed next to the item name.
    
    You can choose if extra shields should only be
    obtainable from randomized items or if they should
    also be repeatedly buyable from shops.
    """
    display_name = "Keep Extra Shields"
    option_never = 0
    option_only_if_random = 1
    option_always_allowed = 2
    default = option_only_if_random

    @classmethod
    def get_option_name(cls, value: T) -> str: # type: ignore
        if value == cls.option_never:
            return "Never (Vanilla)"
        return super().get_option_name(value) # type: ignore

######################
# Item Pool Settings #
######################

class ItemPool(Choice):
    """
    Balanced:
    Original item pool.

    Plentiful:
    Extra major items are added to the pool.

    Minimal:
    Most excess items are removed.

    Scarce:
    Some excess items are removed, including health
    upgrades.
    """
    display_name = "Item Pool"
    option_balanced = 0
    option_plentiful = 1
    option_minimal = 2
    option_scarce = 3
    default = option_balanced

class IceTraps(Choice):
    """
    Off:
    All Ice Traps are removed.

    Normal:
    Only Ice Traps from the base item pool are placed.

    Extra:
    Chance to add extra Ice Traps when junk items are
    added to the itempool.

    Mayhem:
    All added junk items will be Ice Traps.

    Onslaught:
    All junk items will be replaced by Ice Traps, even
    those in the base pool.
    """
    display_name = "Ice Traps"
    option_off = 0
    option_normal = 1
    option_extra = 2
    option_mayhem = 3
    option_onslaught = 4
    default = option_normal

class RemoveDoubleDefense(Toggle):
    """
    If set the double defense item will be removed
    from the item pool for balanced and plentiful.
    """
    display_name = "Remove Double Defense"
    default = False

class ProgGoronSword(Toggle):
    """
    Giant's Knife will always be found         
    before Biggoron's Sword. Medigoron only starts
    selling new knives once the Giant's Knife  
    has been found and broken.
    """
    display_name = "Prog Goron Sword"
    default = False

###########################
# Item Usability Settings #
###########################

class FaroresWindAnywhere(Toggle):
    """
    Farore's Wind can be used outside of dungeons.
    """
    display_name = "Farore's Wind Anywhere"
    default = False

class LiftAgeRestrictions(OptionSet):
    """
    Remove age restrictions for inventory items.

    Most of the items won't appear correctly when
    used as teh wrong version of Link, but they'll
    be fully functional otherwise.
    """
    display_name = "Lift Age Restrictions"
    valid_keys = {
        "Adult Deku Stick",
        "Adult Boomerang",
        "Child Hammer",
        "Adult Slingshot",
        "Child Bow",
        "Child Hookshot",
        "Child Iron Boots",
        "Child Hover Boots",
        "Adult Masks",
        "Adult Kokiri Sword",
        "Child Master Sword",
        "Child Biggoron Sword",
        "Adult Deku Shield",
        "Child Mirror Shield",
        "Child Goron Tunic",
        "Child Zora Tunic",
    }
    default = {}

class LiftAgeRestrictionsInLogic(Toggle):
    """
    Using items as the wrong age may be required to
    beat the seed.
    """
    display_name = "Consider Lifted Age Restrictions in Logic"
    default = False

class RestoreISG(Toggle):
    """
    The Infinite Sword Glitch will work like in OoT.
    
    Specifically, interrupting a crouch stab will
    activate the glitch, and putting away or pulling
    out items will not cancel it.
    """
    display_name = "Restore ISG"
    default = True

class GKDurability(Choice):
    """
    Vanilla:
    The durability will always be set to 8.

    Random Risk:
    Each Giant's Knife will get a random durability
    between 1 and 128, with low being more common,
    and with an average of 15.

    Random Safe:
    Each Giant's Knife will get a random durability
    between 10 and 50, with an average of 30.
    """
    display_name = "GK Durability"
    option_vanilla = 0
    option_random_risk = 1
    option_random_safe = 2
    default = option_vanilla

class RupeesAsAmmo(Toggle):
    """
    If you run out of ammo or magic, you'll use
    rupees instead.
    """
    display_name = "Rupees as Ammo"
    default = False

#####################
# Gameplay Settings #
#####################

class FastBunnyHood(Toggle):
    """
    The Bunny Hood mask behaves like it does in
    Majora's Mask and makes you run 50% faster.
    """
    display_name = "Fast Bunny Hood"
    default = False

class KeepFWWarpPoint(Toggle):
    """
    The Farore's Wind warp point will stay active
    after having been warped to. The old point will
    need to be dispelled before setting a new one.
    """
    display_name = "Keep FW Warp Point"
    default = False

class DamageMultiplier(Choice):
    """
    Changes the amount of damage taken.
    
    If set to OHKO, Link will die in one hit.
    """
    display_name = "Damage Multiplier"
    option_half = 0
    option_single = 1
    option_double = 2
    option_quadruple = 3
    option_octuple = 4
    option_sixteen = 5
    option_ohko = 6
    default = option_single

    @classmethod
    def get_option_name(cls, value: T) -> str: # type: ignore
        if value == cls.option_half:
            return "x1/2"
        elif value == cls.option_single:
            return "x1"
        elif value == cls.option_double:
            return "x2"
        elif value == cls.option_quadruple:
            return "x4"
        elif value == cls.option_octuple:
            return "x8"
        elif value == cls.option_sixteen:
            return "x16"
        elif value == cls.option_ohko:
            return "OHKO"
        return super().get_option_name(value) # type: ignore

class BonkDamage(Choice):
    """
    Choose how many Hearts of damage you'll take when
    hitting a wall or object during a roll.
         
    Damage is unaffected by the damage multiplier 
    setting, but it will respect Nayru's Love and 
    Double Defense.
    """
    display_name = "Bonk Damage"
    option_zero = 0
    option_quarter = 1
    option_half = 2
    option_one = 3
    option_two = 4
    option_four = 5
    option_ohko = 6
    default = option_zero

    @classmethod
    def get_option_name(cls, value: T) -> str: # type: ignore
        if value == cls.option_zero:
            return "0"
        elif value == cls.option_quarter:
            return "1/4"
        elif value == cls.option_half:
            return "1/2"
        elif value == cls.option_one:
            return "1"
        elif value == cls.option_two:
            return "2"
        elif value == cls.option_four:
            return "4"
        elif value == cls.option_ohko:
            return "OHKO"
        return super().get_option_name(value) # type: ignore

class GloomMode(Choice):
    """
    Enabling this setting will make your hearts
    permanently disappear on various conditions.

    Death:
    Delete 1 heart when getting a Game Over.

    Damage:
    Delete 1 heart when losing health for any reason,
    except continuous elemental damage from being 
    burned or frozen.

    Double Defense will require 2 hits per heart.

    Collision:
    Delete 1 heart not only when losing health, but
    also when any collision is detected: getting hit
    during invincibility frames or blocking an attack
    with your shield count as collisions.

    Double Defense will require 2 hits per heart.

    WARNING: THE GAME MAY BE IMPOSSIBLE TO BEAT
    because you can still be expected to use a shield
    (for example to reflect Twinrova's attacks).

    Empty:
    Hearts will be deleted when they become empty.
    """
    display_name = "Gloom Mode"
    option_off = 0
    option_death = 1
    option_damage = 2
    option_collision = 3
    option_empty = 4
    default = option_off

class RandomTrapDamage(Choice):
    """
    Off:
    All traps will be the base game ice trap

    Basic:
    All alternative traps will cause a small damage
    and no other negative effects

    Advanced:
    Toggle individual advanced traps from the options
    below
    """
    display_name = "Random Trap Damage"
    option_off = 0
    option_basic = 1
    option_advanced = 2
    default = option_basic

class FireTrap(Toggle):
    """
    This trap will set you on fire, burning your
    Deku Shield if it's equipped.
    """
    display_name = "Fire Trap"
    default = True

class AntiFairyTrap(Toggle):
    """
    This dangerous fairy will inflict up to 8 hearts
    of damage, but it usually doesn't kill you if you
    have less than that.
    """
    display_name = "Anti Fairy Trap"
    default = True

class RupoorTrap(Choice):
    """
    This rupee will make you poor instead of rich.

    10:
    Rupoors behave how they do in other zelda titles,
    deducting 10 rupees from your wallet.

    Random Ratio:
    Rupoors will deduct a random amount of rupees
    (between 5% and 65% of your current max rupees)
    from your wallet.

    Bankruptcy:
    Rupoors will take all your rupees and make you
    sad.
    """
    display_name = "Rupoor Trap"
    option_off = 0
    option_ten = 1
    option_random_ratio = 2
    option_bankruptcy = 3
    default = option_off

class CurseTraps(Toggle):
    """
    Some traps will apply status effects for 1 minute.
    """
    display_name = "Curse Traps"
    default = False

class ScreenTraps(Toggle):
    """
    Extra curses are added that rotate the screen.
    """
    display_name = "Screen Traps"
    default = False

class ExtraArrowEffects(Toggle):
    """
    Ice Arrows will act like blue fire, melting red
    ice and breaking mud walls in Dodongo's Cavern.

    Light Arrows will activate Sun Switches like in
    Majora's Mask.
    """
    display_name = "Extra Arrow Effects"
    default = False

class HyperActors(OptionSet):
    """
    Powers up the selected actors, allowing them to
    move and act twice as fast.
    """
    display_name = "Hyper Actors"
    valid_keys = {
        "Bosses",
        "Middle Bosses",
        "Enemies",
    }
    default = {}

class FreeCamera(Toggle):
    """
    Use the C-stick to control the camera on new 3DS
    systems and Citra.

    Go to Personalization Settings > Ingame Defaults
    for camera control options.
    """
    display_name = "Free Camera"
    default = True

class RandomGSLocations(Toggle):
    """
    Moves Gold Skulltulas to different locations
    around the same area as the original.
    The age they appear in is always the same as the
    original. If it hides during the night mostly
    depends on if the sun can reach it.
    They will never be in generic areas, such as
    Business Scrub grottos, Fairy Fountains, etc.
    Some new locations are only available with certain
    settings enabled, like tricks and glitches.
    WIP feature. Most dungeon locations are the same.
    """
    display_name = "Random GS Locations"
    default = False

class GuaranteeNewLocations(Toggle):
    """
    Excludes the original location from the Gold
    Skulltula's available locations pool.
    
    If no new locations are available, the original
    will be used regardless.
    """
    display_name = "Guarantee New GS Locations"
    default = False

class RandomOcarinaMelodies(Toggle):
    """
    Randomize the notes for each ocarina song.
    Regular songs will be 3 notes repeated twice.
    Warp songs will be between 5 and 8 notes.
    """
    display_name = "Random Ocarina Melodies"
    default = False

class FrogSongTimer(Range):
    """
    Multiplier for the time you have to play each
    note in the final frog song.
    """
    display_name = "Frog Song Timer"
    range_start = 1
    range_end = 4
    default = 1

@dataclass
class OoT3DOptions(PerGameCommonOptions):
    # Open Settings
    forest_open:                     OpenForest
    kak_gate_open:                   OpenKakarikoGate
    door_time_open:                  OpenDoorOfTime
    fountain_open:                   OpenZorasFountain
    jabu_jabu_open:                  OpenJabuJabu
    gerudo_open:                     OpenGerudoFortress
    bridge_open:                     OpenRainbowBridge
    bridge_stone_count:              BridgeStoneCount
    bridge_medallion_count:          BridgeMedallionCount
    bridge_dungeon_rewards_count:    BridgeDungeonRewardsCount
    bridge_dungeon_count:            BridgeDungeonCount
    bridge_token_count:              BridgeTokenCount
    bridge_heart_count:              BridgeHeartCount
    random_ganons_trials:            RandomGanonsTrials
    ganons_trial_count:              TrialCount

    # World Settings
    starting_age:                    StartingAge
    shuffle_entrances:               ShuffleEntrances
    shuffle_dungeon_entrances:       ShuffleDungeonEntrances
    shuffle_boss_entrances:          ShuffleBossEntrances
    shuffle_overworld_entrances:     ShuffleOverworldEntrances
    shuffle_interior_entrances:      ShuffleInteriorEntrances
    shuffle_grottos_entrances:       ShuffleGrottosEntrances
    shuffle_owl_drops:               ShuffleOwlDrops
    shuffle_warp_songs:              ShuffleWarpSongs
    shuffle_overworld_spawns:        ShuffleOverworldSpawns
    mixed_entrance_pools:            MixedEntrancePools
    mix_dungeons:                    MixDungeons
    mix_overworld:                   MixOverworld
    mix_interior:                    MixInterior
    mix_grottos:                     MixGrottos
    decouple_entrances:              DecoupleEntrances
    bombchus_in_logic:               BombchusInLogic
    ammo_drops:                      AmmoDrops
    heart_drops_and_refills:         HeartDropsAndRefills
    mq_dungeon_count:                MQDungeonCount
    set_dungeon_types:               SetDungeonTypes
    deku_tree_dungeon_type:          DekuTreeDungeonType
    dodongos_cavern_dungeon_type:    DodongosCavernDungeonType
    jabu_jabus_belly_dungeon_type:   JabuJabusBellyDungeonType
    forest_temple_dungeon_type:      ForestTempleDungeonType
    fire_temple_dungeon_type:        FireTempleDungeonType
    water_temple_dungeon_type:       WaterTempleDungeonType
    spirit_temple_dungeon_type:      SpiritTempleDungeonType
    shadow_temple_dungeon_type:      ShadowTempleDungeonType
    bottom_of_the_well_dungeon_type: BottomOfTheWellDungeonType
    ice_cavern_dungeon_type:         IceCavernDungeonType
    training_grounds_dungeon_type:   TrainingGroundsDungeonType
    ganons_castle_dungeon_type:      GanonsCastleDungeonType
    triforce_hunt:                   TriforceHunt
    triforce_pieces:                 TriforcePieces
    required_triforce_pieces:        RequiredTriforcePieces

    # Enemy Randomizer
    enemy_randomizer:                EnemyRandomizer
    randomize_anubis:                Anubis
    randomize_armos:                 Armos
    randomize_bari:                  Bari
    randomize_beamos:                Beamos
    randomize_biri:                  Biri
    randomize_bubble_blue:           BubbleBlue
    randomize_bubble_fire:           BubbleFire
    randomize_bubble_green:          BubbleGreen
    randomize_bubble_white:          BubbleWhite
    randomize_dark_link:             DarkLink
    randomize_dead_hands_hand:       DeadHandsHand
    randomize_deku_baba_small:       DekuBabaSmall
    randomize_deku_baba_big:         DekuBabaBig
    randomize_deku_baba_withered:    DekuBabaWithered
    randomize_deku_scrub:            DekuScrub
    randomize_dinolfos:              Dinolfos
    randomize_dodongo_normal:        DodongoNormal
    randomize_dodongo_baby:          DodongoBaby
    randomize_flare_dancer:          FlareDancer
    randomize_floormaster:           Floormaster
    randomize_flying_floor_tile:     FlyingFloorTile
    randomize_flying_pot:            FlyingPot
    randomize_freezard:              Freezard
    randomize_gerudo_fighter:        GerudoFighter
    randomize_gibdo:                 Gibdo
    randomize_gohma_larva:           GohmaLarva
    randomize_guay:                  Guay
    randomize_iron_knuckle:          IronKnuckle
    randomize_keese_normal:          KeeseNormal
    randomize_keese_fire:            KeeseFire
    randomize_keese_ice:             KeeseIce
    randomize_leever:                Leever
    randomize_like_like:             LikeLike
    randomize_lizalfos:              Lizalfos
    randomize_mad_scrub:             MadScrub
    randomize_moblin_club:           MoblinClub
    randomize_moblin_spear:          MoblinSpear
    randomize_octorok:               Octorok
    randomize_peahat:                Peahat
    randomize_peahat_larva:          PeahatLarva
    randomize_poe:                   Poe
    randomize_redead:                Redead
    randomize_shabom:                Shabom
    randomize_shell_blade:           ShellBlade
    randomize_skulltula:             Skulltula
    randomize_skullwalltula:         Skullwalltula
    randomize_skull_kid:             SkullKid
    randomize_spike:                 Spike
    randomize_stalchild:             Stalchild
    randomize_stalfos:               Stalfos
    randomize_stinger_floor:         StingerFloor
    randomize_stringer_water:        StringerWater
    randomize_tailpasaran:           Tailpasaran
    randomize_tektite_blue:          TektiteBlue
    randomize_tektite_red:           TektiteRed
    randomize_torch_slug:            TorchSlug
    randomize_wallmaster:            Wallmaster
    randomize_wolfos:                Wolfos

    # Shuffle Settings
    shuffle_dungeon_rewards:         ShuffleDungeonRewards
    link_s_pocket:                   LinksPocket
    shuffle_songs:                   ShuffleSongs
    shopsanity:                      Shopsanity
    shopsanity_prices:               ShopsanityPrices
    tokensanity:                     Tokensanity
    scrub_shuffle:                   ScrubShuffle
    shuffle_cows:                    ShuffleCows
    shuffle_korok_sword:             ShuffleKokiriSword
    shuffle_master_sword:            ShuffleMasterSword
    shuffle_ocarinas:                ShuffleOcarinas
    shuffle_weird_egg:               ShuffleWeirdEgg
    shuffle_zeldas_letter:           ShuffleZeldasLetter
    shuffle_gerudo_token:            ShuffleGerudoToken
    shuffle_magic_beans:             ShuffleMagicBeans
    shuffle_merchants:               ShuffleMerchants
    shuffle_adult_trade:             ShuffleAdultTrade
    shuffle_chest_minigame:          ShuffleChestMinigame
    shuffle_frog_rupees:             ShuffleFrogRupees
    shuffle_enemy_souls:             ShuffleEnemySouls
    shuffle_ocarina_buttons:         ShuffleOcarinaButtons
    shuffle_standing_rupees:         ShuffleStandingRupees
    shuffle_recovery_hearts:         ShuffleRecoveryHearts
    shuffle_big_poes:                ShuffleBigPoes

    # Shuffle Dungeon Items
    shuffle_maps_and_compasses:      ShuffleMapsAndCompasses
    shuffle_small_keys:              ShuffleSmallKeys
    shuffle_gerudo_fortress_keys:    ShuffleGerudoFortressKeys
    shuffle_boss_keys:               ShuffleBossKeys
    shuffle_ganons_boss_key:         ShuffleGanonsBossKey
    shuffle_lacs_medallion_count:    LACSMedallionCount
    shuffle_lacs_stone_count:        LACSStoneCount
    shuffle_lacs_reward_count:       LACSRewardCount
    shuffle_lacs_dungeon_count:      LACSDungeonCount
    shuffle_lacs_token_count:        LACSTokenCount
    shuffle_lacs_heart_count:        LACSHeartCount
    key_rings:                       KeyRings

    # Timesaver Settings
    skip_child_stealth:              SkipChildStealth
    skip_tower_escape:               SkipTowerEscape
    skip_epona_race:                 SkipEponaRace
    skip_minigames_repetitions:      SkipMinigamesRepetitions
    free_scarecrow:                  FreeScarecrow
    skip_four_poes_cutscene:         SkipFourPoesCutscene
    lake_hylia_owl:                  LakeHyliaOwl
    big_poe_target_count:            BigPoeTargetCount
    cuccos_to_return:                CuccosToReturn
    king_zora_speed:                 KingZoraSpeed
    complete_mask_quest:             CompleteMaskQuest

    # Logic Options
    logic:                           Logic
    night_skulltulas_expert:         NightSkultullasExpectSun
    logical_tricks:                  LogicalTricks

    # Glitches
    restricted_items:                RestrictedItems
    super_stab:                      SuperStab
    infinite_sword_glitch:           InfiniteSwordGlitch
    bomb_hover:                      BombHover
    ocarina_items_bomb:              OcarinaItemsBomb
    hover_boost:                     HoverBoost
    extend_super_slide:              ExtendedSuperSlide
    megaflip:                        Megaflip
    a_slide:                         ASlide
    hammer_slide:                    HammerSlide
    ledge_cancel:                    LedgeCancel
    action_swap:                     ActionSwap
    quick_put_away:                  QuickPutAway
    hooket_clip:                     HookshotClip
    hooket_jump_bonk:                HookshotJumpBonk
    hooket_jump_boots:               HookshotJumpBoots
    cutscene_dives:                  CutsceneDives
    navi_dive_stick:                 NaviDiveStick
    triple_slash_clip:               TripleSlashClip
    ledge_clip:                      LedgeClip
    seam_walk:                       SeamWalk
    misc_glitches:                   MiscGlitches

    # Misc Settings
    racing:                          Racing
    gossip_stone_hints:              GossipStoneHints
    hint_distribution:               HintDistribution
    misc_hint:                       MiscHints
    hint_clarity:                    HintClarity
    compasses_show_rewards:          CompassesShowRewards
    compasses_show_wot_h:            CompassesShowWotH
    maps_show_dungeon_modes:         MapsShowDungeonModes
    starting_time:                   StartingTime
    chest_animations:                ChestAnimations
    chest_appearance_mod:            ChestAppearanceMod
    chest_agony:                     ChestAgony
    keep_extra_shields:              KeepExtraShields

    # Item Pool Settings
    item_pool:                       ItemPool
    ice_traps:                       IceTraps
    remove_double_defense:           RemoveDoubleDefense
    prog_goron_sword:                ProgGoronSword

    # Item Usability Settings
    farores_wind_anywhere:           FaroresWindAnywhere
    lift_age_restrictions:           LiftAgeRestrictions
    lift_age_restrictions_in_logic:  LiftAgeRestrictionsInLogic
    restore_isg:                     RestoreISG
    gk_durability:                   GKDurability
    rupees_as_ammo:                  RupeesAsAmmo

    # Gameplay Settings
    fast_bunny_hood:                 FastBunnyHood
    keep_fw_warp_point:              KeepFWWarpPoint
    damage_multiplier:               DamageMultiplier
    bonk_damage:                     BonkDamage
    gloom_mode:                      GloomMode
    random_trap_damage:              RandomTrapDamage
    fire_trap:                       FireTrap
    anti_fairy_trap:                 AntiFairyTrap
    rupoor_trap:                     RupoorTrap
    curse_traps:                     CurseTraps
    screen_traps:                    ScreenTraps
    extra_arrows_effects:            ExtraArrowEffects
    hyper_actors:                    HyperActors
    free_camera:                     FreeCamera
    random_gs_locations:             RandomGSLocations
    guarantee_new_locations:         GuaranteeNewLocations
    random_ocarina_melodies:         RandomOcarinaMelodies
    frog_song_timer:                 FrogSongTimer

option_groups = [
    OptionGroup(
        "Open Settings",
        [
            OpenForest,
            OpenKakarikoGate,
            OpenDoorOfTime,
            OpenZorasFountain,
            OpenJabuJabu,
            OpenGerudoFortress,
            OpenRainbowBridge,
            BridgeStoneCount,
            BridgeMedallionCount,
            BridgeDungeonRewardsCount,
            BridgeDungeonCount,
            BridgeTokenCount,
            BridgeHeartCount,
            RandomGanonsTrials,
            TrialCount,
        ]
    ),
    OptionGroup(
        "World Settings",
        [
            StartingAge,
            ShuffleEntrances,
            ShuffleDungeonEntrances,
            ShuffleBossEntrances,
            ShuffleOverworldEntrances,
            ShuffleInteriorEntrances,
            ShuffleGrottosEntrances,
            ShuffleOwlDrops,
            ShuffleWarpSongs,
            ShuffleOverworldSpawns,
            MixedEntrancePools,
            MixDungeons,
            MixOverworld,
            MixInterior,
            MixGrottos,
            DecoupleEntrances,
            BombchusInLogic,
            AmmoDrops,
            HeartDropsAndRefills,
            MQDungeonCount,
            SetDungeonTypes,
            DekuTreeDungeonType,
            DodongosCavernDungeonType,
            JabuJabusBellyDungeonType,
            ForestTempleDungeonType,
            FireTempleDungeonType,
            WaterTempleDungeonType,
            SpiritTempleDungeonType,
            ShadowTempleDungeonType,
            BottomOfTheWellDungeonType,
            IceCavernDungeonType,
            TrainingGroundsDungeonType,
            GanonsCastleDungeonType,
            TriforceHunt,
            TriforcePieces,
            RequiredTriforcePieces,
        ]
    ),
    OptionGroup(
        "Enemy Randomizer",
        [
            EnemyRandomizer,
            Anubis,
            Armos,
            Bari,
            Beamos,
            Biri,
            BubbleBlue,
            BubbleFire,
            BubbleGreen,
            BubbleWhite,
            DarkLink,
            DeadHandsHand,
            DekuBabaSmall,
            DekuBabaBig,
            DekuBabaWithered,
            DekuScrub,
            Dinolfos,
            DodongoNormal,
            DodongoBaby,
            FlareDancer,
            Floormaster,
            FlyingFloorTile,
            FlyingPot,
            Freezard,
            GerudoFighter,
            Gibdo,
            GohmaLarva,
            Guay,
            IronKnuckle,
            KeeseNormal,
            KeeseFire,
            KeeseIce,
            Leever,
            LikeLike,
            Lizalfos,
            MadScrub,
            MoblinClub,
            MoblinSpear,
            Octorok,
            Peahat,
            PeahatLarva,
            Poe,
            Redead,
            Shabom,
            ShellBlade,
            Skulltula,
            Skullwalltula,
            SkullKid,
            Spike,
            Stalchild,
            Stalfos,
            StingerFloor,
            StringerWater,
            Tailpasaran,
            TektiteBlue,
            TektiteRed,
            TorchSlug,
            Wallmaster,
            Wolfos,
        ]
    ),
    OptionGroup(
        "Shuffle Settings",
        [
            ShuffleDungeonRewards,
            LinksPocket,
            ShuffleSongs,
            Shopsanity,
            ShopsanityPrices,
            Tokensanity,
            ScrubShuffle,
            ShuffleCows,
            ShuffleKokiriSword,
            ShuffleMasterSword,
            ShuffleOcarinas,
            ShuffleWeirdEgg,
            ShuffleZeldasLetter,
            ShuffleGerudoToken,
            ShuffleMagicBeans,
            ShuffleMerchants,
            ShuffleAdultTrade,
            ShuffleChestMinigame,
            ShuffleFrogRupees,
            ShuffleEnemySouls,
            ShuffleOcarinaButtons,
            ShuffleStandingRupees,
            ShuffleRecoveryHearts,
            ShuffleBigPoes,
        ]
    ),
    OptionGroup(
        "Shuffle Dungeon Items",
        [
            ShuffleMapsAndCompasses,
            ShuffleSmallKeys,
            ShuffleGerudoFortressKeys,
            ShuffleBossKeys,
            ShuffleGanonsBossKey,
            LACSMedallionCount,
            LACSStoneCount,
            LACSRewardCount,
            LACSDungeonCount,
            LACSTokenCount,
            LACSHeartCount,
            KeyRings,
        ]
    ),
    OptionGroup(
        "Timesaver Settings",
        [
            SkipChildStealth,
            SkipTowerEscape,
            SkipEponaRace,
            SkipMinigamesRepetitions,
            FreeScarecrow,
            SkipFourPoesCutscene,
            LakeHyliaOwl,
            BigPoeTargetCount,
            CuccosToReturn,
            KingZoraSpeed,
            CompleteMaskQuest,
        ]
    ),
    OptionGroup(
        "Logic Options",
        [
            Logic,
            NightSkultullasExpectSun,
            LogicalTricks,
        ]
    ),
    OptionGroup(
        "Glitches",
        [
            RestrictedItems,
            SuperStab,
            InfiniteSwordGlitch,
            BombHover,
            OcarinaItemsBomb,
            HoverBoost,
            ExtendedSuperSlide,
            Megaflip,
            ASlide,
            HammerSlide,
            LedgeCancel,
            ActionSwap,
            QuickPutAway,
            HookshotClip,
            HookshotJumpBonk,
            HookshotJumpBoots,
            CutsceneDives,
            NaviDiveStick,
            TripleSlashClip,
            LedgeClip,
            SeamWalk,
            MiscGlitches,
        ]
    ),
    OptionGroup(
        "Misc Settings",
        [
            Racing,
            GossipStoneHints,
            HintDistribution,
            MiscHints,
            HintClarity,
            CompassesShowRewards,
            CompassesShowWotH,
            MapsShowDungeonModes,
            StartingTime,
            ChestAnimations,
            ChestAppearanceMod,
            ChestAgony,
            KeepExtraShields,
        ]
    ),
    OptionGroup(
        "Item Pool Settings",
        [
            ItemPool,
            IceTraps,
            RemoveDoubleDefense,
            ProgGoronSword,
        ]
    ),
    OptionGroup(
        "Item Usability Settings",
        [
            FaroresWindAnywhere,
            LiftAgeRestrictions,
            LiftAgeRestrictionsInLogic,
            RestoreISG,
            GKDurability,
            RupeesAsAmmo,
        ]
    ),
    OptionGroup(
        "Gameplay Settings",
        [
            FastBunnyHood,
            KeepFWWarpPoint,
            DamageMultiplier,
            BonkDamage,
            GloomMode,
            RandomTrapDamage,
            FireTrap,
            AntiFairyTrap,
            RupoorTrap,
            CurseTraps,
            ScreenTraps,
            ExtraArrowEffects,
            HyperActors,
            FreeCamera,
            RandomGSLocations,
            GuaranteeNewLocations,
            RandomOcarinaMelodies,
            FrogSongTimer,
        ]
    )
]

option_presets = {
    #"placeholder": {
    #    "placeholder": True,
    #    "trap_chance": 50,
    #},
}
