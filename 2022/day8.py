DAY = 8


def read_input(file):
    tree_map = dict()
    with open(file) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            for j, el in enumerate(line):
                tree_map[(i, j)] = int(el)
    return tree_map


def is_edge(k, max_row, max_col):

    if k[0] == 0 or k[1] == 0:
        return True
    if k[0] == max_row or k[1] == max_col:
        return True
    return False


def part1(tree_map):
    visible = set()
    max_row = max(tree_map.keys(), key=lambda k: k[0])[0]
    max_col = max(tree_map.keys(), key=lambda k: k[1])[1]

    for cr, height in tree_map.items():
        if is_edge(cr, max_row, max_col):
            visible.add(cr)
        else:
            left = [tree_map[(cr[0], i)] for i in range(0, cr[1])]
            right = [tree_map[(cr[0], i)] for i in range(cr[1]+1, max_col+1)]
            top = [tree_map[(i, cr[1])] for i in range(0, cr[0])]
            down = [tree_map[(i, cr[1])] for i in range(cr[0]+1, max_row+1)]
            if height > max(left) or height > max(right) or height > max(top) or height > max(down):
                visible.add(cr)

    return len(visible)


def part2(tree_map):
    max_row = max(tree_map.keys(), key=lambda k: k[0])[0]
    max_col = max(tree_map.keys(), key=lambda k: k[1])[1]

    max_score = 0
    for cr, height in tree_map.items():
        if is_edge(cr, max_row, max_col):
            continue
        left = [tree_map[(cr[0], i)] for i in range(0, cr[1])]
        right = [tree_map[(cr[0], i)] for i in range(cr[1]+1, max_col+1)]
        top = [tree_map[(i, cr[1])] for i in range(0, cr[0])]
        down = [tree_map[(i, cr[1])] for i in range(cr[0]+1, max_row+1)]

        scores = 1
        for l, name in zip([left, top, right, down], ['l', 't', 'r', 'd']):
            score_tree = 0
            if name == 'l' or name == 't':
                l = reversed(l)
            for h in l:
                score_tree += 1
                if h >= height:
                    break
            scores *= score_tree
        if scores > max_score:
            max_score = scores
    return max_score


def main():
    test_inputs = read_input(f"inputs/{DAY}_test.txt")
    inputs = read_input(f"inputs/{DAY}.txt")

    p1_test = part1(test_inputs)
    p1 = part1(inputs)

    p2_test = part2(test_inputs)
    p2 = part2(inputs)
    return (p1, p2), (p1_test, p2_test)


if __name__ == '__main__':
    (p1, p2), (p1_test, p2_test) = main()

    print(f"P1 test: {p1_test}")
    print(f"P1: {p1}")
    print(f"P2 test: {p2_test}")
    print(f"P2: {p2}")
