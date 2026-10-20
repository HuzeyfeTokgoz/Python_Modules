import abc
from .capabilities import Shiftling, Sproutling, Morphagon, Bloomelle
from ex0.creatures import Creature


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> Creature:
        ...

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        ...


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
