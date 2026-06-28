#!/usr/bin/env python3
import sys
import typing


def archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file}'")
    try:
        open_file: typing.IO[str] = open(file, "r")
        read_file: str = open_file.read()
        open_file.close()

        print("---\n")
        print(read_file)
        print("\n---")
        print(f"File '{file}' closed.\n")

        new_line_file: list[str] = []
        read_line_file: list[str] = read_file.split('\n')
        for line in read_line_file:
            line += '#\n'
            new_line_file.append(line)

        print("Transform data:")
        print("---\n")
        for lines in new_line_file:
            print(lines, end="")
        print("\n---")

    except Exception as e:
        print(f"Error opening file '{file}': {e}")
        return

    new_file = input("Enter new file name (or empty): ")
    if new_file:
        print(f"Saving data to '{new_file}'")

        new_open_file: typing.IO[str] = open(new_file, "w")
        for line in new_line_file:
            new_open_file.write(line)
        new_open_file.close()

        print(f"Data saved in file '{new_file}'.")
    else:
        print("Not saving data.")
        return


if __name__ == "__main__":
    archive_creation()
