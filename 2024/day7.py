from typing import List, Tuple
import itertools
from operator import add, mul

FILE_PATH = "day7_input.txt"
concat = lambda a, b: int(f"{a}{b}")


def is_valid(test: int, values: List, operators: Tuple) -> bool:
    combinations = itertools.product(operators, repeat=len(values) - 1)
    for combi in combinations:
        total = values[0]
        for v, op in zip(values[1:], combi):
            total = op(total, v)
        if total == test:
            return True
    return False


def main() -> None:
    total_part1 = 0
    total_part2 = 0

    for line in open(FILE_PATH):
        test, values = line.strip().split(": ")
        test, values = int(test), list(map(int, values.split()))
        if is_valid(test, values, (add, mul)):
            total_part1 += test
        if is_valid(test, values, (add, mul, concat)):
            total_part2 += test

    print(f"PART 1: {total_part1}")
    print(f"PART 2: {total_part2}")


if __name__ == "__main__":
    main()
