#!/usr/bin/env python3

class Plant:
    class _Analytics:
        def __init__(self) -> None:
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def value_grow(self) -> None:
            self.__grow_calls += 1

        def value_age(self) -> None:
            self.__age_calls += 1

        def value_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self.__grow_calls} grow, {self.__age_calls} age,"
                  f" {self.__show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self._stats = self._Analytics()

    @staticmethod
    def is_year_old(days) -> bool:
        print(f"Is {days} days more than a year? -> ", end="")
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Unknown plant", height=0.0, age=0)

    def grow(self, add_grow: int) -> None:
        self._stats.value_grow()
        self.height += add_grow

    def add_age(self, add_value: int = 1) -> None:
        self._stats.value_age()
        self.age += add_value

    def show(self) -> None:
        self._stats.value_show()
        print(f"{self.name.capitalize()}: {self.height:.1f}cm,"
              f" {self.age} days old ")

    def display_stats(self) -> None:
        self._stats.display()


class Tree(Plant):
    class _TreeAnalytics(Plant._Analytics):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_calls = 0

        def value_shade(self) -> None:
            self.__shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self.__shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree._TreeAnalytics = self._TreeAnalytics()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._stats.value_shade()
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.is_blooming:
            print(f" {self.name.capitalize()} has not bloomed yet")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        self.is_blooming = True


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42


def display_plant_analytics(plant_obj: Plant) -> None:
    print(f"[statistics for {plant_obj.name.capitalize()}]")
    plant_obj.display_stats()


if __name__ == "__main__":
    rose = Flower("rose", 15, 10, "red")
    oak = Tree("oak", 200, 365, 5)
    sunflower = Seed("sunflower", 80, 45, "yellow")

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(Plant.is_year_old(30))
    print(Plant.is_year_old(400))

    print("\n=== Flower")
    rose.show()
    display_plant_analytics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_plant_analytics(rose)

    print("\n=== Tree")
    oak.show()
    display_plant_analytics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_analytics(oak)

    print("\n=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.add_age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_analytics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_plant_analytics(unknown)
