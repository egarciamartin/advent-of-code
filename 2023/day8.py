from itertools import cycle
from typing import List
from math import lcm


def solve(current: str, end: str, d: dict, instructions=List[str]) -> int:
    circular_ins = cycle(instructions)
    steps = 0
    while not current.endswith(end):
        current = d[current][int(next(circular_ins))]
        steps += 1
    return steps


def main():
    d = {}
    with open("day8_input.txt") as f:
        instructions = f.readline().strip()
        for line in f:
            if len(line.strip()) > 0:
                l = line.strip().split(" = ")
                d[l[0]] = (
                    l[1].split(", ")[0].replace("(", ""),
                    l[1].split(", ")[1].replace(")", ""),
                )
    instructions = instructions.replace("L", "0")
    instructions = instructions.replace("R", "1")

    print(f"Part 1: {solve('AAA', 'ZZZ', d, instructions)}")

    nodes = [node for node in d if node[-1] == "A"]
    steps_part2 = []

    for i, node in enumerate(nodes):
        steps_part2.append(0)
        steps_part2[i] += solve(node, "Z", d, instructions)

    print(f"Part 2: {lcm(*steps_part2)}")


if __name__ == "__main__":
    main()
