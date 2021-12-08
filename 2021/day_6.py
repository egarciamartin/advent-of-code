from collections import defaultdict
import copy


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = lines[0].strip().split(",")
        input = [int(i) for i in input]
    return input


def count(input, days):
    """
    Two dicts, to save the new information on the new_d
    without overwritting the orginal one: d

    Note-to-self: new_d[timer-1] += n and not just =n 
    in case we have already moved one of the other values (e.g. if we already have 
    moved a count of 2 from 7 to 6)
    """
    d = defaultdict(int)
    for i in input:
        d[i] += 1

    for day in range(days):
        new_d = defaultdict(int)
        for timer, n in d.items():
            if timer == 0:
                new_d[6] += n
                new_d[8] += n
            else:
                new_d[timer-1] += n
        d = new_d

    return sum(d.values())


def part1(input):
    return count(input, 80)


def part2(input):
    return count(input, 256)


if __name__ == '__main__':

    test = parse_input('day6_test')
    input = parse_input('day6')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f"Part 2: Test: {count(test)}")
    print(f"Part 2: Real: {count(input)}")
