"""
Part 1: No need to sort, just to check that for each number in the update the 
    greater numbers (values in the dict) are not one of the numbers to the left
Part 2: Didn't know how to do it without sorting. Used a trick that I saw on the reddit
    thread of using functools.cmp_to_key. I could have then changed part 1 to use this 
    function, but decided to leave it as it is to show my initial approach

"""

from typing import List
from collections import defaultdict
from functools import cmp_to_key

FILE_PATH = "day5_input.txt"


def is_valid(
    update: List,
    order: defaultdict,
) -> bool:
    for i, n in enumerate(update):
        if n not in order:
            continue
        left_ns = update[0:i]
        for n_left in left_ns:
            if n_left in order[n]:  # a number that should be at the right is at the left
                return False
    return True


def compare_func(order: defaultdict):
    def compare(a: int, b: int) -> int:
        """
        -1 (back in the list) if a is in the order dict in the left
            and b in the list of greater elements
        1 (forward) if b is in the order dict and
            a in the list of greater elements. b should come after a
        0 other cases
        """
        if a in order and b in order[a]:
            return -1
        elif b in order and a in order[b]:
            return 1
        else:
            return 0

    return compare


def main() -> None:
    total_part1 = 0
    total_part2 = 0
    order = defaultdict(list)
    compare_k = compare_func(order)

    updates = []
    with open(FILE_PATH) as f:
        p1, p2 = f.read().split("\n\n")
        for line in p1.splitlines():
            l, r = line.strip().split("|")
            order[int(l)].append(int(r))

        updates = [[int(n) for n in line.strip().split(",")] for line in p2.splitlines()]
    for update in updates:
        if is_valid(update, order):
            total_part1 += update[(len(update) // 2)]
        else:
            sorted_upd = sorted(update, key=cmp_to_key(compare_k))
            total_part2 += sorted_upd[(len(sorted_upd) // 2)]

    print(f"PART 1: {total_part1}")
    print(f"PART 2: {total_part2}")


if __name__ == "__main__":
    main()
