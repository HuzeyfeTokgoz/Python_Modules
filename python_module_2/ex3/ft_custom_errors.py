#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, error: str = "Unknown garden error") -> None:
        Exception.__init__(self, error)


class PlantError(GardenError):
    def __init__(self, error: str = "Unknown plant error") -> None:
        GardenError.__init__(self, error)


class WaterError(GardenError):
    def __init__(self, error: str = "Unknown water error") -> None:
        GardenError.__init__(self, error)


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")

    except PlantError as e:
        print(f"caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
