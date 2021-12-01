def part1(l):
    counter = 0
    for i, item in enumerate(l):
        if i == 0:
            prev = item
            continue
        if item > prev:
            counter += 1
        prev = item
    print(counter)


def part2(l):
    """
    Sliding window of 3, sum and compare.
    """
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
    print(counter)


# Test input
test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
print('Part 1: Test input')
part1(test)

# Read input
with open('input.txt') as file:
    lines = file.readlines()
    input = [int(line.rstrip()) for line in lines]

# Part 1
print('Part 1: Real input')
part1(input)

# Part 2
print('Part 2: Test input')
part2(test)
print('Part 2: Real input')
part2(input)
