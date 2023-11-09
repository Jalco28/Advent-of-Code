from functools import reduce
import string
letters = string.ascii_lowercase
class Node:
    def __init__(self, value, row, column) -> None:
        self.value = value
        self.row = row
        self.column = column
        self.distance = 999999999999999
        self.connected_to:list[Node] = []

    def define_connections(self, reverse:bool):
        allowed_vectors = [        (-1, 0),
                           (0, -1),        (0, 1),
                                   (1, 0)]
        for vector in allowed_vectors:
            absolute_coords = tuple_addition((self.row, self.column), (vector))
            if -1 in absolute_coords or 144 == absolute_coords[1] or 41 == absolute_coords[0]:
                continue
            if reverse:
                if check_height_difference_reverse(self.value, nodes[absolute_coords[0]][absolute_coords[1]].value):
                    self.connected_to.append(nodes[absolute_coords[0]][absolute_coords[1]])
            else:
                if check_height_difference(self.value, nodes[absolute_coords[0]][absolute_coords[1]].value):
                    self.connected_to.append(nodes[absolute_coords[0]][absolute_coords[1]])

    def define_neighbour_distance(self):
        for node in self.connected_to:
            if node.distance > self.distance+1:
                node.distance = self.distance+1

    def __repr__(self) -> str:
        return f'Node at({self.row}, {self.column})'


def check_height_difference(first, second):
    if first == 'S':
        first = 'a'
    elif first == 'E':
        first = 'z'
    if second == 'S':
        second = 'a'
    elif second == 'E':
        second = 'z'

    if second <= first or letters[letters.index(first)+1] == second:
        return True
    else:
        return False
def check_height_difference_reverse(first, second):
    if first == 'S':
        first = 'a'
    elif first == 'E':
        first = 'z'
    if second == 'S':
        second = 'a'
    elif second == 'E':
        second = 'z'

    if second >= first or letters[letters.index(first)-1] == second:
        return True
    else:
        return False


def tuple_addition(a, b):
    return tuple([sum(x) for x in zip(a, b)])


with open("Day12Input.txt", 'r') as f:
    data = f.readlines()
data = [list(line) for line in data]
nodes = [[Node(data[i][j], i, j) for j in range(144)]for i in range(41)]
for row in nodes:
    for node in row:
        node.define_connections(False)
for row_idx, row in enumerate(data):
    for letter_idx, letter in enumerate(row):
        if letter == 'S':
            START = nodes[row_idx][letter_idx]
        elif letter == 'E':
            END = nodes[row_idx][letter_idx]
START.distance=0
unvisited_nodes = list(reduce(lambda a,b:a+b, nodes))
while unvisited_nodes:
    best_node = None
    for node in unvisited_nodes:
        if best_node is None or best_node.distance > node.distance:
            best_node = node
    best_node.define_neighbour_distance()
    unvisited_nodes.remove(best_node)
print(END.distance)

#Part 2
for row in nodes:
    for node in row:
        node.distance = 999999999999999
        node.connected_to = []
        node.define_connections(True)
END.distance = 0
unvisited_nodes = list(reduce(lambda a,b:a+b, nodes))
while unvisited_nodes:
    best_node = None
    for node in unvisited_nodes:
        if best_node is None or best_node.distance > node.distance:
            best_node = node
    best_node.define_neighbour_distance()
    unvisited_nodes.remove(best_node)
lowest_distance = 999999999999999
for row in nodes:
    for node in row:
        if (node.value == 'a' or node.value == 'S') and node.distance < lowest_distance:
            lowest_distance = node.distance
print(lowest_distance)