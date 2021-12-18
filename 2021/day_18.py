from collections import defaultdict
from typing import Tuple
from queue import PriorityQueue
from copy import copy


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines if line != "\n"]
    return input


def part1(input):

    return


def part2(input):

    return


if __name__ == '__main__':

    test = parse_input('day17_test')
    input = parse_input('day17')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
