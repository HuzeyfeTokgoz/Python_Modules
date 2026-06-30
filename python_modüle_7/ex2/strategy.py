import abc
from ex0 import FlameFactory, AquaFactory
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability

class InvalidStrategyError(Exception):
    pass


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def act(self, Creature) -> None:
        ...

    @abc.abstractmethod
    def is_valid(self, Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, Creature) -> bool:
        return True

    def act(self, Creature) -> None:
        if not self.is_valid(Creature):
            raise InvalidStrategyError(f"Invalid Creature '{Creature.name}' for this normal strategy")
        print(Creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, Creature) -> bool:
        return isinstance(Creature, TransformCapability)            

    def act(self, Creature) -> None:
        if not self.is_valid(Creature):
            raise InvalidStrategyError(f"Invalid Creature '{Creature.name}' for this aggressive strategy")
        print(Creature.transform())
        print(Creature.attack())
        print(Creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, Creature) -> bool:
        return isinstance(Creature, HealCapability)

    def act(self, Creature) -> None:
        if not self.is_valid(Creature):
            raise InvalidStrategyError(f"Invalid Creature '{Creature.name}' for this defensive strategy")
        print(Creature.attack())
        print(Creature.heal())
        