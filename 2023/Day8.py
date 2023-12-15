from itertools import cycle
from math import lcm


with open('inputs/Day8.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

directions = cycle(data[0])
definitions = data[2:]
nodes = {}
for line in definitions:
    line = line.split()
    nodes[line[0]] = (line[2][1:-1], line[3][:-1])

current_node = 'AAA'
steps = 0
while True:
    direction = next(directions)
    if direction == 'L':
        current_node = nodes[current_node][0]
    elif direction == 'R':
        current_node = nodes[current_node][1]
    else:
        raise ValueError
    steps += 1
    if current_node == 'ZZZ':
        break
print(steps)

# Part 2


start_nodes = [node for node in nodes.keys() if node[-1] == 'A']

loop_lengths = []
for start in start_nodes:
    current_node = start
    steps = 0
    directions = cycle(data[0])
    while True:
        direction = next(directions)
        if direction == 'L':
            current_node = nodes[current_node][0]
        elif direction == 'R':
            current_node = nodes[current_node][1]
        else:
            raise ValueError
        steps += 1
        if current_node[-1] == 'Z':
            break
    loop_lengths.append(steps)

print(lcm(*loop_lengths))
