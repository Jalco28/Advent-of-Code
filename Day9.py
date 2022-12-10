with open('Day9TestInput.txt', 'r') as f:
    moves = f.readlines()

moves = [move.strip('\n').split(" ") for move in moves]
head_pos = (0, 0)
tail_pos = (0, 0)
visited_places = {(0, 0)}
allowed_vectors = {"ul": (-1, -1), "um": (-1, 0), "ur": (-1, 1), "ml": (
    0, -1), "mr": (0, 1), "bl": (1, -1), "bm": (1, 0), "br": (1, 1), "mm": (0, 0)}


def tuple_addition(a, b):
    return tuple([sum(x) for x in zip(a, b)])


def tuple_subtraction(a, b):
    return tuple([x[0]-x[1] for x in zip(a, b)])


def do_move(direction):
    global head_pos, tail_pos, visited_places
    head_pos = tuple_addition(head_pos, allowed_vectors[direction])
    if tuple_subtraction(head_pos, tail_pos) not in allowed_vectors.values():
        match direction:
            case "um":
                tail_pos = tuple_addition(head_pos, allowed_vectors["bm"])
            case "bm":
                tail_pos = tuple_addition(head_pos, allowed_vectors["um"])
            case "ml":
                tail_pos = tuple_addition(head_pos, allowed_vectors["mr"])
            case "mr":
                tail_pos = tuple_addition(head_pos, allowed_vectors["ml"])
    visited_places.add(tuple(tail_pos))


translation = {"U": "um", "L": "ml", "R": "mr", "D": "bm"}
for move in moves:
    for i in range(int(move[1])):
        do_move(translation[move[0]])
print(len(visited_places))

# Part 2


# def do_move_multiple(direction):
#     global rope, visited_places
#     rope[0] = tuple_addition(rope[0], allowed_vectors[direction])
#     for i in range(len(rope)):
#         try:
#             difference = tuple_subtraction(rope[i], rope[i+1])
#             if difference not in allowed_vectors.values():
#                 match difference: #logic to check new postion of non-adjacent rope and move accordingly
#                     case ()
#         except IndexError:
#             pass
#     visited_places.add(rope[-1])


# rope = [(0, 0) for i in range(10)]
# visited_places = {(0, 0)}
# for move in moves:
#     for i in range(int(move[1])):
#         do_move_multiple(translation[move[0]])
# print(len(visited_places))
class Knot:
    def __init__(self):
        self.pos = (0, 0)
        last_moved_direction = (0, 0)

    def __repr__(self):
        return f"Knot at {self.pos}"

    def update_pos(self, direction):
        difference = tuple_subtraction(self.pos, self.head.pos)
        if difference not in allowed_vectors.values():
            pass

visited_places = {(0, 0)}
rope = [Knot() for i in range(10)]
for idx, knot in enumerate(rope):
    try:
        knot.head = rope[idx-1]
    except IndexError:
        knot.head = None
for idx, knot in enumerate(rope):
    try:
        knot.tail = rope[idx+1]
    except IndexError:
        knot.tail = None
print()
