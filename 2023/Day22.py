from collections import defaultdict, deque


with open('inputs/Day22.txt', 'r') as f:
    data = [[[int(num) for num in row.split(',')]
             for row in line.strip().split('~')] for line in f.readlines()]
MIN = 0
MAX = 1
X = 0
Y = 1
Z = 2


def rests_on(static, mobile):
    """Determines horizontal overlap"""
    if static == mobile:
        return False
    xs, ys, zs = static
    xm, ym, zm = mobile
    vertically_close = zs[MAX]+1 == zm[MIN]

    if not vertically_close:
        return False

    if range_overlap(ys, ym) and range_overlap(xm, xs):
        return True
    else:
        return False


def range_overlap(a: list[int], b: list[int]):
    if a[MIN] <= b[MIN] <= a[MAX]:  # b min inside a
        return True
    if a[MIN] <= b[MAX] <= a[MAX]:  # b max inside a
        return True
    if b[MIN] <= a[MIN] <= b[MAX]:  # a min inside b
        return True
    if b[MIN] <= a[MAX] <= b[MAX]:  # a max inside b
        return True
    return False


def deep_tuple(x):
    return tuple(map(tuple, x))


mobile_bricks = []
static_bricks = []
for first, second in data:
    x = [first[0], second[0]]
    y = [first[1], second[1]]
    z = [first[2], second[2]]
    mobile_bricks.append([x, y, z])

# Reverse to allow O(1) popping of last item
mobile_bricks.sort(key=lambda x: x[-1][1], reverse=True)
resting_on = defaultdict(list)
while mobile_bricks:
    m_brick = mobile_bricks.pop()
    falling = True
    while falling:
        if m_brick[Z][MIN] == 1:
            falling = False
            m_tuple = deep_tuple(m_brick)
            break
        for s_brick in static_bricks:
            if rests_on(s_brick, m_brick):
                falling = False
                m_tuple = deep_tuple(m_brick)
                resting_on[m_tuple].append(s_brick)
        if falling:
            m_brick[Z] = list(map(lambda a: a-1, m_brick[Z]))

    static_bricks.append(m_tuple)

what_is_supported = defaultdict(list)
for base_brick in static_bricks:
    for variable_brick in static_bricks:
        if rests_on(base_brick, variable_brick):
            what_is_supported[base_brick].append(variable_brick)

redundant_count = 0
for brick in static_bricks:
    redundant = True
    for supported in what_is_supported[brick]:
        if len(resting_on[supported]) == 1:
            redundant = False
            break
    if redundant:
        redundant_count += 1

print(redundant_count)

# Part 2


def num_reliant(brick):
    result = -1
    bricks_moved = []
    queue = deque([brick])
    while queue:
        result += 1
        brick = queue.popleft()
        bricks_moved.append(brick)
        for supported in what_is_supported[brick]:
            num_bricks_supporting = 0
            for supporting_brick in resting_on[supported]:
                if supporting_brick not in bricks_moved:
                    num_bricks_supporting += 1
            if num_bricks_supporting == 0:
                queue.append(supported)
    return result


total = 0
for brick in static_bricks:
    total += num_reliant(brick)
print(total)
print()
