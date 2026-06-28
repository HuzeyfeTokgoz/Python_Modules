#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        32 / 0
    elif operation_number == 2:
        open("/none/file")
    elif operation_number == 3:
        "abc" + 32


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    ops = [0, 1, 2, 3, 4]
    for i in ops:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
        except TypeError as e:
            print(f"Caught TypeError: {e}\n")
        else:
            print("Operation completed successfully\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
