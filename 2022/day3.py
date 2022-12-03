DAY = 3


def read_input(file):
    with open(file) as f:
        contents = f.readlines()
        contents = [line.strip() for line in contents]
        return contents


def get_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def part1(items):
    priorities = 0
    for item in items:
        half = int(len(item)/2)
        common = "".join(set(item[:half]) & set(item[half:]))
        priorities += get_priority(common)
    return priorities


def part2(items):
    priorities = 0
    for i in range(len(items))[::3]:
        common = "".join(set(items[i]) & set(items[i+1]) & set(items[i+2]))
        priorities += get_priority(common)
    return priorities


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
