#!/usr/bin/env python3

def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        int(32) / 0
    elif operation_number == 2:
        open("/none/file")
    elif operation_number == 3:
        "abc" + 32
    else:
        print("Operation completed successfully\n")

def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            value = garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
        except TypeError as e:
            print(f"Caught TypeError: {e}\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()