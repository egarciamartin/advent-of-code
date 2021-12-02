def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [int(line.rstrip()) for line in lines]
    return input


def parse_input_split(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [line.strip().split(" ") for line in lines]
    return input
