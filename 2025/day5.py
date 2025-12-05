from typing import List


def update_ranges(fresh_ranges: List) -> List:
    updated_ranges = set(fresh_ranges)
    while True:
        updates = 0
        for (i1, i2) in fresh_ranges:
            for (u1, u2) in fresh_ranges:
                if (i1, i2) == (u1, u2):
                    continue

                if u1 < i1 and u2 > i2:
                    updated_ranges.discard((i1, i2))
                    updated_ranges.add((u1, u2))
                    updates += 1

                elif u1 < i1 and u2 <= i2 and u2 >= u1 and u2 >= i1:
                    updated_ranges.discard((u1, u2))
                    updated_ranges.discard((i1, i2))
                    updated_ranges.add((u1, i2))
                    updates += 1
                elif u2 > i2 and u1 >= i1 and u1 <= i2:
                    updated_ranges.discard((u1, u2))
                    updated_ranges.discard((i1, i2))
                    updated_ranges.add((i1, u2))
                    updates += 1
            
        fresh_ranges = updated_ranges.copy()
        if updates == 0:
            break
    return updated_ranges


def main():
    fresh_ranges = []
    ranges = True
    total_part1 = 0
    total_part2 = 0
    with open("day5_input.txt") as f:
        for line in f:
            if line == "\n":
                ranges = False
                continue
            if ranges:
                n1, n2 = line.strip().split("-")
                fresh_ranges.append((int(n1), int(n2)))
            else:
                id_ = int(line.strip())
                for (low, top) in fresh_ranges:
                    if id_ >= low and id_ <= top:
                        total_part1+=1
                        break
        
    updated_ranges = update_ranges(fresh_ranges)
    for (low, top) in updated_ranges:
        total_part2 += (top - low + 1)
    print("Part 1: ", total_part1)
    print("Part 2: ", total_part2)

if __name__ == "__main__":
    main()  