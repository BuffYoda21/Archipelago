from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING, List, Mapping

from BaseClasses import Dict, Item, ItemClassification
from .item_table import *

if TYPE_CHECKING:
    from .world import NHWorld

class NHItem(Item):
    game = "NetHack"

def populate_item_name_to_id() -> Dict[str, int]:
    table = {key: index for index, key in enumerate(item_table)}
    for name in item_table:
        entry = item_table[name]
        if isinstance(entry, tuple):
            unid_name = entry[1]
            if isinstance(unid_name, str):
                table.update({unid_name: len(table)})
    # for entry in table:
    #     print(f"{entry}: {table[entry]}")
    return table

ITEM_NAME_TO_ID = populate_item_name_to_id()

def randomize_item_appearances(world: NHWorld) -> None:
    amulets: list[str] = []
    cloaks: list[str] = []
    helms: list[str] = []
    gloves: list[str] = []
    boots: list[str] = []
    scrolls: list[str] = []
    spellbooks: list[str] = []
    potions: list[str] = []
    rings: list[str] = []
    wands: list[str] = []

    for name in item_table:
        data = item_table[name]
        if isinstance(data, tuple) and isinstance(data[1], int):
            item_type = data[1]
            if item_type == RAND_AMULET:
                amulets.append(name)
            elif item_type == RAND_CLOAK:
                cloaks.append(name)
            elif item_type == RAND_HELM:
                helms.append(name)
            elif item_type == RAND_GLOVE:
                gloves.append(name)
            elif item_type == RAND_BOOT:
                boots.append(name)
            elif item_type == RAND_SCROLL:
                scrolls.append(name)
            elif item_type == RAND_SPELLBOOK:
                spellbooks.append(name)
            elif item_type == RAND_POTION:
                potions.append(name)
            elif item_type == RAND_RING:
                rings.append(name)
            elif item_type == RAND_WAND:
                wands.append(name)

    identified = [amulets, cloaks, helms, gloves, boots, scrolls, spellbooks, potions, rings, wands]
    unidentified = [randomized_amulets, randomized_cloaks, randomized_helms, randomized_gloves, randomized_boots,
                    randomized_scrolls, randomized_spellbooks, randomized_potions, randomized_rings, randomized_wands]

    for appearance_list in unidentified:
        world.random.shuffle(appearance_list)

    combined_list_identified = list(chain.from_iterable(identified))
    combined_list_unidentifed = list(chain.from_iterable(unidentified))

    world.randomized_appearances = {
        combined_list_identified[i]: combined_list_unidentifed[i] for i in range(len(combined_list_identified))
    }
                

# placeholder
def create_all_items(world: NHWorld) -> None:
    itempool: list[Item] = [
        create_item(world, world.random.choice(list(ITEM_NAME_TO_ID.keys()))) for _ in range(len(world.multiworld.get_unfilled_locations(world.player)))
    ]

    world.multiworld.itempool += itempool

def create_item(world: NHWorld, name: str) -> NHItem:
    data = item_table[name]
    classification = ItemClassification.filler
    unid_name = name
    if data is ItemClassification:
        classification = data
    elif data is tuple[ItemClassification, str | int]:
        classification = data[0]
        if data[1] is str:
            unid_name = data[1]
        else:
            pass # Get randomized appearance here

    # add if else block to differintiate between using identified vs unidentified items server side based on user options
    return NHItem(name, classification, ITEM_NAME_TO_ID[name], world.player)