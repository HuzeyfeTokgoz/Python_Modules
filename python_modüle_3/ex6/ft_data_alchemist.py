#!/usr/bin/env python3
import random
from typing import Dict


def data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")

    player_list: list[str] = ['Alice', 'bob', 'Charlie', 'dylan',
                              'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print("Initial list of players:", player_list)

    new_player_list: list[str] = [i.capitalize() for i in player_list]
    print("New list with all names capitalized:", new_player_list)

    is_cap_player_list: list[str] = \
        [player for player in player_list if player[0].isupper()]
    print("New list of capitalized names only:", is_cap_player_list)

    new_player_dict: Dict[str, int] = \
        {player: random.randint(1, 999) for player in new_player_list}
    print("Score dict:", new_player_dict)

    average = sum(new_player_dict.values()) / len(new_player_dict)
    print("Score average is", round(average, 2))

    high_score: Dict[str, int] = {i: new_player_dict[i]
                                  for i in new_player_dict
                                  if new_player_dict[i] > average}
    print("High Scores:", high_score)


if __name__ == "__main__":
    data_alchemist()
