from heapq import heappush, heappop
from collections import defaultdict

with open('inputs/Day17.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]


def tuple_addition(a, b):
    return tuple(sum(x) for x in zip(a, b))


def get_heat(row, col):
    return int(data[row][col])


WIDTH = len(data[0])
HEIGHT = len(data)
target_coords = (HEIGHT-1, WIDTH-1)

# state = (total_heat_loss, id(position), position, direction, straight_moves)
queue = [(get_heat(pos[0], pos[1]), id(pos), pos, pos, 1)
         for pos in [(0, 1), (1, 0)]]
tentatives = defaultdict(lambda: float('inf'))

while queue:
    heat_loss, _, curr_pos, motion, straight_moves = heappop(queue)
    if curr_pos == target_coords:
        print(heat_loss)
        break
    new_rel_pos = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    inverse_motion = tuple(x*-1 for x in motion)
    new_rel_pos.remove(inverse_motion)  # Can't go back
    if straight_moves >= 3:
        new_rel_pos.remove(motion)  # Can't go forward any more

    for rel_pos in new_rel_pos:
        forwards = rel_pos == motion
        new_straight = 1 if not forwards else straight_moves+1
        new_pos = tuple_addition(curr_pos, rel_pos)
        if new_pos[0] in range(HEIGHT) and new_pos[1] in range(WIDTH):
            new_heat_loss = heat_loss+get_heat(new_pos[0], new_pos[1])
            if new_heat_loss < tentatives[(new_pos, rel_pos, new_straight)]:
                heappush(queue, (new_heat_loss, id(new_pos),
                         new_pos, rel_pos, new_straight))
                tentatives[(new_pos, rel_pos, new_straight)] = new_heat_loss

# Part 2


# state = (total_heat_loss, id(position), position, direction, straight_moves)
queue = [(get_heat(pos[0], pos[1]), id(pos), pos, pos, 1)
         for pos in [(0, 1), (1, 0)]]
tentatives = defaultdict(lambda: float('inf'))

while queue:
    heat_loss, _, curr_pos, motion, straight_moves = heappop(queue)
    if curr_pos == target_coords and straight_moves >= 4:
        print(heat_loss)
        break

    if straight_moves < 4:
        new_rel_pos = [motion]
    else:
        new_rel_pos = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        inverse_motion = tuple(x*-1 for x in motion)
        new_rel_pos.remove(inverse_motion)  # Can't go back
        if straight_moves >= 10:
            new_rel_pos.remove(motion)  # Can't go forward any more

    for rel_pos in new_rel_pos:
        forwards = rel_pos == motion
        new_straight = 1 if not forwards else straight_moves+1
        new_pos = tuple_addition(curr_pos, rel_pos)
        if new_pos[0] in range(HEIGHT) and new_pos[1] in range(WIDTH):
            new_heat_loss = heat_loss+get_heat(new_pos[0], new_pos[1])
            if new_heat_loss < tentatives[(new_pos, rel_pos, new_straight)]:
                heappush(queue, (new_heat_loss, id(new_pos),
                         new_pos, rel_pos, new_straight))
                tentatives[(new_pos, rel_pos, new_straight)] = new_heat_loss
