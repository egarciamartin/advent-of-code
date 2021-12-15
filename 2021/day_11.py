from collections import defaultdict
from collections import deque


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def get_octupus_map(input):
    octopus_map = defaultdict(int)
    for i, line in enumerate(input):
        for j, energy in enumerate(line):
            octopus_map[(i, j)] = int(energy)
    return octopus_map


def get_neighbors(point):
    """
    Diagonals also

    """
    grid_size = (10, 10)
    neighbors = list()
    directions = [(0, 1), (0, -1), (1, 0), (1, 1),
                  (1, -1), (-1, 0), (-1, 1), (-1, -1)]

    for d in directions:
        cand = tuple(sum(x) for x in zip(point, d))
        if cand[0] >= 0 and cand[1] >= 0 and cand[0] <= (grid_size[0] - 1) and cand[1] <= (grid_size[1]-1):
            neighbors.append(cand)

    return neighbors


def part1(input):
    steps = 100
    octo_map = get_octupus_map(input)
    nflashes = 0
    for _ in range(steps):
        octo_left = deque()
        flashing = set()
        for k, v in octo_map.items():
            octo_map[k] += 1
            if octo_map[k] > 9:
                octo_left.append(k)
                flashing.add(k)
        while octo_left:
            current = octo_left.pop()
            ns = get_neighbors(current)
            for nb in ns:
                if nb in flashing:
                    continue
                octo_map[nb] += 1
                if (octo_map[nb] > 9):
                    octo_left.append(nb)
                    flashing.add(nb)
        for p in flashing:
            octo_map[p] = 0
            nflashes += 1
    return nflashes


def part2(input):
    step = 0
    octo_map = get_octupus_map(input)
    simult = False
    while(simult == False):
        octo_left = deque()
        flashing = set()
        for k, v in octo_map.items():
            octo_map[k] += 1
            if octo_map[k] > 9:
                octo_left.append(k)
                flashing.add(k)
        while octo_left:
            current = octo_left.pop()
            ns = get_neighbors(current)
            for nb in ns:
                if nb in flashing:
                    continue
                octo_map[nb] += 1
                if (octo_map[nb] > 9):
                    octo_left.append(nb)
                    flashing.add(nb)
        for p in flashing:
            octo_map[p] = 0
        init_v = octo_map[(0, 0)]
        simult = all([v == init_v for v in octo_map.values()])
        step += 1
    return step


if __name__ == '__main__':

    test = parse_input('day11_test')
    input = parse_input('day11')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
