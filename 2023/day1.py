WORD_MAP = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def part2(line):
    


def main():
    score_part1 = 0
    score_part2 = 0
    with open("day1_input.txt") as f:
        for line in f:
            line_part1 = []
            for c in line:
                if c.isnumeric():
                    line_part1.append(c) 
            score_part1 += int("".join([line_part1[0], line_part1[-1]]))
            score_part2 += part2(line)
    print(f"Part 1: {score_part1}")
    print(f"Part 2: {score_part2}")


if __name__ == "__main__":
    main()
