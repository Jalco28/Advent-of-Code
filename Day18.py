vectors = {(-1, 0, 0),
           (0, -1, 0),
           (0, 0, -1),
           (0, 0, 1),
           (0, 1, 0),
           (1, 0, 0)}


def tuple_addition(a, b):
    return tuple([sum(x) for x in zip(a, b)])


with open('Day18Input.txt', 'r') as f:
    cubes = f.readlines()

cubes = [cube.strip('\n').split(',') for cube in cubes]
cubes = [(int(cube[0]), int(cube[1]), int(cube[2])) for cube in cubes]
cubes = set(cubes)
counter = 0

for cube in cubes:
    temp = 6
    for vector in vectors:
        coords = tuple_addition(cube, vector)
        if coords in cubes:
            temp -= 1
    counter += temp
print(counter)

#Part 2

min_x = min(cube[0] for cube in cubes)
min_y = min(cube[1] for cube in cubes)
min_z = min(cube[2] for cube in cubes)
max_x = max(cube[0] for cube in cubes)
max_y = max(cube[1] for cube in cubes)
max_z = max(cube[2] for cube in cubes)
all_blocks = []
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        for z in range(min_z, max_z+1):
            all_blocks.append((x,y,z))
all_blocks = set(all_blocks)
air = all_blocks.difference(cubes)

outer_air = set()
queue = [(min_x,min_y,min_z)]
visited = {(min_x,min_y,min_z)}
while queue:
    current = queue.pop(0)
    outer_air.add(current)
    for vector in vectors:
        position = tuple_addition(vector, current)
        if position not in cubes.union(visited) and all([min_x<=position[0]<=max_x, min_y<=position[1]<=max_y, min_z<=position[2]<=max_z]):
            queue.append(position)
            visited.add(position)
inner_surfaces = 0
inner_air = air.difference(outer_air)
for current in inner_air:
    for vector in vectors:
        position = tuple_addition(current, vector)
        if position in cubes:
            inner_surfaces += 1
print(counter-inner_surfaces)
print()