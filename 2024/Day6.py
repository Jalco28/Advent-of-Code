# with open('inputs/test.txt', 'r') as f:
with open('inputs/Day6.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

direction_change = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP
}


def tuple_addition(a, b):
    return tuple(sum(x) for x in zip(a, b))


def explore(map, pos, part):
    direction = UP
    visited = {(pos, direction)}
    while True:
        new_pos = tuple_addition(pos, direction)
        try:
            if (new_pos, direction) in visited:  # We in loop!
                if part == 2:
                    return True
            if map[new_pos] == '#':
                direction = direction_change[direction]
                continue
            if map[new_pos] in '.^':
                pos = new_pos
                visited.add((pos, direction))

        except KeyError:
            if part == 1:
                unique_visited = set()
                for pos, _ in visited:
                    unique_visited.add(pos)
                return unique_visited
            else:
                return False


map = {}
for row, line in enumerate(data):
    for col, char in enumerate(line):
        map[(row, col)] = char
        if char == '^':
            start_pos = (row, col)


unique_visited = explore(map, start_pos, 1)
print(len(unique_visited))

# Part 2
counter = 0
for row, col in unique_visited:
    if map[(row, col)] != '.':
        continue
    new_map = map | {(row, col): '#'}
    if explore(new_map, start_pos, 2):
        counter += 1

print(counter)
