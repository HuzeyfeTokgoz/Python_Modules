#!/usr/bin/env python3
import random
from typing import Generator, Tuple


def gen_event() -> Generator[Tuple[str, str], None, None]:
    name_lst = ["alice", "bob", "charlie", "dylan"]
    action_lst = ["run", "eat", "sleep", "grab", "move",
                  "climb", "swim", "release"]
    while True:
        name = random.choice(name_lst)
        action = random.choice(action_lst)
        yield (name, action)


def consume_event(event_lst: list[Tuple[str, str]]) \
                    -> Generator[Tuple[str, str], None, None]:

    while event_lst:
        remove_lst = random.choice(event_lst)
        event_lst.remove(remove_lst)
        yield remove_lst


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    event_stream = gen_event()
    event_list = []
    for i in range(1000):
        event_name, event_action = next(event_stream)
        print(f"Event {i}: Player {event_name} did action {event_action}")
    for _ in range(10):
        event_tuple = next(event_stream)
        event_list.append(event_tuple)
    print(f"\nBuilt list of 10 events: {event_list}\n")
    for remove_list in consume_event(event_list):
        print(f"Got event from list: {remove_list}")
        print(f"Remains in list: {event_list}\n")
