from collections import defaultdict
import copy


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = lines[0].strip().split(",")
        input = [int(i) for i in input]
    return input


def count_slow(input, days):
    timers = copy.copy(input)

    for day in range(days):
        new = 0
        for i, timer in enumerate(timers):
            if timer > 0:
                timers[i] -= 1
            else:
                timers[i] = 6
                new += 1
        for _ in range(new):
            timers.append(8)
    return len(timers)


def count_list(input, days):
    """
    Practice purposes. 
    Same as the hashmap but with two lists
    """
    counts = [0 for i in range(9)]
    for item in input:
        counts[item] += 1

    for day in range(days):
        temp = [0 for i in range(9)]
        for i, item in enumerate(counts):
            if i == 0 and item > 0:
                temp[6] += item
                temp[8] += item
            else:
                temp[i-1] += item

        counts = temp
    return sum(counts)


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


if __name__ == '__main__':

    test = parse_input('day6_test')
    input = parse_input('day6')

    print(f"Part 1: Test: {count(test, 80)}")
    print(f"Part 1: Real: {count(input, 80)}")

    print(f"Part 2: Test: {count(test, 256)}")
    print(f"Part 2: Real: {count(input, 256)}")
