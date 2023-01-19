
DAY = 7


def read_input(file):
    pass


def part1():
    pass


def part2():
    pass


def main():
    test_inputs = read_input(f"inputs/{DAY}_test.txt")
    inputs = read_input(f"inputs/{DAY}.txt")

    p1_test = part1()
    p1 = part1()

    p2_test = part2()
    p2 = part2()

    return (p1, p2), (p1_test, p2_test)


if __name__ == '__main__':
    (p1, p2), (p1_test, p2_test) = main()

    print(f"P1 test: {p1_test}")
    print(f"P1: {p1}")
    print(f"P2 test: {p2_test}")
    print(f"P2: {p2}")
