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


def count(input, days):
    d = defaultdict(int)
    for i in input:
        d[i] = d[i] + 1

    for day in range(days):
        new_d = defaultdict(int)
        for k, v in d.items():
            if k == 0:
                new_d[6] += v
                new_d[8] += v
            else:
                new_d[k-1] += v

        d = new_d

    return sum(d.values())


if __name__ == '__main__':

    test = parse_input('day6_test')
    input = parse_input('day6')

    print(f"Part 1: Test: {count(test, 80)}")
    print(f"Part 1: Real: {count(input, 80)}")

    print(f"Part 2: Test: {count(test, 256)}")
    print(f"Part 2: Real: {count(input, 256)}")
