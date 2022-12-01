DAY = 1


def read_input(file):
    with open(file) as f:
        calories = f.readlines()
        calories = [cal.strip() for cal in calories]
    return calories


def count_calories(calories):
    cal_l = []
    inter = 0
    for cal in calories:
        if cal == "":
            cal_l.append(inter)
            inter = 0
            continue
        inter += int(cal)
    if inter != 0:
        cal_l.append(inter)
    return cal_l


def main():
    test = read_input(f"inputs/{DAY}_test.txt")
    inputs = read_input(f"inputs/{DAY}.txt")

    p1 = max(count_calories(inputs))
    p1_test = max(count_calories(test))

    p2 = sum(sorted(count_calories(inputs), reverse=True)[:3])
    p2_test = sum(sorted(count_calories(test), reverse=True)[:3])

    # For testing
    return (p1, p2), (p1_test, p2_test)


if __name__ == '__main__':
    (p1, p2), (p1_test, p2_test) = main()

    print(f"P1 test: {p1_test}")
    print(f"P1: {p1}")
    print(f"P2 test: {p2_test}")
    print(f"P2: {p2}")
