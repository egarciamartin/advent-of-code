
def get_divisors(n) -> int:
    divisors = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_invalid_id(id_: str, part1=True) -> bool:
    if part1:
        if len(id_) % 2 != 0:
            return False
        divisions = [len(id_) // 2]
    else:
        if len(id_) % 2 != 0 and len(set(id_))== 1 and len(id_) > 1:
            return True
        divisions = get_divisors(len(id_))
    
    for k in divisions:
        divided_id = []
        for i in range(0, len(id_), k):
            divided_id.append(id_[i : i + k])
        if len(set(divided_id)) == 1:
            return True

    return False


def main():
    with open("day2_input.txt") as f:
        line = f.read().replace("\n", "")
        pairs = [tuple(map(int, rng.split("-"))) for rng in line.strip().split(",") if rng]
        print(pairs)

    total_part1 = 0
    total_part2 = 0
    for pair in pairs:
        start, end = pair
        for i in range(start, end+1):
            if is_invalid_id(str(i), part1=True):
                total_part1 += i
            if is_invalid_id(str(i), part1=False):
                total_part2 += i
    
    print("Part 1", total_part1)
    print("Part 2", total_part2)
            

if __name__ == "__main__":
    main()
