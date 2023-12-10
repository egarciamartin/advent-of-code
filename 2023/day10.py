from collections import defaultdict, deque
from typing import Tuple, List

pipe_map = defaultdict(str)
#  S = J


def get_neighbors(coord: Tuple) -> List:
    """
    There's only two neighbors available,
    and it depends on the pipe
    """
    pipe = pipe_map[coord]
    if pipe == "|":
        return [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1])]
    elif pipe == "-":
        return [(coord[0], coord[1] - 1), (coord[0], coord[1] + 1)]
    elif pipe == "L":
        return [(coord[0] - 1, coord[1]), (coord[0], coord[1] + 1)]
    elif pipe == "J":
        return [(coord[0], coord[1] - 1), (coord[0] - 1, coord[1])]
    elif pipe == "7":
        return [(coord[0], coord[1] - 1), (coord[0] + 1, coord[1])]
    elif pipe == "F":
        return [(coord[0] + 1, coord[1]), (coord[0], coord[1] + 1)]
    elif pipe == "S":
        # J for the input. Hardcoding it
        return [(coord[0], coord[1] - 1), (coord[0] - 1, coord[1])]
    else:
        raise ValueError(f"Pipe {pipe} not in list, error in reading input")


def bfs(start: Tuple, end: Tuple) -> int:
    """
    Reasoning: the start will have two paths,
    it doesn't matter which one we take since it's
    a loop. To not make a double loop, focus only on one of them
    """
    visited = set()
    first_neighbors = get_neighbors(start)

    q = deque([first_neighbors[0]])
    visited.add(start)
    visited.add(first_neighbors[0])

    steps = 1
    while q:
        current = q.popleft()
        neighbors = get_neighbors(current)

        for neighbor in neighbors:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
        steps += 1
    return steps


def main():
    with open("day10_input.txt") as f:
        for row, line in enumerate(f):
            for col, c in enumerate(line):
                pipe_map[(row, col)] = c
                if c == "S":
                    start = (row, col)

    steps = bfs(start, start)

    print(f"Part 1: {steps // 2}")
    # print(f"Part 2: {part2_sum}")


if __name__ == "__main__":
    main()
