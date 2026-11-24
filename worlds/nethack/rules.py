from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import NHWorld


def set_all_rules(world: NHWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: NHWorld) -> None:
    pass

def set_all_location_rules(world: NHWorld) -> None:
    pass

def set_completion_condition(world: NHWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: True
