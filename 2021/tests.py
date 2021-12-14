import day_1
import day_2
import day_3
import day_4
import day_5
import day_6
import day_7
import day_8
import day_9
import day_10
import day_11
import day_12
import day_13

DAYS = 13
days = [i for i in range(1, DAYS + 1)]
days_func = [eval(f'day_{i}') for i in days]
results = [[(7, 5), (1390, 1457)],
           [(150, 900), (2027977, 1903644897)],
           [(198, 230), (3687446, 4406844)],
           [(4512, 1924), (58838, 6256)],
           [(5, 12), (5576, 18144)],
           [(5934, 26984457539), (360268, 1632146183902)],
           [(37, 168), (339321, 95476244)],
           [(26, 61229), (519, 1027483)],
           [(15, 1134), (489, 1056330)],
           [(26397, 288957), (290691, 2768166558)],
           [(1656, 195), (1725, 308)],
           [(10, 36), (3410, 98796)],
           [(17, None), (621, None)],
           [(1588, 2188189693529), (3306, 3760312702877)]
           ]


for i, day_func in zip(days, days_func):
    input = day_func.parse_input(f'day{i}')
    test = day_func.parse_input(f'day{i}_test')

    p1_test = day_func.part1(test)
    p2_test = day_func.part2(test)

    p1_real = day_func.part1(input)
    p2_real = day_func.part2(input)

    assert p1_test == results[i-1][0][0], f"Day {i} test part 1 incorrect"
    assert p2_test == results[i-1][0][1], f"Day {i} test part 2 incorrect"

    assert p1_real == results[i-1][1][0], f"Day {i} part 1 incorrect"
    assert p2_real == results[i-1][1][1], f"Day {i} part 2 incorrect"

    print(f"Tests for day {i} passed")

print("--- All tests passed ----")
