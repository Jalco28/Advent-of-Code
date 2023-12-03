from functools import reduce
import operator


with open('inputs/Day3.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

coords_containing_digits = set()
SYMBOL_DELTAS = [(r, c) for r in range(-1, 2) for c in range(-1, 2)]
SYMBOL_DELTAS.remove((0, 0))


def tuple_addition(a, b):
    return tuple(sum(x) for x in zip(a, b))


def check_for_number(start_coord):
    r, c = start_coord
    if (not data[r][c].isdigit()) or (start_coord in coords_containing_digits):
        return 0
    num_coords = [start_coord]

    for i in range(1, 3):  # Search backwards
        try:
            if data[r][max(0, (c-i))].isdigit():
                num_coords.append((r, max(0, (c-i))))
            else:
                break
        except IndexError:  # Tried to search off the map
            break

    for i in range(1, 3):  # Search Forwards
        try:
            if data[r][c+i].isdigit():
                num_coords.append((r, c+i))
            else:
                break
        except IndexError:  # Tried to search off the map
            break
    num_coords = list(set(num_coords))
    num_coords.sort(key=lambda x: x[1])
    coords_containing_digits.update(num_coords)  # Inplace union
    number = int(reduce(operator.add, [data[coord[0]][coord[1]]
                                       for coord in num_coords]))
    return number


total = 0

for row_idx, row in enumerate(data):
    for col_idx, char in enumerate(row):
        if char == '.' or char.isdigit():
            continue
        else:
            for coord in (tuple_addition((row_idx, col_idx), delta) for delta in SYMBOL_DELTAS):
                total += check_for_number(coord)

print(total)

# Part 2
total = 0
for row_idx, row in enumerate(data):
    for col_idx, char in enumerate(row):
        if char == '*':
            coords_containing_digits = set()
            nums_for_gear = []
            for coord in (tuple_addition((row_idx, col_idx), delta) for delta in SYMBOL_DELTAS):
                nums_for_gear.append(check_for_number(coord))
            nums_for_gear = [num for num in nums_for_gear if num != 0]
            if len(nums_for_gear) != 2:
                continue
            gear_ratio = nums_for_gear[0]*nums_for_gear[1]
            total += gear_ratio
print(total)
