import util


def part1(l):
    counter = 0
    for i, item in enumerate(l):
        if i == 0:
            prev = item
            continue
        if item > prev:
            counter += 1
        prev = item
    return counter


def part2(l):
    counter = 0
    window = 3
    i = 0
    while ((i + window) <= len(l)):
        sum_window = l[i] + l[i+1] + l[i+2]
        if i == 0:
            sum_prev = sum_window
            i += 1
            continue

        if sum_window > sum_prev:
            counter += 1

        sum_prev = sum_window
        i += 1
    return counter


# Inputs
test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input = util.parse_input('day1')


# Part 1
print(f'Part 1: Test input -- {part1(test)}')
print(f'Part 1: Real input -- {part1(input)}')

# Part 2
print(f'Part 2: Test input -- {part2(test)}')
print(f'Part 2: Real input -- {part2(input)}')
