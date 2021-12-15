from collections import defaultdict
from typing import Tuple
from queue import PriorityQueue
from copy import copy


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines if line != "\n"]
    return input


def get_cave_map(input):
    cave_map = defaultdict(int)
    for i, line in enumerate(input):
        for j, risk in enumerate(line):
            cave_map[(i, j)] = int(risk)
    return cave_map


def get_neighbors(point, grid_size):
    """
    Not diagonally

    """
    neighbors = list()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for d in directions:
        cand = tuple(sum(x) for x in zip(point, d))
        if cand[0] >= 0 and cand[1] >= 0 and cand[0] <= (grid_size[0] - 1) and cand[1] <= (grid_size[1]-1):
            neighbors.append(cand)

    return neighbors


def dijkstra(max_coordinate, grid_size, cave_map):
    """"
    Dijkstra with priority queues. 
    From: https://www.redblobgames.com/pathfinding/a-star/implementation.html#python-dijkstra 
    """
    q = PriorityQueue()
    q.put((0, (0, 0)))
    came_from = defaultdict(Tuple)
    cost_so_far = defaultdict(int)
    came_from[(0, 0)] = None
    cost_so_far[(0, 0)] = 0

    while q:
        current = q.get()[1]
        if current == max_coordinate:
            break
        for next in get_neighbors(current, grid_size):
            new_cost = cost_so_far[current] + cave_map[next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                q.put((new_cost, next))
                came_from[next] = current
    return cost_so_far[max_coordinate]


def part1(input):

    cave_map = get_cave_map(input)
    max_coordinate = max(cave_map.keys())
    grid_size = (max_coordinate[0] + 1, max_coordinate[1]+1)
    cost = dijkstra(max_coordinate, grid_size, cave_map)

    return cost


def get_new_map(cave_map, grid_size):
    new_map = defaultdict(int)
    for k, v in cave_map.items():
        for incr_x in range(5):
            for incr_y in range(5):
                new_k = (k[0] + (grid_size[0] * incr_x),
                         k[1] + (grid_size[1] * incr_y))
                new_v = v + incr_x + incr_y
                if new_v > 9:
                    new_v = new_v % 9
                new_map[new_k] = new_v
    return new_map


def part2(input):
    old_cave_map = get_cave_map(input)

    old_max_coordinate = max(old_cave_map.keys())
    old_grid_size = (old_max_coordinate[0] + 1, old_max_coordinate[1]+1)
    cave_map = get_new_map(old_cave_map, old_grid_size)

    max_coordinate = max(cave_map.keys())
    grid_size = (max_coordinate[0] + 1, max_coordinate[1]+1)
    cost = dijkstra(max_coordinate, grid_size, cave_map)

    return cost


if __name__ == '__main__':

    test = parse_input('day15_test')
    input = parse_input('day15')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
