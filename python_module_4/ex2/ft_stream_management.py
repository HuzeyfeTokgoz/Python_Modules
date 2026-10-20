#!/usr/bin/env python3
import sys
import typing


def archive_creation() -> None:
    if len(sys.argv) != 2:
        print("[STDERR] Usage: ft_ancient_text.py <file>", file=sys.stderr)
        return

    file: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file}'")
    try:
        open_file: typing.IO[str] = open(file, "r")
        read_file: str = open_file.read()
        open_file.close()

        print("---")
        print(read_file)
        print("---")
        print(f"File '{file}' closed.\n")

        new_line_file: list[str] = []
        read_line_file: list[str] = read_file.split('\n')
        for line in read_line_file:
            line += '#\n'
            new_line_file.append(line)

        print("Transform data:")
        print("---")
        for lines in new_line_file:
            print(lines, end="")
        print("---")

    except Exception as e:
        print(f"[STDERR] Error opening file '{file}': {e}", file=sys.stderr)
        return

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip('\n')

    if new_file:
        print(f"Saving data to '{new_file}'")
        try:
            new_open_file: typing.IO[str] = open(new_file, "w")
            for line in new_line_file:
                new_open_file.write(line)
            new_open_file.close()
            print(f"Data saved in file '{new_file}'.")

        except Exception as e:
            print(f"[STDERR] Error opening file \
                  '{new_file}': {e}", file=sys.stderr)
            print("Data not saved.")
            return
    else:
        print("Not saving data.")
        return


if __name__ == "__main__":
    archive_creation()
