from typing import List


def calculate_mirror(pattern: List) -> int:
    mirror_part1 = 0
    mirror_part2 = 0

    for i in range(1, len(pattern)):
        first = pattern[:i][::-1]
        second = pattern[i:]

        first = first[: len(second)]
        second = second[: len(first)]
        if first == second:
            mirror_part1 = i

        differences = 0
        for lf, ls in zip(first, second):
            for el_f, el_s in zip(lf, ls):
                if el_f != el_s:
                    differences += 1

        if differences == 1:
            mirror_part2 = i
    return mirror_part1, mirror_part2


def main():
    total_part1 = 0
    total_part2 = 0
    patterns = []
    with open("day13_input.txt") as f:
        l = []
        for line in f:
            if line == "\n":
                patterns.append(l)
                l = []
                continue
            l.append(line.strip())
    patterns.append(l)

    for pattern in patterns:
        p1h, p2h = calculate_mirror(pattern)
        total_part1 += 100 * p1h
        total_part2 += 100 * p2h

        columns = list(zip(*pattern))
        p1v, p2v = calculate_mirror(columns)
        total_part1 += p1v
        total_part2 += p2v

    print(f"Part 1: {total_part1}")
    print(f"Part 2: {total_part2}")


if __name__ == "__main__":
    main()
