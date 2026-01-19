#!/usr/bin/env python3

from . import elements


def healing_potion() -> str:
    '''
    Simulate the use of healing potion
    '''
    f, w = elements.create_fire(), elements.create_water()
    return f"Healing potion brewed with {f} and {w}"


def strength_potion() -> str:
    '''
    Simulate the use of strength potion
    '''
    e, f = elements.create_earth(), elements.create_fire()
    return f"Strength potion brewed with {e} and {f}"


def invisibility_potion() -> str:
    '''
    Simulate the use of invisibility potion
    '''
    a, w = elements.create_air(), elements.create_water()
    return f"Invisibility potion brewed with {a} and{w}"


def wisdom_potion() -> str:
    '''
    Simulate the use of the wisdow potion
    '''
    all_elements = [
        elements.create_fire(),
        elements.create_water(),
        elements.create_earth(),
        elements.create_air()
    ]
    return f"Wisdom potion brewed with all elements: {', '.join(all_elements)}"
