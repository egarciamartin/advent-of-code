word_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def main():
    score_part1 = 0
    score_part2 = 0
    with open("day1_input.txt") as f:
        for line in f:
            line_part1 = []
            line_part2 = []
            for i, c in enumerate(line):
                if c.isnumeric():
                    line_part1.append(c)
                    line_part2.append(c)
                else:
                    for word, number in word_map.items():
                        if line[i: i+len(word)] == word:
                            line_part2.append(word_map[word])
            score_part1 += int("".join([line_part1[0], line_part1[-1]]))
            score_part2 += int("".join([line_part2[0], line_part2[-1]]))
    print(f"Part 1: {score_part1}")
    print(f"Part 2: {score_part2}")


if __name__ == "__main__":
    main()
