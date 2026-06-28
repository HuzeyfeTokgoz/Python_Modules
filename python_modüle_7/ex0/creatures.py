import abc


class Creature(abc.ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abc.abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return(f"{self.name} is a {self.type} type Creature")


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", type="Fire")

    def attack(self) -> str:
        return(f"{self.name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", type="Fire/Flying")

    def attack(self) -> str:
        return(f"{self.name} uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", type="Water")

    def attack(self) -> str:
        return(f"{self.name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", type="Fire")

    def attack(self) -> str:
        return(f"{self.name} uses Hydro Pump!")
