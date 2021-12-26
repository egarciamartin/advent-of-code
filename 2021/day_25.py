
def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def get_next(c, k, grid_size):
    if c == '>':
        if (k[1] + 1) > grid_size[1]:
            next = (k[0], 0)
        else:
            next = (k[0], k[1]+1)
    elif c == 'v':
        if (k[0] + 1) > grid_size[0]:
            next = (0, k[1])
        else:
            next = (k[0]+1, k[1])
    return next


def move(d, c, grid_size):
    out = dict()
    hasmoved = 0
    for k, v in d.items():
        if v == c:
            next = get_next(c, k, grid_size)
            if d[next] == '.':
                out[k] = '.'
                out[next] = v
                hasmoved += 1
            elif k not in out:
                out[k] = v
        elif k not in out:
            out[k] = v
    return out, hasmoved


def part1(input):
    mp = dict()
    for i, line in enumerate(input):
        for j, sc in enumerate(line):
            mp[(i, j)] = sc

    grid_size = (i, j)
    steps = 0
    while True:
        mp, moved_east = move(mp, '>', grid_size)
        mp, moved_south = move(mp, 'v', grid_size)
        if moved_south < 1 and moved_east < 1:
            break
        steps += 1
    return steps + 1


def part2(input):

    return


if __name__ == '__main__':

    test = parse_input('day25_test')
    input = parse_input('day25')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")
