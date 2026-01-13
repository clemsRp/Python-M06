#!/usr/bin/env python3

import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water


def main() -> None:
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print()

    print("Method 2 - Specific function import:")
    print("create_water():", create_water())
    print()

    print("Method 3 - Aliased import:")
    print("heal():", heal())
    print()

    print("Method 4 - Multiple imports:")
    print("create_earth():", alchemy.elements.create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", alchemy.potions.strength_potion())
    print()


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")

    main()

    print("All import transmutation methods mastered!")
