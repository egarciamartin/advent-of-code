def is_invalid_id_p1(id_: str) -> bool:
    return id_[:len(id_) // 2] == id_[len(id_) // 2:] 
    

def is_invalid_id_p2(id_: str,) -> bool:
    len_id = len(id_)
    if len_id % 2 != 0 and len(set(id_))== 1 and len_id > 1:
        return True
    
    for k in range(1, (len_id // 2) + 1):
        if len_id % k == 0:
            divided_id = []
            for i in range(0, len_id, k):
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
            if is_invalid_id_p1(str(i)):
                total_part1 += i
            if is_invalid_id_p2(str(i)):
                total_part2 += i
    
    print("Part 1", total_part1)
    print("Part 2", total_part2)
            

if __name__ == "__main__":
    main()
