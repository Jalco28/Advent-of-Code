from itertools import pairwise
import numpy as np

with open('inputs/Day18.txt', 'r') as f:
    data = [line.split() for line in f.readlines()]

deltas = {
    'U': -1,
    'D': 1,
    'L': -1j,
    'R': 1j
}

trench = {0}
curr_coord = 0+0j
min_row = float('inf')
max_row = -float('inf')

min_col = float('inf')
max_col = -float('inf')

# curr_coord.real = row, curr_coord.image = col
for direction, distance, _ in data:
    delta = deltas[direction]
    for i in range(int(distance)):
        curr_coord += delta
        trench.add(curr_coord)

        min_row = min(min_row, int(curr_coord.real))
        max_row = max(max_row, int(curr_coord.real))

        min_col = min(min_col, int(curr_coord.imag))
        max_col = max(max_col, int(curr_coord.imag))

min_row -= 1
min_col -= 1
max_row += 1
max_col += 1
top_left = min_row+min_col*1j
bottom_right = max_row+max_col*1j

width = (max_col-min_col)+1
height = (max_row-min_row)+1
box_area = width*height
visited = set()
q = [bottom_right]
while q:
    current_node = q.pop()
    visited.add(current_node)
    for delta in deltas.values():
        new_coords = current_node+delta
        if new_coords not in visited and new_coords not in trench and new_coords.real in range(min_row, max_row+1) and new_coords.imag in range(min_col, max_col+1):
            q.append(new_coords)

print(box_area-len(visited))

# Part 2
num_to_direction = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}
instructions = []
for *_, hex_code in data:
    hex_code = hex_code[2:-1]
    distance = int(hex_code[:-1], 16)
    direction = num_to_direction[hex_code[-1]]
    instructions.append((direction, distance))

curr_coord: complex = 0+0j
rows = [0]
cols = [0]

for direction, distance in instructions:
    curr_coord += distance*deltas[direction]
    rows.append(int(curr_coord.real))
    cols.append(int(curr_coord.imag))

# Shoelace algorithm, thanks internet
sl_area = 0

# Find perimiter
perimeter = 0

# rows = [0, 0, 2, 2, 0]
# cols = [0, 2, 2, 0, 0]

for (r1, c1), (r2, c2) in pairwise(zip(rows, cols, strict=True)):
    if r1 == r2:
        perimeter += abs(c2-c1)+1
    else:
        perimeter += abs(r2-r1)+1
    matrix = np.array([[r1, r2], [c1, c2]])
    sl_area += np.linalg.det(matrix)

sl_area = abs(sl_area/2)
# Every vertex was counted twice
perimeter -= len(rows)-1

result = sl_area + (perimeter//2) + 1
print(result)
