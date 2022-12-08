with open('Day8Input.txt', 'r') as f:
    trees = f.readlines()

trees = [list(line.strip('\n')) for line in trees]
for row_idx, row in enumerate(trees[:]):
    for column_idx, tree in enumerate(row):
        trees[row_idx][column_idx] = int(tree)
def tuple_addition(a,b):
    return [sum(x) for x in zip(a,b)]

def check_visibility(row, column, height, direction):
    position = (row, column)
    try:
        while True:
            position = tuple_addition(position, direction)
            if -1 in position:
                raise IndexError
            neighbour = trees[position[0]][position[1]]
            if neighbour >= height:
                return False
    except IndexError:
        return True
UP = (-1, 0)
DOWN =(1, 0)
LEFT =(0, -1)
RIGHT = (0, 1)

total = 0
for row_idx, row in enumerate(trees):
    for column_idx, tree in enumerate(row):
        if check_visibility(row_idx, column_idx, tree, UP) or check_visibility(row_idx, column_idx, tree, DOWN) or check_visibility(row_idx, column_idx, tree, LEFT) or check_visibility(row_idx, column_idx, tree, RIGHT):
            total += 1
print(total)
# Part 2
def check_viewing_distance(row, column, height, direction):
    position = (row, column)
    distance_looked = 0
    try:
        while True:
            position = tuple_addition(position, direction)
            if -1 in position:
                raise IndexError
            neighbour = trees[position[0]][position[1]]
            if neighbour >= height:
                return distance_looked+1
            distance_looked += 1
    except IndexError:
        return distance_looked

scores = []
for row_idx, row in enumerate(trees):
    for column_idx, tree in enumerate(row):
        distances = [check_viewing_distance(row_idx, column_idx, tree, UP), check_viewing_distance(row_idx, column_idx, tree, DOWN), check_viewing_distance(row_idx, column_idx, tree, LEFT), check_viewing_distance(row_idx, column_idx, tree, RIGHT)]
        scores.append(distances[0]*distances[1]*distances[2]*distances[3])
print(max(scores))