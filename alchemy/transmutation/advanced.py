#!/usr/bin/env python3

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    '''
    Simulate the creation of the philosopher stone
    '''
    l, h = lead_to_gold(), healing_potion()
    return f"Philosopher’s stone created using {l} and {h}"


def elixir_of_life() -> str:
    '''
    Simulate the use of elexir of life
    '''
    return "Elixir of life: eternal youth achieved!"
