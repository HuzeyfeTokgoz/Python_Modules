#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    data = ["25", "abc"]
    for d in data:
        print(f"Input data is '{d}'")
        try:
            print(f"Temperature is now {input_temperature(d)}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()