from typing import List

FILE_PATH = "day2_input.txt"


def is_save(level: List) -> bool:
    """
    Calculate the differences, and if any of them is not between (-1, -3) or (1,3),
    return False. Considers increasing or decreasing values
    """
    diffs = [level[i] - level[i + 1] for i in range(len(level) - 1)]
    if all([-3 <= el <= -1 for el in diffs]) or all([1 <= el <= 3 for el in diffs]):
        return True
    return False


def main() -> None:
    """Part 2: check removing one level at a time, and then if any of those
    combinations is True, the report is safe
    """
    total_part1 = 0
    total_part2 = 0
    with open(FILE_PATH) as f:
        for report in f:
            l = list(map(int, report.strip().split(" ")))
            total_part1 += is_save(l)
            total_part2 += any([is_save(l[:i] + l[i + 1 :]) for i in range(len(l))])
    print(f"PART 1: {total_part1}")
    print(f"PART 2: {total_part2}")


if __name__ == "__main__":
    main()
