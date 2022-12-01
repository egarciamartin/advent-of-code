from collections import defaultdict
from typing import Tuple
from queue import PriorityQueue
from copy import copy


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readline()
    return lines


def part1(input):
    """
    T = 4, no subpackets, literal
    T != 4, subpackets

    110 100 0 1010  |  010 100 1 0001 0 0000
    """
    packets = list()
    versions = list()
    literals = list()
    b = bin(int(input, 16))[2:]
    print(b)
    packets.append(b)
    while packets:
        p = packets.pop()
        v = int(p[0:3], 2)
        t = int(p[3:6], 2)
        versions.append(v)
        if t == 4:  # literal
            nxt = p[6]
            literals.append(int(p[7:11], 2))
            c = 11
            while nxt != 0:
                nxt = p[c]
                literals.append(int(p[c+1:c+1+5], 2))
                c += 5

            # if there is still left. append to packets
            if len(p) > (c+3):
                packets.append(p[c:])

        else:
            lid = p[6]
            if lid == 0:
                l = int(p[7:22], 2)
                packets.append(p[22:22+l])
            else:
                ns = int(p[7:18], 2)

    print(v, t)

    return


def part2(input):

    return


if __name__ == '__main__':

    test = parse_input('day16_test')
    input = parse_input('day16')

    print(test)

    print(f"Part 1: Test: {part1(test)}")
    # print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
