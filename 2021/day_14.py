from collections import Counter, defaultdict
from copy import copy
from math import ceil


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines if line != "\n"]
    return input


def part1(input):
    template = input[0]
    rules = {line.split(" -> ")[0]: line.split(" -> ")[1]
             for line in input[1:]}

    steps = 10
    polymer = template
    for _ in range(steps):
        new_polymer = list()
        for i in range(len(polymer)-1):
            pair = polymer[i] + polymer[i+1]
            new_polymer.append(polymer[i])
            if pair in rules:
                new_polymer.append(rules[pair])
        new_polymer.append(polymer[-1])
        polymer = new_polymer

    cnt = Counter(polymer)
    return cnt.most_common()[0][1] - cnt.most_common()[-1][1]


def part2(input):
    template = input[0]
    rules = {line.split(" -> ")[0]: line.split(" -> ")[1]
             for line in input[1:]}

    cnt = Counter(template)
    pairs = defaultdict(int)
    for i in range(len(template)-1):
        pair = template[i] + template[i+1]
        pairs[pair] += 1

    steps = 40
    for _ in range(steps):
        new_pairs = defaultdict(int)
        for pair, n in pairs.items():
            if pair in rules:
                r = rules[pair]
                new_pairs[pair[0] + r] += n
                new_pairs[r + pair[1]] += n
                cnt[r] += n
            else:
                continue

        pairs = copy(new_pairs)
    return cnt.most_common()[0][1] - cnt.most_common()[-1][1]


if __name__ == '__main__':

    test = parse_input('day14_test')
    input = parse_input('day14')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
