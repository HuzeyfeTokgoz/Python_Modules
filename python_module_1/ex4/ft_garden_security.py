#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._plant_age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def set_height(self, new_height) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age) -> None:
        if new_age >= 0:
            self._plant_age = new_age
            print(f"Age updated: {new_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> str:
        return (f"{self.name}: {self.get_height() :.1f}cm, "
                f"{self.get_age()} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.show()}\n")

    rose.set_height(20)
    rose.set_age(100)
    print("")
    rose.set_height(-20)
    rose.set_age(-100)
    print(f"\nCurrent state: {rose.show()}")
