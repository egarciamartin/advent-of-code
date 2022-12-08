import pandas as pd
import day1 as d1
import day2 as d2
import day3 as d3
import day4 as d4
import day5 as d5
import day6 as d6
import day7 as d7
import day8 as d8

DAYS = 8
results = pd.read_csv('results.csv', index_col="day")

for day in range(1, DAYS+1):
    (p1, p2), (_, _) = eval(f'd{day}').main()
    p1_target = results.loc[day, 'p1']
    p2_target = results.loc[day, 'p2']

    assert str(p1) == str(p1_target), f"Test failed for day {day} PART 1"
    assert str(p2) == str(p2_target), f"Test failed for day {day} PART 2"

    print(f"Tests passed for day {day}")

print("Tests passed")
