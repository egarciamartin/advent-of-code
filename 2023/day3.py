from functools import reduce


def valid_positions(pos):
    return [
        (pos[0] - 1, pos[1] - 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1] - 1),
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1] + 1),
        (pos[0], pos[1] + 1),
        (pos[0] + 1, pos[1] + 1),
    ]


def main():
    symbols = {}
    part_numbers = []
    part_numbers_positions = {}
    gear_ratios = []
    with open("day3_input.txt") as f:
        file = f.readlines()
        for row, line in enumerate(file):
            line = line.strip()
            for col, c in enumerate(line):
                if c != "." and not c.isnumeric():
                    symbols[(row, col)] = c
        number = ""
        positions = []
        for row, line in enumerate(file):
            for col, c in enumerate(line):
                if c.isnumeric():
                    number += c
                    positions.append((row, col))
                else:
                    if number != "":
                        adjacent = False
                        for pos_iter in positions:
                            for check_pos in valid_positions(pos_iter):
                                if check_pos in symbols:
                                    adjacent = True
                                    break
                            if adjacent:
                                part_numbers.append(int(number))
                                part_numbers_positions.update(
                                    {pos: int(number) for pos in positions}
                                )

                                break
                    number = ""
                    positions = []

        for pos, symbol in symbols.items():
            if symbol == "*":
                gears_tmp = set()
                for check_pos in valid_positions(pos):
                    if check_pos in part_numbers_positions:
                        gears_tmp.add(part_numbers_positions[check_pos])
                if len(gears_tmp) == 2:
                    gear_ratios.append(reduce(lambda x, y: x * y, gears_tmp))
    print(f"Part 1: {sum(part_numbers)}")
    print(f"Part 2: {sum(gear_ratios)}")


if __name__ == "__main__":
    main()
