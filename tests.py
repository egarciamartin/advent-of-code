import util
import day_1
import day_2
import day_3
import day_4


def test_day1(day, values):
    """
    Each value for each part 
    """
    p1_res = values[0]
    p2_res = values[1]

    input = util.parse_input(day)
    input = [int(item) for item in input]

    assert p1_res == day_1.part1(input), "Part 1 incorrect"
    assert p2_res == day_1.part2(input), "Part 2 incorrect"
    print(f"All tests passed for {day}")


def test_day2(day, values):
    p1_res = values[0]
    p2_res = values[1]

    input = util.parse_input_split(day)

    assert p1_res == day_2.part1(input), "Part 1 incorrect"
    assert p2_res == day_2.part2(input), "Part 2 incorrect"
    print(f"All tests passed for {day}")


def test_day3(day, values):
    p1_res = values[0]
    p2_res = values[1]

    input = util.parse_input(day)

    assert p1_res == day_3.part1(input), "Part 1 incorrect"
    assert p2_res == day_3.part2(input), "Part 2 incorrect"
    print(f"All tests passed for {day}")


def test_day4(day, values):
    p1_res = values[0]
    p2_res = values[1]

    numbers, boards = day_4.parse_input(day)

    assert p1_res == day_4.part1(numbers, boards), "Part 1 incorrect"
    assert p2_res == day_4.part2(numbers, boards), "Part 2 incorrect"
    print(f"All tests passed for {day}")


test_day1('day1_test', (7, 5))
test_day1('day1', (1390, 1457))
test_day2('day2_test', (150, 900))
test_day2('day2', (2027977, 1903644897))
test_day3('day3_test', (198, 230))
test_day3('day3', (3687446, 4406844))
test_day4('day4_test', (4512, 1924))
test_day4('day4', (58838, 6256))

print("All tests passed")
