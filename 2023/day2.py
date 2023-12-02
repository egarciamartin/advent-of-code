from collections import defaultdict
from functools import reduce

game_conf = {
    "red":12,
    "green":13,
    "blue":14
}

def main():
    valid_games = []
    powers = []
    with open("day2_input.txt") as f:
        for id_, line in enumerate(f):
            line = line.replace(",","").replace(";","").strip().split(":")[1].split(" ")
            is_valid = True
            max_colors = defaultdict(int)
            for i, el in enumerate(line):
                if el in game_conf:
                    n = int(line[i-1])
                    if n > game_conf[el]:
                        is_valid=False
                    if n > max_colors[el]:
                        max_colors[el] = n
            powers.append(reduce(lambda x, y: x * y,  max_colors.values()))
            if is_valid:
                valid_games.append(id_ + 1)

        print(f"Part 1: {sum(valid_games)}") 
        print(f"Part 2: {sum(powers)}")


if __name__ == "__main__":
    main()
