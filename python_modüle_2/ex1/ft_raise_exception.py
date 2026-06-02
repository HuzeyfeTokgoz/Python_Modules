#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    value = int(temp_str)
    if 40 < value:
        raise Exception(f"Caught input_temperature error: {value}°C is too hot for plants (max 40°C)")
    elif 0 > value:
        raise Exception(f"Caught input_temperature error: {value}°C is too cold for plants (min 0°C)")
    return value


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    data = ["25", "abc", "100", "-50"]
    
    for d in data:
        print(f"Input data is '{d}'")
        try:
            print(f"Temperature is now {input_temperature(d)}°C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()