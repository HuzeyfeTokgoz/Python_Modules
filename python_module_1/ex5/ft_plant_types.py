#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm,"
              f" {self.age} days old")

    def add_age(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height += 0.8


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


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade of"
              f" {self.height}cm long and {self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        self.height += 2.1
        self.nutritional_value += 1

    def pass_time(self, days: int) -> None:
        for _ in range(days):
            self.grow()
            self.add_age()


if __name__ == "__main__":
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April", 0)

    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.pass_time(20)
    tomato.show()
