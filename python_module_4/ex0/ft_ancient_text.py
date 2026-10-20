#!/usr/bin/env python3
import sys
import typing


def ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file}'")
    try:
        open_file: typing.IO[str] = open(file, "r")
        read_file: str = open_file.read()
        print("---")
        print(read_file)
        print("---")

    except Exception as e:
        print(f"Error opening file '{file}': {e}")

    else:
        open_file.close()
        print(f"File '{file}' closed.")


if __name__ == "__main__":
    ancient_text()
