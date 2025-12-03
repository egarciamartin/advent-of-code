from typing import List


def read_input(file = "day3_input.txt") -> List:
    banks = []
    with open(file) as f:
        for line in f:
            banks.append(list(map(int, line.strip())))
    return banks


def calculate_joltage(banks: List[int], init_total: int = 2) -> int:
    """
    Greedy approach. On each pass (of each line), check the max considering that
    the number has to have a total number of digits. e.g., if total = 3, and the input is: [9, 8, 7, 6]
    we stop checking after the 7 (3rd digit)
    """
    total_joltage = []
    for bank in banks:
        joltages = []
        total = init_total
        max_i = 0
        while total >= 1:
            max_n = 0
            for i in range(max_i, len(bank)-total+1):
                if bank[i] > max_n:
                    max_n = bank[i]
                    max_i = i+1
            total -= 1
            joltages.append(max_n)
        total_joltage.append("".join(list(map(str, joltages))))
    return sum(map(int, total_joltage))



def main(): 
    banks = read_input()

    print("Part 1", calculate_joltage(banks, 2))
    print("Part 2", calculate_joltage(banks,12))

if __name__ == "__main__":
    main()
