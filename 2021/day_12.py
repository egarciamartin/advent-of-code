from collections import defaultdict
from collections import deque


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip() for line in lines]
    return input


def get_graph(input):
    graph = defaultdict(list)
    for line in input:
        p1, p2 = line.split("-")
        graph[p1].append(p2)
        graph[p2].append(p1)

    return graph


def part1(input):
    """
    Idea: Queue of lists. On each list is the path and while there is no end, keep adding to
    that path
    """
    graph = get_graph(input)
    paths = list()
    q = deque()
    count = 0
    for p in graph['start']:
        q.append([p])
    while q:
        nodes = q.pop()
        for p in graph[nodes[-1]]:  # neighbors
            if p == 'start' or (p.islower() and p in nodes):
                continue
            elif p == 'end':
                paths.append(nodes)
                count += 1
            else:
                # The ones left, plus the current one.
                q.append(nodes + [p])

    return count


def part2_condition(nodes):
    """
    There are already more than one small cave. 
    That and p in nodes, means that there would be 2 pairs of repeated small ones
    which is not allowed
    """
    for i in nodes:
        if i.islower() and nodes.count(i) > 1:
            return True
    return False


def part2(input):
    graph = get_graph(input)
    paths = list()
    q = deque()
    count = 0
    for p in graph['start']:
        q.append([p])

    while q:
        nodes = q.pop()
        p2 = part2_condition(nodes)
        for p in graph[nodes[-1]]:  # neighbors
            if p == 'start' or (p.islower() and p in nodes and p2):
                continue
            elif p == 'end':
                paths.append(nodes)
                count += 1
            else:
                # The ones left, plus the current one.
                q.append(nodes + [p])

    return count


if __name__ == '__main__':

    test = parse_input('day12_test')
    input = parse_input('day12')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test {part2(test)}')
    print(f'Part 2: Real {part2(input)}')
