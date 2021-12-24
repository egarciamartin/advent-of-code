
def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def get_grid(input_image):
    """
    i = rows
    j = cols
    """

    grid = dict()
    for i, row in enumerate(input_image):
        for j, pix in enumerate(row):
            grid[(i, j)] = pix

    return grid


def get_neighbors(point):
    """
    Diagonals also

    """
    neighbors = list()
    directions = [(0, 1), (0, -1), (1, 0), (1, 1),
                  (1, -1), (-1, 0), (-1, 1), (-1, -1)]

    for d in directions:
        cand = tuple(sum(x) for x in zip(point, d))
        # if cand[0] >= 0 and cand[1] >= 0 and cand[0] <= (grid_size[0] - 1) and cand[1] <= (grid_size[1]-1):
        neighbors.append(cand)
    neighbors.append(point)
    return neighbors


def padding(d, c):
    " 1 top, down, left, right"
    max_x, max_y = max(d.keys())
    min_x, min_y = min(d.keys())

    # top, bottom
    for j in range(min_y - 1, max_y + 2):
        d[(min_x - 1, j)] = c
        d[(max_x + 1, j)] = c
    # left,  right
    for i in range(min_x, max_x+1):
        d[(i, min_y - 1)] = c
        d[(i, max_y + 1)] = c

    return d


def enhance(steps, enh_alg, in_grid, c_):
    for _ in range(steps):
        out_grid = dict()
        for k in in_grid.keys():
            neighbors = sorted(get_neighbors(k))
            st_char = [
                str(in_grid[p]) if p in in_grid else c_ for p in neighbors]
            enh_ind = int(
                "".join(["1" if c == "#" else "0" for c in st_char]), 2)
            out_grid[k] = enh_alg[enh_ind]

        # flipping if the first is #
        if enh_alg[0] == "#":
            c_ = "." if c_ == "#" else "#"
        in_grid = padding(out_grid, c_)
    return out_grid


def part1(input):
    """
    1. Read image
    2. Add padding "."
    3. Get neighbors for every k 
    4. Get the value or c_ if not in keys, convert to binary and then to decimal. 
    5. Get output character
    6. Add padding with c_ if needed to flip, otherwise "."
    """
    enh_alg = input[0]
    input_image = input[2:]
    grid = get_grid(input_image)
    c_ = '.'
    in_grid = padding(grid, c_)
    steps = 2
    out_grid = enhance(steps, enh_alg, in_grid, c_)
    s = sum([1 for v in out_grid.values() if v == "#"])
    return s


def part2(input):
    """
    Takes a bit too long. (17 secs)
    """
    enh_alg = input[0]
    input_image = input[2:]
    grid = get_grid(input_image)
    c_ = '.'
    in_grid = padding(grid, c_)
    steps = 50
    out_grid = enhance(steps, enh_alg, in_grid, c_)
    s = sum([1 for v in out_grid.values() if v == "#"])
    return s


if __name__ == '__main__':

    test = parse_input('day20_test')
    input = parse_input('day20')

    # print(test)

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
