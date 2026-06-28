#!/usr/bin/env python3
from typing import Tuple


def secure_archive(file: str, mode: str = "read",
                   content: str = "") -> Tuple[bool, str]:
    try:
        if mode == "read":
            with open(file, "r") as f:
                open_file = f.read()
            return (True, open_file)

        elif mode == "write":
            with open(file, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid mode")

    except Exception as e:
        file_tuple = (False, str(e))
        return file_tuple


if __name__ == "__main__":
    test1 = secure_archive('/not/existing/file', "read")
    test2 = secure_archive('a', "read")
    test3 = secure_archive('./ft_vault_security.py', "read")
    test4 = secure_archive('b', "write", "test metni")

    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(test1)
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(test2)
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(test3)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(test4)
