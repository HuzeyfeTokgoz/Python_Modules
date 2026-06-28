import abc
from . import capabilities


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self):
        ...

    @abc.abstractmethod
    def create_evolved(self):
        ...


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return capabilities.Sproutling()

    def create_evolved(self):
        return capabilities.Bloomelle()
    

class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return capabilities.Shiftling()

    def create_evolved(self):
        return capabilities.Morphagon()
