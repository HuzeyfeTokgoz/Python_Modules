from typing import Any
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, \
    DefensiveStrategy, InvalidStrategyError


def tournament(opponents: list[tuple[Any, Any]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            warrior1 = factory1.create_base()
            warrior2 = factory2.create_base()

            print("\n* Battle *")
            print(warrior1.describe())
            print(" vs.")
            print(warrior2.describe())
            print(" now fight!")

            try:
                strategy1.act(warrior1)
                strategy2.act(warrior2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    print("Tournament (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    tournament([
        (flame_factory, normal_strat),
        (heal_factory, defensive_strat)
    ])

    print("\n----------------------------------\n")

    print("Tournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    tournament([
        (flame_factory, aggressive_strat),
        (heal_factory, defensive_strat)
    ])

    print("\n----------------------------------\n")

    print("Tournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    tournament([
        (aqua_factory, normal_strat),
        (heal_factory, defensive_strat),
        (transform_factory, aggressive_strat)
    ])
