#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    '''
    Return a string about the ingredients list state
    '''
    for ingredient in ingredients.split():
        if ingredient not in ["fire", "water", "earth", "air"]:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
