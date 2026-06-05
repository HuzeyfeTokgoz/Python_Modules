import math


def coordinate():
    while True:
        try:
            new_coordinate = input("Enter new coordinates as "
                                   "floats in format 'x,y,z': ")
            value = new_coordinate.split(",")

            if len(value) != 3:
                print("Invalid syntax")
                continue
            tuples = (float(value[0]), float(value[1]), float(value[2]))
            return tuples
        except ValueError as e:
            print(f"Error on parameter: {e}")


def get_player_pos() -> None:
    try:
        print("=== Game Coordinate System ===")
        print("\nGet a first set of coordinates")
        input_coordinate1 = coordinate()
        x1 = input_coordinate1[0]
        y1 = input_coordinate1[1]
        z1 = input_coordinate1[2]

        print(f"Got a first tuple: {input_coordinate1}")
        print(f"It includes: X={x1}, Y={y1}, Z={z1}")
        center_distance = math.sqrt((x1 - 0)**2 + (y1 - 0)**2 + (z1 - 0)**2)
        print(f"Distance to center: {round(center_distance, 4)}")

        print("\nGet a second set of coordinates")
        input_coordinate2 = coordinate()
        x2 = input_coordinate2[0]
        y2 = input_coordinate2[1]
        z2 = input_coordinate2[2]
        between_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1)**2)
        print("Distance between the 2 sets of coordinates: "
              f"{round(between_distance, 4)}")

    except ValueError as e:
        print(f"Error on parameter: {e}")


if __name__ == "__main__":
    get_player_pos()
