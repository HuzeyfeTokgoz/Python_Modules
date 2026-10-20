#!/usr/bin/env python3
import sys


def new_list(argv: list[str]) -> list[int]:
    i = 0
    score = []
    while i < len(argv):
        try:
            score += [int(argv[i])]
        except ValueError:
            print(f"Invalid parameter: '{argv[i]}'")
        i += 1
    return score


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    lst: list[int] = new_list(sys.argv[1:])

    if len(lst) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    print(f"Scores processed: {lst}")
    print(f"Total players: {len(lst)}")
    print(f"Total score: {sum(lst)}")
    print(f"Average score: {sum(lst) / len(lst):.1f}")
    print(f"High score: {max(lst)}")
    print(f"Low score: {min(lst)}")
    print(f"Score range: {max(lst) - min(lst)}")


if __name__ == "__main__":
    score_analytics()
