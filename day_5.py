import numpy as np


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
        input = [line.split(" -> ") for line in input]
        input_tup = [[tuple(map(int, el.split(',')))
                      for el in line] for line in input]
    return input_tup


def get_grid_size(input):
    max_ = max(max(max(input)))
    return (max_+1, max_+1)


def get_points(p1, p2):
    points = [p1]
    point = p1
    while point != p2:
        x = 1 if p1[0] < p2[0] else 0 if p1[0] == p2[0] else -1
        y = 1 if p1[1] < p2[1] else 0 if p1[1] == p2[1] else -1
        point = (point[0] + x, point[1] + y)
        points.append(point)
    return points


def sum_points(input, part2=False):
    size = get_grid_size(input)
    grid = np.zeros(size)

    for (x1, y1), (x2, y2) in input:
        if (x1 == x2 or y1 == y2) or part2:
            points = get_points((x1, y1), (x2, y2))
            for i in points:
                grid[i[1], i[0]] += 1

    return np.sum(grid[:, :] >= 2)


if __name__ == '__main__':

    test = parse_input('day5_test')
    input = parse_input('day5')

    print(f"Part 1: Test: {sum_points(test)}")
    print(f"Part 1: Real: {sum_points(input)}")

    print(f"Part 2: Test: {sum_points(test, part2=True)}")
    print(f"Part 2: Real: {sum_points(input, part2=True)}")
