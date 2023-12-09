def main():
    extrapolated_sum = 0
    with open("day9_input.txt") as f:
        for line in f:
            history = list(map(int, line.strip().split()))
            last_history = [history[-1]]
            while len(set(history)) > 1:
                history = [y - x for x, y in zip(history[:-1], history[1:])]
                last_history.append(history[-1])

            extrapolated_sum += sum(last_history)

    print(f"Part 1: {extrapolated_sum}")
    # print(f"Part 2: {}")


if __name__ == "__main__":
    main()
