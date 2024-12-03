import re

FILE_PATH = "day3_input.txt"


def mult(el: str) -> int:
    mems = el.replace("mul(", "").replace(")", "").split(",")
    return int(mems[0]) * int(mems[1])


def main() -> None:
    pattern = re.compile("do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")
    total_part1 = 0
    total_part2 = 0
    with open(FILE_PATH) as f:
        prev = "do()"
        for line in f:
            finds = pattern.findall(line)
            total_part1 += sum(
                [mult(el) for el in finds if el not in (["don't()", "do()"])]
            )

            for el in finds:
                if el in (["don't()", "do()"]):
                    prev = el
                elif prev == "do()":
                    total_part2 += mult(el)

    print(f"PART 1: {total_part1}")
    print(f"PART 2: {total_part2}")


if __name__ == "__main__":
    main()
