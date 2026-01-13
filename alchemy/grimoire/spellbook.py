#!/usr/bin/env python3

def record_spell(spell_name: str, ingredients: str) -> str:
    '''
    Return a string about the spell state
    '''
    from . import validator

    valid = validator.validate_ingredients(ingredients)
    state = "recorded"
    if valid[-7:] == "INVALID":
        state = "rejected"
    return f"Spell {state}: {spell_name} ({valid})"
