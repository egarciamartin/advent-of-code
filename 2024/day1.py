from collections import Counter
FILE_NAME = "day1_input.txt"

def main():
    left = []
    right = []
    total_part1 = 0
    total_part2 = 0
    with open(FILE_NAME) as f:
        for line in f:
            l = line.strip().split("  ")
            left.append(int(l[0]))
            right.append(int(l[1]))
    counter_right = Counter(right)
    for left_i, right_i in zip(sorted(left), sorted(right)):
        total_part1 += abs(right_i - left_i)
        total_part2 += left_i * counter_right[left_i]

    print(f"PART 1: {total_part1}")
    print(f"PART 2: {total_part2}")
if __name__ == "__main__":
    main()