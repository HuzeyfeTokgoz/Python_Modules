import sys

def new_list(argv):
    i = 0
    list = []
    while i < len(argv):
        try:
           list += [int(argv[i])]
        except ValueError:
            print(f"Invalid parameter: '{argv[i]}'")
        i += 1
    return list

def score_analytics():
    print("=== Player Score Analytics ===")
    list = new_list(sys.argv[1:])

    if len(list) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
                " <score1> <score2> ...")
        return

    print(f"Scores processed: {list}")
    print(f"Total players: {len(list)}")
    print(f"Total score: {sum(list)}")
    print(f"Average score: {sum(list) / len(list):.1f}")
    print(f"High score: {max(list)}")
    print(f"Low score: {min(list)}")
    print(f"Score range: {max(list) - min(list)}")


if __name__ == "__main__":
    score_analytics()
