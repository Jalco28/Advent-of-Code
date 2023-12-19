from collections import defaultdict


# with open('inputs/test.txt', 'r') as f:
with open('inputs/Day10.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]


def tuple_addition(a, b):
    return tuple(sum(x) for x in zip(a, b))


MAX_INDEX = 139
NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

deltas = {
    '.': [],
    '-': [EAST, WEST],
    '|': [NORTH, SOUTH],
    'L': [NORTH, EAST],
    'J': [NORTH, WEST],
    '7': [SOUTH, WEST],
    'F': [SOUTH, EAST],
    'S': [SOUTH, WEST],  # For my input, S is a 7
    # 'S': [SOUTH, EAST], # For the test, S is an F
}

graph = defaultdict(set)
graph_distances = {}
for row_idx, row in enumerate(data):
    for col_idx, char in enumerate(row):
        current_coord = (row_idx, col_idx)
        if char == 'S':
            start_coord = current_coord
        for delta in deltas[char]:
            potential_coord = tuple_addition(current_coord, delta)
            if all(0 <= x <= MAX_INDEX for x in potential_coord):
                graph[current_coord].add(potential_coord)


def next_coord(current, prev):
    return [x for x in graph[current] if x != prev][0], current


steps = 1
c1, c2 = graph[start_coord]
p1 = p2 = start_coord
cycle = {start_coord}
while True:
    cycle.add(c1)
    cycle.add(c2)
    c1, p1 = next_coord(c1, p1)
    c2, p2 = next_coord(c2, p2)
    steps += 1
    if c1 == c2:
        cycle.add(c1)
        break
print(steps)

#Part 2
area = 0
for row_idx, row in enumerate(data):
    inside = False
    for col_idx, char in enumerate(row):
        if (row_idx, col_idx) in cycle:
            if char in '|LJ':
                inside = not inside
        elif inside:
            area += 1


print(area)
print()
