from copy import copy
from itertools import combinations


# with open('inputs/test.txt', 'r') as f:
with open('inputs/Day11.txt', 'r') as f:
    data: list[str] = [line.strip() for line in f.readlines()]
orig_data = copy(data)
WIDTH = len(data[0])
HEIGHT = len(data)


def galaxy_set(data):
    galaxies = set()
    for row_idx, row in enumerate(data):
        for col_idx, char in enumerate(row):
            if char == '#':
                galaxies.add((row_idx, col_idx))
    return galaxies


def str_insert(string, idx, char):
    return string[:idx] + char + string[idx:]


empty_rows = []
for idx, row in enumerate(data):
    if set(row) == set('.'):
        empty_rows.append(idx)

for row in reversed(empty_rows):
    data.insert(row, '.'*WIDTH)

empty_columns = []
for column_idx in range(WIDTH):
    column = set(row[column_idx] for row in data)
    if column == set('.'):
        empty_columns.append(column_idx)

for column_idx in reversed(empty_columns):
    for idx, row in enumerate(data):
        data[idx] = str_insert(row, column_idx, '.')

galaxies = galaxy_set(data)
pairs = combinations(galaxies, 2)
total = 0
for pair in pairs:
    a, b = pair
    total += abs(a[0]-b[0])+abs(a[1]-b[1])

print(total)

# Part 2
# https://en.wikipedia.org/wiki/Hubble%27s_law#Determining_the_Hubble_constant
h0 = 1_000_000-1
data = orig_data

galaxies = galaxy_set(data)
for galaxy in copy(galaxies):
    row, col = galaxy
    row += h0 * len([empty_row for empty_row in empty_rows if empty_row < row])
    col += h0 * \
        len([empty_col for empty_col in empty_columns if empty_col < col])
    if (row, col) != galaxy:
        galaxies.remove(galaxy)
        galaxies.add((row, col))

pairs = combinations(galaxies, 2)

total = 0
for pair in pairs:
    a, b = pair
    total += abs(a[0]-b[0])+abs(a[1]-b[1])

print(total)
print()
