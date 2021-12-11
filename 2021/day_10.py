from collections import defaultdict
from collections import deque


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def part1(input):
    d = {'(': ')', '[': ']', '<': '>', '{': '}'}
    ds = {')': 3, ']': 57, '}': 1197, '>': 25137}
    corrupt_chars = list()
    for line in input:
        q = deque()
        for c in line:
            if c in d:
                q.append(c)
            elif d[q.pop()] != c:
                corrupt_chars.append(c)
                break

    return sum([ds[c] for c in corrupt_chars])


def part2(input):
    d = {'(': ')', '[': ']', '<': '>', '{': '}'}
    ds = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = list()
    for line in input:
        corrupt = False
        q = deque()
        for c in line:
            if c in d:
                q.append(c)
            elif d[q.pop()] != c:
                corrupt = True
                break
        if not corrupt:
            lc = [d[i] for i in list(reversed(q))]
            score = 0
            for item in lc:
                score = score * 5 + ds[item]
            scores.append(score)

    t = sorted(scores, reverse=True)
    return t[len(t)//2]


if __name__ == '__main__':

    test = parse_input('day10_test')
    input = parse_input('day10')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
