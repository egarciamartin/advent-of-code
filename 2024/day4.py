from typing import Dict, Tuple, List

FILE_PATH = "day4_input.txt"


def is_adjacent(pos: Tuple, letter: str, word_map: Dict) -> List[Tuple]:
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    possible_positions = [(pos[0] + dx, pos[1] + dy) for dx, dy in offsets]
    positions = []
    for position in possible_positions:
        if position in word_map and word_map[position] == letter:
            positions.append(position)
    return positions


def count_p1(word_map: Dict) -> int:
    total = 0
    for k, c in word_map.items():
        if c == "X":
            positions = is_adjacent(pos=k, letter="M", word_map=word_map)
            for pos in positions:
                diff = (pos[0] - k[0], pos[1] - k[1])
                next_coordinate = (pos[0] + diff[0], pos[1] + diff[1])
                next_next_coordinate = (pos[0] + (diff[0] * 2), pos[1] + (diff[1] * 2))
                if (
                    next_coordinate in word_map
                    and next_next_coordinate in word_map
                    and word_map[next_coordinate] == "A"
                    and word_map[next_next_coordinate] == "S"
                ):
                    total += 1
    return total


def count_p2(word_map: Dict) -> int:
    total = 0
    valid_patterns = [
        ("M", "S", "M", "S"),
        ("S", "S", "M", "M"),
        ("M", "M", "S", "S"),
        ("S", "M", "S", "M"),
    ]
    for k, c in word_map.items():
        if c == "A":
            tl = (k[0] - 1, k[1] - 1)
            tr = (k[0] - 1, k[1] + 1)
            bl = (k[0] + 1, k[1] - 1)
            br = (k[0] + 1, k[1] + 1)
            if tl in word_map and tr in word_map and bl in word_map and br in word_map:
                if (
                    word_map[tl],
                    word_map[tr],
                    word_map[bl],
                    word_map[br],
                ) in valid_patterns:
                    total += 1
    return total


def main() -> None:
    word_map = {}
    with open(FILE_PATH) as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line.strip()):
                word_map[(i, j)] = c
    print(f"PART 1: {count_p1(word_map=word_map)}")
    print(f"PART 2: {count_p2(word_map=word_map)}")


if __name__ == "__main__":
    main()
