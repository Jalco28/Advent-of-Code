def print_map():
    for row in range(min_row, max_row+1):
        for column in range(min_col, max_col+1):
            print('#' if (row, column) in elves else '.', end='')
        print()

def tuple_addition(a, b):
    return tuple([sum(x) for x in zip(a, b)])

with open('Day23Input.txt', 'r') as f:
    data = f.read().split('\n')

directions = ['north', 'south', 'west', 'east']
first_direction = 0
vectors = [(-1, -1), (-1, 0), (-1, 1),
           (0, -1),           (0, 1),
           (1, -1),  (1, 0),  (1, 1)]

elves: set[tuple] = set()
for row_idx, row in enumerate(data):
    for column_idx, elf in enumerate(row):
        if elf == '#':
            elves.add((row_idx, column_idx))
i = 0
while True:
    i += 1
    proposed = {}
    direction_order = [(first_direction+i)%4 for i in range(4)]
    first_direction += 1
    for elf in elves:   #Create proposals
        occupied_spaces = any([tuple_addition(vector, elf) in elves for vector in vectors])
        if not occupied_spaces:
            continue
        for direction_index in direction_order:
            direction = directions[direction_index]
            if direction == "north" and all([tuple_addition(vector, elf) not in elves for vector in vectors[:3]]):
                proposed[elf] = tuple_addition(elf, (-1,0))
                break
            if direction == "south" and all([tuple_addition(vector, elf) not in elves for vector in vectors[5:]]):
                proposed[elf] = tuple_addition(elf, (1,0))
                break
            if direction == "west" and all([tuple_addition(vector, elf) not in elves for vector in [vectors[0]]+[vectors[3]]+[vectors[5]]]):
                proposed[elf] = tuple_addition(elf, (0,-1))
                break
            if direction == "east" and all([tuple_addition(vector, elf) not in elves for vector in [vectors[2]]+[vectors[4]]+[vectors[7]]]):
                proposed[elf] = tuple_addition(elf, (0,1))
                break
    # Detect and remove conflicting proposals
    duplicates = [value for value in proposed.items() if list(proposed.values()).count(value[1]) > 1]
    for duplicate in duplicates:
        proposed.pop(duplicate[0])

    #Do moves
    if len(proposed) == 0:
        print(i)
        break
    for proposal in proposed.items():
        elves.remove(proposal[0])
        elves.add(proposal[1])

min_row = min([elf[0] for elf in elves])
min_col = min([elf[1] for elf in elves])
max_row = max([elf[0] for elf in elves])
max_col = max([elf[1] for elf in elves])

area = (abs(max_col-min_col)+1)*(abs(max_row-min_row)+1)
# print_map()
# print(area-len(elves))


print()
