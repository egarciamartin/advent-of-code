from functools import reduce
from collections import defaultdict


def main():
    points_part1 = 0
    card_copies = defaultdict(int)
    with open("day4_input.txt") as f:
        for card, line in enumerate(f):
            card_copies[card] += 1
            l = line.strip().split(": ")[1].split(" | ")
            winning = list(map(int, l[0].split()))
            my_numbers = list(map(int, l[1].split()))
            n_wins = sum(1 for n in my_numbers if n in winning)
            if n_wins > 1:
                points_part1 += reduce(lambda x, _: x * 2, range(n_wins - 1), 1)
            elif n_wins == 1:
                points_part1 += 1
            for i in range(n_wins):
                card_copies[card + i + 1] += 1 * card_copies[card]

    print(f"Part 1: {points_part1}")
    print(f"Part 2: {sum(card_copies.values())}")


if __name__ == "__main__":
    main()
