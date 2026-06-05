#!/usr/bin/env python3
import random


def gen_player_achievements() -> set[str]:

    lst = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
           'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
           'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
           'Boss Slayer']

    adet = random.randint(5, 9)
    select_lst = random.sample(lst, adet)

    return set(select_lst)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    lst_union = set.union(alice, bob, charlie, dylan)
    lst_intersection = set.intersection(alice, bob, charlie, dylan)

    print(f"\nAll distinct achievements: {lst_union}")
    print(f"\nCommon achievements: {lst_intersection}")

    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")

    print(f"\nAlice is missing: {lst_union.difference(alice)}")
    print(f"Bob is missing: {lst_union.difference(bob)}")
    print(f"Charlie is missing: {lst_union.difference(charlie)}")
    print(f"Dylan is missing: {lst_union.difference(dylan)}")
