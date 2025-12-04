def read_input():
    cds = {}
    with open("day4_input.txt") as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line):
                cds[(i,j)] = c
        max_i = i
        max_j = j

    return cds, max_i, max_j

def get_adjacent(cds, pos_i, pos_j):
    adjacents = []
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    positions = [(pos_i + dx, pos_j + dy) for dx, dy in offsets]

    for pos in positions:
        if pos in cds and cds[pos] == "@":
            adjacents.append(pos)
             
    return adjacents
    

def main():
    cds, max_i, max_j = read_input()
    adjacent_set_p1 = set()
    adjacent_set_p2 = set()
    while True:
        adjacent_set = set()
        for i in range(0, max_i+1):
            for j in range(0, max_j + 1):
                if cds[(i, j)] == "@":
                    adjacents = get_adjacent(cds, i, j)
                    if len(adjacents) < 4:
                        adjacent_set.add((i,j))
                        adjacent_set_p2.add((i,j))
        
        for pos in adjacent_set:
            cds[pos] = "."
        if not adjacent_set_p1:
            adjacent_set_p1 = adjacent_set.copy()
        if not adjacent_set:
            break
    print("Part 1: ", len(adjacent_set_p1))
    print("Part 2: ", len(adjacent_set_p2))

if __name__ == "__main__":
    main()