from itertools import combinations, product
from math import isclose

with open('inputs/Day24.txt', 'r') as f:
    data = [[int(point.strip()) for point in line.strip().replace(
        '@', ',').split(',')] for line in f.readlines()]


def is_forwards(x, y, sx, sy, dx, dy):
    # Is (x+dx, y+dy) closer to (sx,sy) than (x,y)?
    # ie are we stepping towards it
    return abs(x-(sx+dx)) <= abs(x-sx) and abs(y-(sy+dy)) <= abs(y-sy)


def solve(stones, p2=False):
    # m = dy/dx
    # y-y1 = m(x-x1)
    # y= mx - mx1 + y1
    # c = -mx1 + y1
    # [(m,c, startx, starty)]
    equations = []
    for x, y, _, dx, dy, _ in stones:
        m = dy/dx
        c = -m*x + y
        equations.append((m, c, x, y, dx, dy))

    total = 0
    intersections = []
    # m1x+c1 = m2x+c2
    # m1x = m2x +c2-c1
    # m1x-m2x = c2-c1
    # x(m1-m2) = c2-c1
    # x = (c2-c1)/(m1-m2)
    for eq1, eq2 in combinations(equations, 2):
        m1, c1, sx1, sy1, dx1, dy1 = eq1
        m2, c2, sx2, sy2, dx2, dy2 = eq2

        try:
            x_collision = (c2-c1)/(m1-m2)
        except ZeroDivisionError:  # No intersection
            continue

        y_collision = m1*x_collision + c1
        if not (200000000000000 <= x_collision <= 400000000000000 and 200000000000000 <= y_collision <= 400000000000000):
            # if not (7 <= x_collision <= 27 and 7 <= y_collision <= 27):
            continue

        if (not is_forwards(x_collision, y_collision, sx1, sy1, dx1, dy1)) or (not is_forwards(x_collision, y_collision, sx2, sy2, dx2, dy2)):
            continue
        total += 1
        intersections.append((x_collision, y_collision))

    if p2:
        return intersections
    else:
        return total


print(solve(data))
# Part 2


def all_xy_vectors():
    max_val = 500   # Think I got lucky with my input having smaller numbers so it takes less time
    vals = []
    for x, y in product(range(-max_val, max_val), range(-max_val, max_val)):
        vals.append((x, y))
    vals.sort(key=lambda x: sum(map(abs, x)))   # Search outwards
    for val in vals:
        yield val


# Number of lines that should match before we consider this the answer (max 300)
MIN_CONFIDENCE = 5
idxs_reached = set()
for rv_x, rv_y in all_xy_vectors():
    adjusted_stones = []
    for idx, stone in enumerate(data):
        if idx >= MIN_CONFIDENCE:
            continue
        if stone[3]-rv_x == 0:
            continue  # Would cause line with infinite gradient, lets pretend it doesn't exist
        adjusted_stones.append(
            [stone[0], stone[1], stone[2], stone[3]-rv_x, stone[4]-rv_y, stone[5]])
        intersection_points = solve(adjusted_stones, True)
        # Checks if the intersection points are all "close" to allow for floating point error
        if (any(not isclose(intersection_points[0][0], x) for x, _ in intersection_points) or any(not isclose(intersection_points[0][1], y) for _, y in intersection_points)) and idx != 0:
            idxs_reached.add(idx)
            break  # Stop checking stones for this vel
    else:
        idxs_reached.add(idx)
        intersection = list(map(round, intersection_points[0]))
        break

h1, h2 = adjusted_stones[:2]

t1 = (intersection[0]-h1[0])/h1[3]
t2 = (intersection[0]-h2[0])/h2[3]
dz = (h1[2]-h2[2] + t1*h1[5]-t2*h2[5])/(t1-t2)
z = h1[2] + t1*(h1[5]-dz)

print(f'x: {intersection[0]}')
print(f'y: {intersection[1]}')
print(f'z: {z}')
print(f'Total: {round(sum(intersection) + z)}')
