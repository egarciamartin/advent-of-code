import util
import day_1
import day_2
import day_3
import day_4
import day_5
import day_6
import day_7


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

    assert p1_res == day_4.get_score(numbers, boards), "Part 1 incorrect"
    assert p2_res == day_4.get_score(numbers, boards, True), "Part 2 incorrect"
    print(f"All tests passed for {day}")


def test_day5(day, values):
    p1_res = values[0]
    p2_res = values[1]

    input = day_5.parse_input(day)

    assert p1_res == day_5.sum_points(input), "Part 1 incorrect"
    assert p2_res == day_5.sum_points(input, part2=True), "Part 2 incorrect"
    print(f"All tests passed for {day}")


def test_day6(day, values):
    p1_res = values[0]
    p2_res = values[1]

    input = day_6.parse_input(day)

    assert p1_res == day_6.count(input, 80), "Part 1 incorrect"
    assert p2_res == day_6.count(input, 256), "Part 2 incorrect"
    print(f"All tests passed for {day}")


def test_day7(day, values):
    p1_res = values[0]
    p2_res = values[1]

    input = day_7.parse_input(day)

    assert p1_res == day_7.get_lowest_fuel(input), "Part 1 incorrect"
    assert p2_res == day_7.get_lowest_squared_fuel(input), "Part 2 incorrect"
    print(f"All tests passed for {day}")


test_day1('day1_test', (7, 5))
test_day1('day1', (1390, 1457))

test_day2('day2_test', (150, 900))
test_day2('day2', (2027977, 1903644897))

test_day3('day3_test', (198, 230))
test_day3('day3', (3687446, 4406844))

test_day4('day4_test', (4512, 1924))
test_day4('day4', (58838, 6256))

test_day5('day5_test', (5, 12))
test_day5('day5', (5576, 18144))

test_day6('day6_test', (5934, 26984457539))
test_day6('day6', (360268, 1632146183902))

test_day7('day7_test', (37, 168))
test_day7('day7', (339321, 95476244))

print("All tests passed")
