from functools import reduce
from itertools import combinations


def inbetween_check(num, lower, upper):
    if lower <= num <= upper:
        return True
    else:
        return False


def get_blocked_spots(origin: tuple, distance, row):
    vertical = row-origin[0]
    horizontal = distance - abs(vertical)
    if abs(vertical) > distance:
        return []
    start = origin[1]-horizontal
    end = origin[1]+horizontal
    # return set(range(start, end+1))
    return (start, end)


def get_distance(a: tuple, b: tuple):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


# WANTED_ROW = 10
WANTED_ROW = 2_000_000
with open("Day15Input.txt", 'r') as f:
    sensors = f.readlines()

sensors = [sensor.strip("\n").split(" ") for sensor in sensors]
sensors = [[(int(sensor[3][2:-1]), int(sensor[2][2:-1])),
            (int(sensor[9][2:]), int(sensor[8][2:-1]))] for sensor in sensors]

blocked_spots = set()
for sensor in sensors:
    blocked_spots = blocked_spots.union(get_blocked_spots(
        sensor[0], get_distance(sensor[0], sensor[1]), WANTED_ROW))
for sensor in sensors:
    if (sensor[1][0] == WANTED_ROW) and (sensor[1][1] in blocked_spots):
        blocked_spots.remove(sensor[1][1])

print(len(blocked_spots))

# Part 2
LOWER_SEARCH_BOUND = 0
UPPER_SEARCH_BOUND = 4000000
for row in range(UPPER_SEARCH_BOUND):
    intervals = []
    for sensor in sensors:
        x = get_blocked_spots(
            sensor[0], get_distance(sensor[0], sensor[1]), row)

        if x != []:
            if x[0] < 0:
                x = (0,x[1])
            if x[1] > UPPER_SEARCH_BOUND:
                x = (x[0], UPPER_SEARCH_BOUND)
            if x[0]>x[1]:
                x = []
            if x != []:
                intervals.append(x)
    changes_made = True
    while changes_made:
        changes_made = False
        for pair in combinations(intervals, 2):
            x,y=pair
            if inbetween_check(x[0], *y) or inbetween_check(x[1], *y) or inbetween_check(y[0], *x) or inbetween_check(y[1], *x) or y[1]+1 == x[0] or x[1]+1 == y[0]:
                changes_made = True
                new = sorted(pair[0]+pair[1])
                new.pop(1)
                new.pop(1)
                intervals.append(tuple(new))
                intervals.remove(pair[0])
                intervals.remove(pair[1])
                break
    if len(intervals) != 1:
        print(f'{row=}')
        print(intervals)
    # print(intervals)

print()
