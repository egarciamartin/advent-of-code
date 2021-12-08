import numpy as np


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [(line.strip()) for line in lines]
    return input


def part1(input):
    input = np.array([list(number) for number in input]).astype(int)
    sums = np.sum(input, axis=0)
    gamma = ''
    epsilon = ''
    half = input.shape[0] // 2

    for el in sums:
        if int(el) > half:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    power = int(gamma, 2) * int(epsilon, 2)
    return power


def get_ratings(input, zero_order=[0, 1]):
    rating = input
    bit = 0

    while len(rating) > 1:
        sums = np.sum(rating, axis=0)
        zero_or_one = zero_order[0]
        if (sums[bit] * 2) >= (len(rating)):
            zero_or_one = zero_order[1]
        mask = (rating[:, bit] == zero_or_one)
        rating = rating[mask, :]
        bit += 1

    rating = rating[0, :].tolist()
    rating = [str(i) for i in rating]
    rating = "".join(rating)
    return rating


def part2(input):
    input = np.array([list(number) for number in input]).astype(int)
    ogr = get_ratings(input, zero_order=[0, 1])
    co2_sr = get_ratings(input, zero_order=[1, 0])
    lsr = int(ogr, 2) * int(co2_sr, 2)
    return lsr


if __name__ == '__main__':

    # Inputs
    test = parse_input('day3_test')
    input = parse_input('day3')

    # Part 1
    print(f'Part 1: Test input: {part1(test)}')
    print(f'Part 1: Real input: {part1(input)}')

    # Part 2
    print(f'Part 2: Test input: {part2(test)}')
    print(f'Part 2: Real input: {part2(input)}')
