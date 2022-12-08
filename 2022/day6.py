
DAY = 6


def read_input(file):
    with open(file) as f:
        l = f.readline().strip()
    return l


def get_marker(inputs, window):
    start = 0

    while (start + window) <= len(inputs):
        packet = inputs[start:start+window]
        if len(packet) == len(set(packet)):
            return start+window
        start += 1


def main():
    test_inputs = read_input(f"inputs/{DAY}_test.txt")
    inputs = read_input(f"inputs/{DAY}.txt")

    p1_test = get_marker(test_inputs, 4)
    p1 = get_marker(inputs, 4)

    p2_test = get_marker(test_inputs, 14)
    p2 = get_marker(inputs, 14)

    return (p1, p2), (p1_test, p2_test)


if __name__ == '__main__':
    (p1, p2), (p1_test, p2_test) = main()

    print(f"P1 test: {p1_test}")
    print(f"P1: {p1}")
    print(f"P2 test: {p2_test}")
    print(f"P2: {p2}")
