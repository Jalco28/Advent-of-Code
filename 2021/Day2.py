with open('inputs/Day2.txt', 'r') as f:
    data = [line.strip().split(' ') for line in f.readlines()]

horizontal = depth = 0

for direction, delta in data:
    delta = int(delta)
    if direction == 'forward':
        horizontal += delta
    elif direction == 'down':
        depth += delta
    elif direction == 'up':
        depth -= delta

print(horizontal*depth)

# Part 2

horizontal = depth = aim = 0

for direction, delta in data:
    delta = int(delta)
    if direction == 'forward':
        horizontal += delta
        depth += aim*delta
    elif direction == 'down':
        aim += delta
    elif direction == 'up':
        aim -= delta

print(horizontal*depth)
