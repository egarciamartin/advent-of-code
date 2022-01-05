def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def get_map(input):
    m = set()
    for line in input:
        if line.startswith('fold') or line == '':
            break
        i, j = line.split(',')
        m.add((int(i), int(j)))
    return m


def part1(input):
    n_folds = 1
    m = get_map(input)
    folds = [line.split(' ')[2] for line in input if line.startswith('fold')]
    for i in range(n_folds):
        fold = folds[i]
        fold_n = int(fold.split("=")[1])
        fold_n_bot = fold_n * 2 + 1
        for n, rev in zip(range(fold_n), reversed(range(fold_n_bot))):
            if n == rev:
                break

            if fold.split('=')[0] == 'y':
                keys_rev = [k for k in m if k[1] == rev]
                for k in keys_rev:
                    m.add((k[0], n))

            else:
                keys_rev = [k for k in m if k[0] == rev]
                for k in keys_rev:
                    m.add((n, k[1]))

            for k in keys_rev:
                m.remove(k)
    return len(m)


def part2(input):

    m = get_map(input)
    folds = [line.split(' ')[2] for line in input if line.startswith('fold')]
    for fold in folds:
        fold_n = int(fold.split("=")[1])
        fold_n_bot = fold_n * 2 + 1
        for n, rev in zip(range(fold_n), reversed(range(fold_n_bot))):
            if n == rev:
                break

            if fold.split('=')[0] == 'y':
                keys_rev = [k for k in m if k[1] == rev]

                for k in keys_rev:
                    m.add((k[0], n))

            else:
                keys_rev = [k for k in m if k[0] == rev]

                for k in keys_rev:
                    m.add((n, k[1]))

            for k in keys_rev:
                m.remove(k)

    x_ = [k[0] for k in m]
    y_ = [k[1] for k in m]
    max_x = max(x_)
    max_y = max(y_)

    for j in range(max_y + 1):
        row = list()
        for i in range(max_x + 1):
            if (i, j) in m:
                row.append("#")
            else:
                row.append(" ")
        print("".join(row))
    return -1


if __name__ == '__main__':

    test = parse_input('day13_test')
    input = parse_input('day13')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
