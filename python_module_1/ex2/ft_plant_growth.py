#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def age(self) -> None:
        self.plant_age += 1

    def grow(self) -> None:
        self.height += 0.8

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


if __name__ == "__main__":
    Rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    print(Rose.show())
    temp = Rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        Rose.age()
        Rose.grow()
        Rose.height = round(Rose.height, 1)
        print(Rose.show())
    print(f"Growth this week: {round(Rose.height - temp, 1)}cm")
