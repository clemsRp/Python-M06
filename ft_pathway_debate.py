#!/usr/bin/env python3

from alchemy import transmutation
import alchemy.transmutation.basic as basic
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


def main() -> None:
    print("Testing Absolute Imports (from basic.py):")

    print("lead_to_gold():", basic.lead_to_gold())
    print("stone_to_gem():", basic.stone_to_gem())
    print()

    print("Testing Relative Imports (from advanced.py):")
    print("philosophers_stone(): ", end="")
    print(philosophers_stone())
    print("elixir_of_life():", elixir_of_life())
    print()

    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold(): ", end="")
    print(transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone() :", end="")
    print(transmutation.philosophers_stone())
    print()


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")

    main()

    print("Both pathways work! Absolute: clear, Relative: concise")
