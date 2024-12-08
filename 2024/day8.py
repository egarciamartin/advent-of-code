from collections import defaultdict
from itertools import combinations
from typing import Tuple, Set

FILEPATH = "day8_input.txt"
grid_inv = defaultdict(list)


def is_inside_grid(point: Tuple, max_coodinates: Tuple) -> bool:
    if (
        point[0] >= 0
        and point[0] < max_coodinates[0]
        and point[1] >= 0
        and point[1] < max_coodinates[1]
    ):
        return True
    return False


def calculate_antinodes(grid: defaultdict, max_c: Tuple, part="part1") -> Set:
    """
    grid = {"O" : [(1,0), (2,2)]}
    """

    s = set()
    for _, locs in grid.items():
        if not len(locs) >= 1:
            continue
        if part == "part2":
            s.update(locs)
        for p1, p2 in combinations(locs, 2):
            diff = (p2[0] - p1[0], p2[1] - p1[1])
            for direction in [-1, 1]:
                i = 1
                while True:
                    p_next = (
                        (p1[0] + direction * diff[0] * i, p1[1] + direction * diff[1] * i)
                        if direction == -1
                        else (
                            p2[0] + direction * diff[0] * i,
                            p2[1] + direction * diff[1] * i,
                        )
                    )
                    if is_inside_grid(p_next, max_c):
                        s.add(p_next)
                    else:
                        break
                    if part == "part1":
                        break
                    i += 1
    return s


def main() -> None:
    with open(FILEPATH) as f:
        lines = list(map(lambda l: l.strip(), f))
        max_coordinates = (len(lines[0]), len(lines))
    for i, l1 in enumerate(lines):
        for j, c in enumerate(l1):
            if c != ".":
                grid_inv[c].append((i, j))
    print(f'PART 1: {len(calculate_antinodes(grid_inv, max_coordinates, "part1"))}')
    print(f'PART 2: {len(calculate_antinodes(grid_inv, max_coordinates, "part2"))}')


if __name__ == "__main__":
    main()
