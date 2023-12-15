with open('inputs/Day14.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

cubes = set()
rounds = set()

for row_idx, row in enumerate(data):
    for col_idx, char in enumerate(row):
        if char == 'O':
            rounds.add((row_idx, col_idx))
        elif char == '#':
            cubes.add((row_idx, col_idx))

rounds = frozenset(rounds)
cubes = frozenset(cubes)


def push_up(rounds: frozenset, cubes: frozenset):
    rounds = set(rounds)

    ordered_rounds = sorted(list(rounds), key=lambda x: x[0])
    for round in ordered_rounds:
        row, col = round
        rounds.remove(round)
        while True:
            row -= 1
            if row < 0:
                break
            if (row, col) in cubes:
                break
            if (row, col) in rounds:
                break
        row += 1
        rounds.add((row, col))
    return frozenset(rounds)


rounds = push_up(rounds, cubes)

max_load = len(data)
total = 0
for row, col in rounds:
    total += max_load-row
print(total)

# Part 2

width = len(data[0])
height = len(data)

# width=height=3

coords = []  # Full grid of coords
for row_idx in range(height):
    current = []
    for col_idx in range(width):
        current.append((row_idx, col_idx))
    coords.append(current)

tcoords = []  # Grid of coords rotated clockwise
for col_idx in range(width):
    current = []
    for row_idx in range(height):
        current.insert(0, coords[row_idx][col_idx])
    tcoords.append(current)


tmap = {}  # Old coords to rotated coords
for row_idx, row in enumerate(tcoords):
    for col_idx, coord in enumerate(row):
        tmap[coord] = (row_idx, col_idx)


def rotate(coords):
    new_values = set()
    for coord in coords:
        new_values.add(tmap[coord])
    return frozenset(new_values)


cubes = set()
rounds = set()

for row_idx, row in enumerate(data):
    for col_idx, char in enumerate(row):
        if char == 'O':
            rounds.add((row_idx, col_idx))
        elif char == '#':
            cubes.add((row_idx, col_idx))
rounds = frozenset(rounds)
cubes = frozenset(cubes)

turns_done = 0
# State -> number of turns
seen_states = {(rounds, turns_done % 4): turns_done}
pushes_todo = 4000000000

while pushes_todo > 0:
    rounds = push_up(rounds, cubes)
    rounds = rotate(rounds)
    cubes = rotate(cubes)
    turns_done += 1

    pushes_todo -= 1

    if (rounds, turns_done % 4) in seen_states:
        loop_start = seen_states[(rounds, turns_done % 4)]
        loop_length = turns_done-loop_start
        loops_left = pushes_todo//loop_length
        pushes_todo -= loops_left*loop_length
        turns_done += loops_left*loop_length
    seen_states[(rounds, turns_done % 4)] = turns_done

max_load = len(data)
total = 0
for row, col in rounds:
    total += max_load-row
print(total)
