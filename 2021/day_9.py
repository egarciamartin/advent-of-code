from collections import defaultdict
from collections import deque


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def get_height_map(input):
    height_map = defaultdict(int)
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            height_map[(i, j)] = int(col)
    return height_map


def get_neighbors(point, grid_size):
    """
    Only up, down, left, right
    If it would be with diagonals:
    directions_all = [(0, 1), (0, -1), (1, 0), (1, 1),
                      (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    """
    neighbors = list()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for d in directions:
        cand = tuple(sum(x) for x in zip(point, d))
        if cand[0] >= 0 and cand[1] >= 0 and cand[0] <= (grid_size[0] - 1) and cand[1] <= (grid_size[1]-1):
            neighbors.append(cand)

    return neighbors


def get_low_points(height_map, grid_size):
    risk = 0
    low_points = defaultdict(int)
    for point, v in height_map.items():
        neighbors = get_neighbors(point, grid_size)
        lower = [True if height_map[p] > v else False for p in neighbors]
        if all(lower):
            risk += v + 1
            low_points[point] = v

    return risk, low_points


def part1(input):
    grid_size = (len(input), len(input[0]))
    height_map = get_height_map(input)
    risk, low_points = get_low_points(height_map, grid_size)

    return risk


def part2(input):
    """
    BFS algoritm
    https://www.redblobgames.com/pathfinding/a-star/introduction.html#breadth-first-search 
    Tip from @javitronxo
    """
    grid_size = (len(input), len(input[0]))
    height_map = get_height_map(input)
    _, low_points = get_low_points(height_map, grid_size)
    basins = list()
    for coordinate, v in low_points.items():
        frontier = deque()
        frontier.append(coordinate)
        came_from = dict()
        came_from[coordinate] = None
        while frontier:
            current = frontier.pop()
            for next in get_neighbors(current, grid_size):
                if next not in came_from and height_map[next] != 9:
                    frontier.append(next)
                    came_from[next] = current
        basins.append(len(came_from))

    result = 1
    for basin in sorted(basins, reverse=True)[0:3]:
        result *= basin

    return result


if __name__ == '__main__':

    test = parse_input('day9_test')
    input = parse_input('day9')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
