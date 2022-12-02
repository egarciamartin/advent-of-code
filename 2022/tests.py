import pandas as pd
import day1 as d1
import day2 as d2

DAYS = 2
results = pd.read_csv('results.csv', index_col="day")

for day in range(1, DAYS+1):
    (p1, p2), (_, _) = eval(f'd{day}').main()
    p1_target = results.loc[day, 'p1']
    p2_target = results.loc[day, 'p2']

    assert p1 == p1_target, f"Test failed for day {day} PART 1"
    assert p2 == p2_target, f"Test failed for day {day} PART 2"

    print(f"Tests passed for day {day}")

print("Tests passed")
