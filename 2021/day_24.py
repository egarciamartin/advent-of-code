def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def get_check_offset(input):
    """
    Lines for check: 5 
    Line for offset: 15
    """
    check = []
    offset = []
    for line in input:
        if line.split(" ")[0] == "inp":
            i = 0
        if i == 5:
            check.append(int(line.split(" ")[2]))
        elif i == 15:
            offset.append(int(line.split(" ")[2]))
        i += 1
    return check, offset


def alu(check, offset, largest=True):
    """
    From: https://github.com/kemmel-dev/AdventOfCode2021/blob/master/day24/AoC%20Day%2024.pdf

    Once we figure out that we have a stack structure as z, there is one key step.
    If we want z=0 in the last step, the stack must be empty. 
    That means that we want the same number of push and pop. 

    This results in:

    if CHECK > 0:
        stack.push(w + OFFSET)
    else:
        v = stack.pop()
        if (v + CHECk != w):
            stack.push(w + OFFSET)

    Thus, we want the last condition to never be true, making v + CHECK == w, and 
    with that we get the different w. 

    Pairs that map which digits should be equal with a different of pair_offset
    (for each pop push pair). 
    To get the largest: 9 in the left for positive offsets, 9 in the right otherwise.
    To get the smallest: 1 in the left for negative offsets, 1 in the right otherwise.
    Very ad-hoc, same as doing it by hand.

    """

    pairs = []
    stack = []
    pair_offset = []
    digit = ["0"] * 14

    for step in range(14):
        if check[step] > 0:
            stack.append((step, offset[step]))
        else:
            (s_, o_) = stack.pop()
            pairs.append((step, s_))
            pair_offset.append(o_ + check[step])

    for i, off in enumerate(pair_offset):
        if largest:
            if off > 0:
                digit[pairs[i][0]] = "9"
                digit[pairs[i][1]] = str(9 - off)
            else:
                digit[pairs[i][1]] = "9"
                digit[pairs[i][0]] = str(9 + off)
        else:
            if off > 0:
                digit[pairs[i][1]] = "1"
                digit[pairs[i][0]] = str(1 + off)
            else:
                digit[pairs[i][0]] = "1"
                digit[pairs[i][1]] = str(1 - off)

    return int("".join(digit))


def part1(input):
    check, offset = get_check_offset(input)
    digit = alu(check, offset, largest=True)
    return digit


def part2(input):
    check, offset = get_check_offset(input)
    digit = alu(check, offset, largest=False)
    return digit


if __name__ == '__main__':

    test = parse_input('day24_test')
    input = parse_input('day24')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
