import util


def part1(input):
    horizontal = 0
    depth = 0

    for move, n in input:
        n = int(n)
        if move == 'forward':
            horizontal += n
        elif move == 'down':
            depth += n
        elif move == 'up':
            depth -= n

    return horizontal * depth


def part2(input):
    horizontal = 0
    depth = 0
    aim = 0

    for move, n in input:
        n = int(n)
        if move == 'forward':
            horizontal += n
            depth += aim * n
        elif move == 'down':
            aim += n
        elif move == 'up':
            aim -= n

    return horizontal * depth


if __name__ == '__main__':

    # Inputs
    test = util.parse_input_split('day2_test')
    input = util.parse_input_split('day2')

    # Part 1
    print(f'Part 1: Test input: {part1(test)}')
    print(f'Part 1: Real input: {part1(input)}')

    # Part 2
    print(f'Part 2: Test input: {part2(test)}')
    print(f'Part 2: Real input: {part2(input)}')
