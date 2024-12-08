from itertools import combinations
from collections import defaultdict
from math import gcd


def tuple_sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def tuple_add(a, b):
    return tuple(sum(x) for x in zip(a, b))


def tuple_mul(tup, scalar):
    return tuple(a*scalar for a in tup)


def check_bounds(pos):
    row, col = pos
    if not (0 <= row <= len(data)-1) or not (0 <= col <= len(data[0])-1):
        return False
    return True


def unit_delta(delta):
    a, b = delta
    div = gcd(a, b)
    return (a//div, b//div)


with open('inputs/Day8.txt', 'r') as f:
    # with open('inputs/test.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

positions = defaultdict(set)

for row, line in enumerate(data):
    for col, char in enumerate(line):
        if char != '.':
            positions[char].add((row, col))

anti_nodes = set()
for antennas in positions.values():
    for a, b in combinations(antennas, 2):
        delta = tuple_sub(b, a)

        new_anti_node = tuple_sub(a, delta)
        if check_bounds(new_anti_node):
            anti_nodes.add(new_anti_node)

        new_anti_node = tuple_add(a, tuple_mul(delta, 2))
        if check_bounds(new_anti_node):
            anti_nodes.add(new_anti_node)
print(len(anti_nodes))

anti_nodes = set()
for antennas in positions.values():
    for a, b in combinations(antennas, 2):
        delta = unit_delta(tuple_sub(b, a))
        anti_nodes.add(a)
        anti_nodes.add(b)

        scalar = 1
        while True:
            new_anti_node = tuple_sub(a, tuple_mul(delta, scalar))
            scalar += 1
            if check_bounds(new_anti_node):
                anti_nodes.add(new_anti_node)
            else:
                break

        scalar = 1
        while True:
            new_anti_node = tuple_add(a, tuple_mul(delta, scalar))
            scalar += 1
            if check_bounds(new_anti_node):
                anti_nodes.add(new_anti_node)
            else:
                break

print(len(anti_nodes))
