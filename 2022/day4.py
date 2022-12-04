DAY = 4


def read_input(file):
    inputs = []
    with open(file) as f:
        for line in f:
            l = line.strip().split(',')
            l = [(int(el.split('-')[0]), int(el.split('-')[1])) for el in l]
            inputs.append(l)
    return inputs


def get_pairs(items, part2=False):

    pairs = 0
    for el in items:
        # contained inside (2 in 1)
        if el[0][0] <= el[1][0] and el[0][1] >= el[1][1]:
            pairs += 1
        # contained inside (1 in 2)
        elif el[1][0] <= el[0][0] and el[1][1] >= el[0][1]:
            pairs += 1

        elif not el[1][0] > el[0][1] and not el[0][0] > el[1][1] and part2:
            pairs += 1

    return pairs


def main():
    test = read_input(f"inputs/{DAY}_test.txt")
    inputs = read_input(f"inputs/{DAY}.txt")

    p1_test = get_pairs(test)
    p1 = get_pairs(inputs)

    p2_test = get_pairs(test, part2=True)
    p2 = get_pairs(inputs, part2=True)

    # For testing
    return (p1, p2), (p1_test, p2_test)


if __name__ == '__main__':
    (p1, p2), (p1_test, p2_test) = main()

    print(f"P1 test: {p1_test}")
    print(f"P1: {p1}")
    print(f"P2 test: {p2_test}")
    print(f"P2: {p2}")
