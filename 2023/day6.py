def main():
    part1_score = 1
    with open("day6_input.txt") as f:
        times = list(map(int, f.readline().strip().split(": ")[1].split()))
        distances = list(map(int, f.readline().strip().split(": ")[1].split()))

    for time, distance in zip(times, distances):
        ways_to_win = sum(1 for i in range(time) if (time - i) * i > distance)
        if ways_to_win > 0:
            part1_score *= ways_to_win

    print(f"Part 1: {part1_score}")

    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    part2_score = sum(1 for i in range(time) if (time - i) * i > distance)

    print(f"Part 2: {part2_score}")


if __name__ == "__main__":
    main()
