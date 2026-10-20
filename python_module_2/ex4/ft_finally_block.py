#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, error: str = "Unknown plant error") -> None:
        Exception.__init__(self, error)


def water_plant(plant_name: str) -> None:
    if plant_name and plant_name[0].isupper():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")

    data = ["Tomato", "Lettuce", "Carrots"]
    try:
        for plant in data:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")

    data2 = ["Tomato", "lettuce", "Carrots"]
    try:
        for plant in data2:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
