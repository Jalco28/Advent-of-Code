from copy import copy

with open('inputs/Day16.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]


def tuple_addition(a, b):
    return tuple([sum(x) for x in zip(a, b)])


def print_old(old_beams):
    for row_idx in range(HEIGHT):
        for col_idx in range(WIDTH):
            print('#' if (row_idx, col_idx) in map(
                lambda x: x[:2], old_beams) else '.', end='')
        print()
    print()


def print_energised(energised_coords):
    for row_idx in range(HEIGHT):
        for col_idx in range(WIDTH):
            print('#' if (row_idx, col_idx) in energised_coords else '.', end='')
        print()
    print()


WIDTH = len(data[0])
HEIGHT = len(data)

grid = {}
for row_idx, row in enumerate(data):
    for col_idx, char in enumerate(row):
        grid[(row_idx, col_idx)] = char
UP = [(-1, 0)]
DOWN = [(1, 0)]
LEFT = [(0, -1)]
RIGHT = [(0, 1)]
rel_direction: dict[str, dict[str, list[tuple[int]]]] = {
    '.': {
        'u': UP,
        'd': DOWN,
        'l': LEFT,
        'r': RIGHT
    },
    '\\': {
        'u': LEFT,
        'd': RIGHT,
        'l': UP,
        'r': DOWN
    },
    '/': {
        'u': RIGHT,
        'd': LEFT,
        'l': DOWN,
        'r': UP
    },
    '|': {
        'u': UP,
        'd': DOWN,
        'l': UP+DOWN,
        'r': UP+DOWN
    },
    '-': {
        'u': LEFT+RIGHT,
        'd': LEFT+RIGHT,
        'l': LEFT,
        'r': RIGHT
    },
}
rel_tuple_to_dir = {
    (-1, 0): 'u',
    (1, 0): 'd',
    (0, -1): 'l',
    (0, 1): 'r'
}


def solve(old_beams):
    i = 0
    energised_coords = {old_beams[0][:2]}
    new_beams = []
    visited_beams = {old_beams[0]}
    while old_beams:
        while old_beams:
            row, col, direction = old_beams.pop()
            char = grid[(row, col)]
            curr_beams = rel_direction[char][direction]
            for beam in curr_beams:
                new_row, new_col = tuple_addition((row, col), beam)
                beam_pos_dir = (new_row, new_col, rel_tuple_to_dir[beam[:2]])
                # New coords out of bounds
                if (new_row not in range(HEIGHT)) or (new_col not in range(WIDTH)):
                    continue
                elif beam_pos_dir in visited_beams:
                    continue
                else:
                    new_beams.append(beam_pos_dir)
                    energised_coords.add((new_row, new_col))
                    visited_beams.add(beam_pos_dir)
        old_beams = list(set(copy(new_beams)))
        new_beams = []
        i += 1

    return len(energised_coords)


print(solve([(0, 0, 'r')]))
print()

# Part 2
start_beams = []
for row_idx in range(HEIGHT):
    start_beams.append([(row_idx, 0, 'r')])
    start_beams.append([(row_idx, WIDTH-1, 'l')])

for col_idx in range(WIDTH):
    start_beams.append([(0, col_idx, 'd')])
    start_beams.append([(HEIGHT-1, col_idx, 'u')])

print(max(solve(beam) for beam in start_beams))
