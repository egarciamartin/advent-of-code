def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = lines[0].strip().split(",")
        input = [int(i) for i in input]
    return input


def get_lowest_fuel(input):
    """
    median
    """
    position = sorted(input)[len(input) // 2]
    return sum([abs(i - position) for i in input])


def get_lowest_squared_fuel(input):
    """
    mean and surroundings
    """
    position = round(sum(input) / len(input))

    fuels = list()
    for position in [position, position+1, position-1]:
        fuels.append(
            sum([sum(j for j in range(1, abs(i - position)+1)) for i in input]))
    return min(fuels)


if __name__ == '__main__':

    test = parse_input('day7_test')
    input = parse_input('day7')

    print(f"Part 1: Test: {get_lowest_fuel(test)}")
    print(f"Part 1: Real: {get_lowest_fuel(input)}")

    print(f'Part 2: Test {get_lowest_squared_fuel(test)}')
    print(f'Part 2: Real {get_lowest_squared_fuel(input)}')
