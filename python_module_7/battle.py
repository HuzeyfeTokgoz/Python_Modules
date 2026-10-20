from ex0.factories import CreatureFactory
from ex0 import FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")

    warrior1 = factory1.create_base()
    warrior2 = factory2.create_base()

    print(warrior1.describe())
    print(" vs.")
    print(warrior2.describe())
    print(" fight!")

    print(warrior1.attack())
    print(warrior2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    test_battle(flame_factory, aqua_factory)
