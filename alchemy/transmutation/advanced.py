#!/usr/bin/env python3

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    l, h = lead_to_gold(), healing_potion
    return f"Philosopher’s stone created using {l} and {h}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
