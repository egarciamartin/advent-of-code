from collections import deque
from typing import Tuple

INITIAL = 50
circular = deque(list(range(0, 100)))
circular.rotate(INITIAL)

def read_input(input_file="day1_input.txt"):
    with open(input_file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def mod_rotate(q: deque, n: int, direction: str) -> Tuple[deque, int]:
    all_zero_clicks = 0
    if direction == "L":
        for _ in range(n):
            popped = q.pop()
            if popped == 0: 
                all_zero_clicks += 1
            q.appendleft(popped)
    elif direction == "R":
        for _ in range(n):
            popped = q.popleft()
            q.append(popped)
            if q[0] == 0:
                all_zero_clicks += 1
    return q, all_zero_clicks


input = read_input()
password = 0
all_zero_clicks = 0
for instruction in input:
    direction = instruction[0]
    n = int(instruction[1:])
    circular, all_zeros = mod_rotate(circular, n, direction)
    if circular[0] == 0:
        password += 1
    all_zero_clicks += all_zeros
    

print("part 1: ", password)
print("part 2: ", all_zero_clicks)
