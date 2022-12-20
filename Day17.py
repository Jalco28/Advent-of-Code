from itertools import cycle

class State:
    def __init__(self, rock, wind_index, rock_count, highest_row) -> None:
        self.rock = rock
        self.wind_index = wind_index
        self.rock_count = rock_count
        self.highest_row = highest_row
    def __eq__(self, other) -> bool:
        return (self.rock, self.wind_index) == (other.rock, other.wind_index)

def tuple_addition(a, b):
    return tuple([sum(x) for x in zip(a, b)])


def push_right(a):
    return tuple_addition(a, (1, 0))


def push_left(a):
    return tuple_addition(a, (-1, 0))


def push_down(a):
    return tuple_addition(a, (0, -1))


def print_map():
    for row in range(highest_row+6):
        y = (highest_row+6) - row
        for x in range(1, 8):
            if (x, y) in points:
                print('#', end='')
            elif (x, y) in moving_points:
                print('@', end='')
            else:
                print('.', end='')
        print()
    print('-'*7, end='\n\n')


with open("Day17Input.txt", 'r') as f:
    wind = cycle(f.readline().strip('\n'))
wind_index = -1
rock_count = -1
rocks = ['-', '+', 'L', '|', '.']
cycle_found = False
rocks = cycle(rocks)
clock = cycle(['push', 'fall'])
highest_row = 0
points = set()
seen_states = []
for i in range(1000000000000):
    if points:
        highest_row = max(point[1] for point in points)
    else:
        highest_row = 0
    # points = set(filter(lambda x: x[1]>(highest_row-50), points))
    clock = cycle(['push', 'fall'])
    moving_points = set()
    rock = next(rocks)
    rock_count += 1

    lower_left = (3, highest_row+4)
    if rock == '-':
        moving_points.add(lower_left)
        moving_points.add(tuple_addition(lower_left, (1, 0)))
        moving_points.add(tuple_addition(lower_left, (2, 0)))
        moving_points.add(tuple_addition(lower_left, (3, 0)))
    elif rock == '+':
        moving_points.add(tuple_addition(lower_left, (1, 0)))
        moving_points.add(tuple_addition(lower_left, (0, 1)))
        moving_points.add(tuple_addition(lower_left, (1, 1)))
        moving_points.add(tuple_addition(lower_left, (2, 1)))
        moving_points.add(tuple_addition(lower_left, (1, 2)))
    elif rock == 'L':
        moving_points.add(lower_left)
        moving_points.add(tuple_addition(lower_left, (1, 0)))
        moving_points.add(tuple_addition(lower_left, (2, 0)))
        moving_points.add(tuple_addition(lower_left, (2, 1)))
        moving_points.add(tuple_addition(lower_left, (2, 2)))
    elif rock == '|':
        moving_points.add(lower_left)
        moving_points.add(tuple_addition(lower_left, (0, 1)))
        moving_points.add(tuple_addition(lower_left, (0, 2)))
        moving_points.add(tuple_addition(lower_left, (0, 3)))
    elif rock == '.':
        moving_points.add(lower_left)
        moving_points.add(tuple_addition(lower_left, (0, 1)))
        moving_points.add(tuple_addition(lower_left, (1, 1)))
        moving_points.add(tuple_addition(lower_left, (1, 0)))
    # print_map()
    # print(highest_row)
    new_rock = True
    if cycle_found:
        if (1000000000000 - rock_count)%rocks_per_cycle == 0:
            cycles_left = (1000000000000 - rock_count)/rocks_per_cycle
            print(int(highest_row + (cycles_left*height_per_cycle)))
            break

    while True:
        # print_map()
        move = next(clock)
        move_allowed = True
        if move == 'push':
            direction = next(wind)
            wind_index += 1
            wind_index = wind_index%10091
            current_state = State(rock, wind_index, rock_count, highest_row)
            if new_rock and not cycle_found:
                if current_state in seen_states and rock_count > 2000:
                    matching_state = list(filter(lambda x: x == current_state, seen_states))[0]
                    height_per_cycle = current_state.highest_row - matching_state.highest_row
                    rocks_per_cycle = current_state.rock_count - matching_state.rock_count
                    cycle_found = True
                else:
                    seen_states.append(current_state)
                new_rock = False

            if direction == '>':
                for point in moving_points:
                    new_point = push_right(point)
                    if new_point[0] == 8 or new_point in points:
                        move_allowed = False
                        break

                if not move_allowed:
                    continue
                else:
                    temp = set()
                    for point in moving_points:
                        temp.add(push_right(point))
                    moving_points = temp

            elif direction == '<':
                for point in moving_points:
                    new_point = push_left(point)
                    if new_point[0] == 0 or new_point in points:
                        move_allowed = False
                        break

                if not move_allowed:
                    continue
                else:
                    temp = set()
                    for point in moving_points:
                        temp.add(push_left(point))
                    moving_points = temp

        elif move == 'fall':
            for point in moving_points:
                new_point = push_down(point)
                if new_point in points or new_point[1] == 0:
                    move_allowed = False
                    break

            if not move_allowed:
                points = points.union(moving_points)
                break
            else:
                temp = set()
                for point in moving_points:
                    temp.add(push_down(point))
                moving_points = temp

# print(highest_row)
print()
