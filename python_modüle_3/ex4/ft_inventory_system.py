#!/usr/bin/env python3
import sys


def inventory_system():
    args = sys.argv[1:]
    new_item = {}

    print("=== Inventory System Analysis ===")
    for arg in args:
        try:
            if ':' in arg:
                key, value = arg.split(':')
            else:
                raise ValueError(f"invalid parameter '{arg}'")
        except ValueError as e:
            print("Error -", e)
            continue

        try:
            value = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}':", e)
            continue

        if key in new_item.keys():
            print(f"Redundant item '{key}' - discarding")
            continue
        else:
            new_item[key] = value

    total_value = sum(new_item.values())
    print("Got inventory: ", new_item)
    print(f"Item list: {list(new_item)}")
    print(f"Total quantity of the {len(new_item.keys())} items: {total_value}")
    for item in new_item.keys():
        print(f"Item {item} represents {round((new_item[item]
                                               / total_value) * 100, 1)}%")

    max_value = -1
    for item_value in new_item.values():
        if item_value > max_value:
            max_value = item_value

    min_value = 99999
    for item in new_item.keys():
        quantity = new_item[item]
        if quantity < min_value:
            min_value = quantity
            least_abundant_item = item

    print(f"Item most abundant: potion with quantity {max_value}")
    print(f"Item least abundant: {least_abundant_item}"
          f" with quantity {quantity}")

    new_item.update({'magic_item': 1})
    print("Updated inventory: ", new_item)


if __name__ == "__main__":
    inventory_system()
