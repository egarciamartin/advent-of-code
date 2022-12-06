from collections import defaultdict, deque

DAY = 5


def read_input(file):

    stacks = defaultdict(deque)
    moves = []
    moves_section = False
    with open(file) as f:
        for line in f:
            line = line.strip('\n').split(" ")
            if (len(line) <= 1) or (line[0] == "" and line[1] == "1"):
                moves_section = True
                continue
            if not moves_section:
                n_spaces = 0
                n_stack = 1
                for el in line:
                    if el == "":
                        n_spaces += 1
                        if n_spaces == 4:
                            n_stack += 1
                            n_spaces = 0
                    else:
                        c = el[1]
                        stacks[n_stack].append(c)
                        n_stack += 1
            else:
                moves.append((int(line[1]), int(line[3]), int(line[5])))
    return stacks, moves


def part1(stacks, moves):
    message = []
    for move in moves:
        for _ in range(move[0]):
            el = stacks[move[1]].popleft()
            stacks[move[2]].appendleft(el)

    message = [stack[0] for k, stack in sorted(stacks.items())]
    return "".join(message)


def part2(stacks, moves):
    message = []
    for move in moves:
        elements = []
        for _ in range(move[0]):
            elements.append(stacks[move[1]].popleft())
        for el in reversed(elements):
            stacks[move[2]].appendleft(el)

    message = [stack[0] for k, stack in sorted(stacks.items())]
    return "".join(message)


def main():
    test_stacks, test_moves = read_input(f"inputs/{DAY}_test.txt")
    stacks, moves = read_input(f"inputs/{DAY}.txt")

    p1_test = part1(test_stacks, test_moves)
    p1 = part1(stacks, moves)

    test_stacks, test_moves = read_input(f"inputs/{DAY}_test.txt")
    stacks, moves = read_input(f"inputs/{DAY}.txt")

    p2_test = part2(test_stacks, test_moves)
    p2 = part2(stacks, moves)

    return (p1, p2), (p1_test, p2_test)


if __name__ == '__main__':
    (p1, p2), (p1_test, p2_test) = main()

    print(f"P1 test: {p1_test}")
    print(f"P1: {p1}")
    print(f"P2 test: {p2_test}")
    print(f"P2: {p2}")
