from collections import defaultdict


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def part1(input):
    lengths = [2, 4, 3, 7]
    counter = 0
    for line in input:
        end = line.split(" | ")[1].split(" ")
        for el in end:
            if len(el) in lengths:
                counter += 1
    return counter


def get_key_dict(left_elements):

    key_dict = defaultdict(str)
    for digit in left_elements:
        if len(digit) == 2:
            key_dict[1] = digit
        elif len(digit) == 4:
            key_dict[4] = digit
        elif len(digit) == 3:
            key_dict[7] = digit
        elif len(digit) == 7:
            key_dict[8] = digit

    for digit in left_elements:
        if len(digit) == 5:
            if len(set(digit).intersection(set(key_dict[1]))) == 2:
                key_dict[3] = digit
            elif len(set(digit).intersection(set(key_dict[4]))) == 3:
                key_dict[5] = digit
            else:
                key_dict[2] = digit
        elif len(digit) == 6:
            if len(set(digit).intersection(set(key_dict[4]))) == 4:
                key_dict[9] = digit
            elif len(set(digit).intersection(set(key_dict[1]))) == 1:
                key_dict[6] = digit
            else:
                key_dict[0] = digit

    return key_dict


def part2(input):
    numbers = list()
    for i, line in enumerate(input):
        start = line.split(" | ")[0].split(" ")
        end = line.split(" | ")[1].split(" ")
        key_dict = get_key_dict(start)
        number = ''
        for e in end:
            for key, digit in key_dict.items():
                if set(digit) == set(e):
                    number += str(key)
                    break
        numbers.append(number)
    return sum(list(map(int, numbers)))


if __name__ == '__main__':

    test = parse_input('day8_test')
    input = parse_input('day8')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
