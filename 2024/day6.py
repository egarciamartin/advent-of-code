from typing import Tuple, List
from itertools import cycle

FILEPATH = "day6_input.txt"
directions = cycle(["up", "right", "down", "left"])
dir_d = {"up": (-1, 0), "right": (0, +1), "down": (1, 0), "left": (0, -1)}


def main() -> None:
    obstacles = []
    with open(FILEPATH) as f:
        lines = list(map(lambda l: l.strip(), f))
        max_c = (len(lines), len(lines[0]))
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == "^":
                    guard_pos = (i, j)
                elif c == "#":
                    obstacles.append((i, j))
    dist_positions = {guard_pos}
    direction = next(directions)
    has_exit = False
    while not has_exit:
        while True:
            next_pos = (
                guard_pos[0] + dir_d[direction][0],
                guard_pos[1] + dir_d[direction][1],
            )
            if next_pos in obstacles:
                direction = next(directions)
                break
            if (
                next_pos[0] >= max_c[0]
                or next_pos[1] >= max_c[1]
                or next_pos[0] < 0
                or next_pos[1] < 0
            ):
                has_exit = True
                break
            guard_pos = next_pos
            dist_positions.add(guard_pos)

    print(f"PART 1: {len(dist_positions)}")


if __name__ == "__main__":
    main()
