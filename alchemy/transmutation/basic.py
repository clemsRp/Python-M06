#!/usr/bin/env python3

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    '''
    Simulate the use of lead to gold
    '''
    return "Lead transmuted to gold using " + create_fire()


def stone_to_gem() -> str:
    '''
    Simulate the use of stone to gem
    '''
    return "Stone transmuted to gem using " + create_earth()
