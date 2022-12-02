DAY = 2

score_chart = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

win_action = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}


def read_input(file):
    with open(file) as f:
        guide = f.readlines()
        guide = [line.strip() for line in guide]
        guide = [(line.split(" ")[0], line.split(" ")[1])for line in guide]
        return guide


def part1(guide):
    score = 0
    for (elf, coder) in guide:
        elf_win = win_action[elf]
        # win
        if elf_win == coder:
            score += 6
        elif score_chart[elf] == score_chart[coder]:
            score += 3  # draw

        score += score_chart[coder]

    return score


def part2(guide):
    """
    Steps
    -> (_, X) + 2
    -> (_, Y) + 0
    -> (_, Z) + 1
    Modulo to iterate over the circular list
    """

    circular_list = [1, 2, 3]

    score = 0
    for (elf, shape) in guide:
        if shape == 'Y':
            pos = 0
            score += 3
        elif shape == "Z":
            pos = 1
            score += 6

        elif shape == "X":
            pos = 2
        ind = score_chart[elf] - 1
        score += circular_list[(ind + pos) % 3]

    return score


def main():
    test = read_input(f"inputs/{DAY}_test.txt")
    inputs = read_input(f"inputs/{DAY}.txt")

    p1_test = part1(test)
    p1 = part1(inputs)

    p2_test = part2(test)
    p2 = part2(inputs)

    # For testing
    return (p1, p2), (p1_test, p2_test)


if __name__ == '__main__':
    (p1, p2), (p1_test, p2_test) = main()

    print(f"P1 test: {p1_test}")
    print(f"P1: {p1}")
    print(f"P2 test: {p2_test}")
    print(f"P2: {p2}")
