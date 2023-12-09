from functools import reduce
from itertools import pairwise


def main():
    part1_sum = 0
    part2_sum = 0
    with open("day9_input.txt") as f:
        for line in f:
            history = list(map(int, line.strip().split()))
            last_history = [history[-1]]
            first_history = [history[0]]
            while len(set(history)) > 1:
                history = [y - x for x, y in pairwise(history)]
                last_history.append(history[-1])
                first_history.append(history[0])
            part1_sum += sum(last_history)
            part2_sum += reduce(lambda x, y: y - x, reversed(first_history))

    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")


if __name__ == "__main__":
    main()
