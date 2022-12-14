with open('Day9Input.txt', 'r') as f:
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

#Part 2
values_map = {-2:-1, -1:-1, 0:0, 1:1, 2:1}
visited_places = {(0, 0)}
rope = [(0,0) for i in range(10)]
def calculate_tail_pos(head, tail):
    if tuple_subtraction(head, tail) not in allowed_vectors.values():
        vector = tuple_subtraction(head, tail)
        vector = tuple(values_map[value] for value in vector)
        return tuple_addition(tail, vector)
    else:
        return tail
for move in moves:
    for i in range(int(move[1])):
        rope[0] = tuple_addition(rope[0], allowed_vectors[translation[move[0]]])
        for knot_idx, knot in enumerate(rope):
            if knot_idx == 0:
                continue
            rope[knot_idx] = calculate_tail_pos(rope[knot_idx-1], knot)
            if knot_idx == 9:
                visited_places.add(knot)
print(len(visited_places)+1)