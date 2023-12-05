from functools import reduce
from collections import defaultdict


def main():
    maps = {
        "seed": [],
        "soil": [],
        "fertilizer": [],
        "water": [],
        "light": [],
        "temperature": [],
        "humidity": [],
    }
    with open("day5_input.txt") as f:
        seeds = list(map(int, f.readline().strip().split(": ")[1].split(" ")))
        print(seeds)
        for line in f:
            line = line.strip()
            try:
                if str(line[0]).isalpha():
                    map_ = line.split("-")[0]
                elif str(line[0]).isnumeric():
                    dest, source, range_ = tuple(map(int, line.split(" ")))
                    maps[map_].append(
                        {
                            "min": source,
                            "max": source + range_ - 1,
                            "diff": dest - source,
                        }
                    )
            except:
                continue
    locations = set()
    for seed in seeds:
        for name, map_ in maps.items():
            for el in map_:
                if seed >= el["min"] and seed <= el["max"]:
                    seed += el["diff"]
                    break
        locations.add(seed)
    print(f"Part 1: {min(locations)}")
    # print(f"Part 2: {sum(card_copies.values())}")


if __name__ == "__main__":
    main()
