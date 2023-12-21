from functools import cache
from collections import deque

with open('inputs/Day21.txt', 'r') as f:
    # with open('inputs/test.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

WIDTH = len(data[0])
HEIGHT = len(data)

rocks = set()
for row_idx, row in enumerate(data):
    for col_idx, char in enumerate(row):
        if char == '#':
            rocks.add(row_idx+col_idx*1j)
        elif char == 'S':
            start_pos = row_idx + col_idx*1j

neighbours = [1, -1, 1j, -1j]
finals = set()
seen_states = set()


def explore(pos, depth):
    if (pos, depth) in seen_states:
        return
    seen_states.add((pos, depth))
    if depth == 64:
        finals.add(pos)
        return
    for new_pos in (pos+neighbour for neighbour in neighbours):
        if new_pos in rocks:
            continue
        elif 0 <= new_pos.real <= HEIGHT and 0 <= new_pos.imag <= WIDTH:
            explore(new_pos, depth+1)


# explore(start_pos, 0)
# print(len(finals))

# Part 2


@cache
def normalise_pos(pos):
    return pos.real % HEIGHT + pos.imag % WIDTH*1j


finals = set()
seen_states = set()
STEPS = 100
queue = deque([(start_pos, 0)])


def explore_p2(pos, depth):
    # if (pos, depth) in seen_states:
    #     return
    seen_states.add((pos, depth))
    if depth == STEPS:
        finals.add(pos)
        return
    for new_pos in (pos+neighbour for neighbour in neighbours):
        wrapped_pos = normalise_pos(new_pos)
        if (wrapped_pos in rocks) or ((new_pos, depth+1) in seen_states):
            continue
        else:
            explore_p2(new_pos, depth+1)


def solve_p2(steps):
    finals = set()
    seen_states = set()
    queue = deque([(start_pos, 0)])
    while queue:
        pos, depth = queue.pop()
        seen_states.add((pos, depth))
        if depth == steps:
            finals.add(pos)
            continue
        for new_pos in (pos+neighbour for neighbour in neighbours):
            wrapped_pos = normalise_pos(new_pos)
            # if wrapped_pos == start_pos and pos != start_pos:
            #     print(f'start_pos reached after {depth+1} steps ')
            if (wrapped_pos in rocks) or ((new_pos, depth+1) in seen_states):
                continue
            else:
                queue.append((new_pos, depth+1))
    return len(finals)


cycle_offset = 26501365 % WIDTH

# for i in range(0, 4):
#     print(solve_p2(cycle_offset+i*WIDTH))

# After much waiting, this gives 3752, 33614, 93252, 182666
# These have a constant second difference of 29776
# Using old fashioned pen and paper (misc/day10.png)
# we find the sequence: plots_reached = 14888x^2 - 14802x + 3666. Where x is a natrual number representing how many (lots of grid_sizes) + cycle offset of steps we have taken
# for example, x=1; 1488x^2 + 204x + 1 = 15093. This represents that after 1*grid_size steps we reach 15093 steps
# we want to find after 26501365 steps so we do ceil(26501365/grid_size) which gives 202301
# plugging that in as x gives us plots_reached = 609298746763952
