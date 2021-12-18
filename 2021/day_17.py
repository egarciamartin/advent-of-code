

def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        input = file.readline()
        x = input.split('x=')[1].split('..')
        xmin = int(x[0])
        xmax = int(x[1].split(',')[0])
        y = input.split('y=')[1].split('..')
        ymin = int(y[0])
        ymax = int(y[1])
    return xmin, xmax, ymin, ymax


def sign(x):
    if x > 0:
        return -1
    elif x < 0:
        return 1
    else:
        return 0


def get_valid_shots(input):
    """
    Too complicated, help from @javitronxo
    """
    xmin, xmax, ymin, ymax = input
    valid = dict()

    for vx in range(0, 300):
        for vy in range(-120, 120):
            pos = [0, 0]
            highest_y = 0
            vx_, vy_ = vx, vy
            while pos[0] <= xmax and pos[1] >= ymin:
                pos[0] = pos[0] + vx_
                pos[1] = pos[1] + vy_
                vx_ += sign(vx_)
                vy_ -= 1
                highest_y = max(highest_y, pos[1])
                if xmin <= pos[0] <= xmax and ymin <= pos[1] <= ymax:
                    valid[(vx, vy)] = highest_y
    return valid


def part1(input):
    """
    Test all possible combinations of initial velocities
    x ranges between 0 and 300 (limit based on the test data)
    y ranges between the limits of ymin
    Save all the valid ones, and their height.
    Then get the one with the max y
    """
    valid = get_valid_shots(input)
    return max(valid.values())


def part2(input):
    valid = get_valid_shots(input)
    return len(valid)


if __name__ == '__main__':

    test = parse_input('day17_test')
    input = parse_input('day17')

    print(f"Part 1: Test: {part1(test)}")
    print(f"Part 1: Real: {part1(input)}")

    print(f'Part 2: Test: {part2(test)}')
    print(f'Part 2: Real: {part2(input)}')
