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
import day_14
import day_15
import day_17
import day_20
import day_24
import day_25


with open(f'results.csv') as file:
    lines = file.readlines()
    results = [line.strip() for line in lines]

for i in range(25):
    try:
        day_func = eval(f'day_{i+1}')
    except:
        print(f"No solution yet for Day {i+1}")
        continue

    input = day_func.parse_input(f'day{i+1}')
    p1 = day_func.part1(input)
    p2 = day_func.part2(input)

    p1_res = int(results[i+1].split(",")[1])
    p2_res = int(results[i+1].split(",")[2])

    assert p1 == p1_res, f"Day {i+1} part 1 incorrect"
    assert p2 == p2_res, f"Day {i+1} part 2 incorrect"

    print(f"Day {i+1} Tests Passed")

print("All Tests Passed")
