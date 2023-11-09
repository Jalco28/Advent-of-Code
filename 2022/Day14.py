from itertools import pairwise

with open('Day14Input.txt', 'r') as f:
    rocks = f.readlines()
rocks = [rock.strip('\n').split(' -> ') for rock in rocks]
for rock_idx, rock in enumerate(rocks[:]):
    for coord_idx, coords in enumerate(rock):
        coords = coords.split(',')
        rocks[rock_idx][coord_idx] = (int(coords[1]), int(coords[0]))

leftest_column = 0
rightest_column = 999999999
lowest_row = 0
highest_row = 0
for rock in rocks:
    for point in rock:
        if point[1] > leftest_column:
            leftest_column = point[1]
        if point[1] < rightest_column:
            rightest_column = point[1]

        if point[0] > lowest_row:
            lowest_row = point[0]

width = leftest_column-rightest_column
height = lowest_row-highest_row
lowest_row += 2 #Part 2
points = {}


def set_points_between(a, b):
    if a[0] == b[0]:
        vector = a[1]-b[1]
        for i in range(1, abs(vector)):
            if vector < 0:
                points[(a[0], a[1]+i)] = '█'
            else:
                points[(a[0], a[1]-i)] = '█'
    elif a[1] == b[1]:
        vector = a[0]-b[0]
        for i in range(1, abs(vector)):
            if vector < 0:
                points[(a[0]+i, a[1])] = '█'
            else:
                points[(a[0]-i, a[1])] = '█'


def tuple_addition(a, b):
    return tuple([sum(x) for x in zip(a, b)])


for rock in rocks:
    for point_pair in pairwise(rock):
        points[point_pair[0]] = '█'
        points[point_pair[1]] = '█'
        set_points_between(*point_pair)
points[(lowest_row, leftest_column-500)] = '█'
points[(lowest_row, rightest_column+500)] = '█'
set_points_between((lowest_row, leftest_column-500), (lowest_row, rightest_column+500))
def print_map():
    for row in range(highest_row, lowest_row+1):
        for column in range(rightest_column, leftest_column+1):
            if (row, column) in points:
                print(points[(row, column)], end='')
            else:
                print('.', end='')
        print()
    print()
# print_map()
finished = False
sand_count = 0
while not finished:
    sand_position = (0, 500)
    at_rest = False
    while not at_rest:
        # if sand_position[0] > lowest_row:
        #     finished = True
        #     break
        if tuple_addition(sand_position, (1, 0)) not in points:
            sand_position = tuple_addition(sand_position, (1, 0))
        elif tuple_addition(sand_position, (1, -1)) not in points:
            sand_position = tuple_addition(sand_position, (1, -1))
        elif tuple_addition(sand_position, (1, 1)) not in points:
            sand_position = tuple_addition(sand_position, (1, 1))
        else:
            points[sand_position] = 'o'
            at_rest = True
            sand_count += 1
            # print_map()
    if (0,500) in points:
        finished = True

print_map()
print(sand_count)

print()