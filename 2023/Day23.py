from collections import defaultdict, deque


with open('inputs/Day23.txt') as f:
    data = [line.strip() for line in f.readlines()]

START = 0+data[0].index('.')*1j
END = len(data)-1+data[-1].index('.')*1j
PEN = END-1


def get_char_at(pos: complex):
    row = int(pos.real)
    col = int(pos.imag)
    char = data[row][col]
    return char


arrow_deltas = {
    '>': [1j],
    '<': [-1j],
    '^': [-1],
    'v': [1]
}

final_lengths = []
# Current pos, visited, length
queue = [(START, {START}, 0)]
while queue:
    curr_pos, visited, curr_len = queue.pop()
    if curr_pos == END:
        final_lengths.append(curr_len)
        continue
    char = get_char_at(curr_pos)
    if char in arrow_deltas:
        allowed_deltas = arrow_deltas[char]
    elif curr_pos == PEN:
        allowed_deltas = [1]
    else:
        allowed_deltas = [1j, -1j, -1, 1]
    for delta in allowed_deltas[::]:
        new_pos = curr_pos+delta
        new_char = get_char_at(new_pos)
        if new_pos in visited or new_char == '#':
            allowed_deltas.remove(delta)
        elif new_char in arrow_deltas and delta == -1*arrow_deltas[new_char][0]:
            allowed_deltas.remove(delta)
    for delta in allowed_deltas:
        new_pos = curr_pos + delta
        new_visited = visited.union({new_pos})
        queue.append((new_pos, new_visited, curr_len+1))

print(max(final_lengths))

# Part 2
HEIGHT = len(data)
WIDTH = len(data[0])
nodes = [START, END]
visited = set()
queue = [START]
allowed_deltas = [1j, -1j, -1, 1]
while queue:
    pos = queue.pop()
    visited.add(pos)
    new_routes = 0
    for delta in allowed_deltas:
        new_pos = pos+delta
        if new_pos.real not in range(HEIGHT) or new_pos.imag not in range(WIDTH):
            continue
        if get_char_at(new_pos) == '#':
            continue
        new_routes += 1
        if new_pos in visited:
            continue

        queue.append(new_pos)
    if new_routes > 2:
        nodes.append(pos)
graph = defaultdict(dict)
for node in nodes:
    visited = set()
    queue = deque([(node, 0)])
    while queue:
        pos, depth = queue.popleft()
        visited.add(pos)
        if pos in nodes and depth != 0:
            graph[node][pos] = depth
            continue
        for delta in allowed_deltas:
            new_pos = pos+delta
            if new_pos.real not in range(HEIGHT) or new_pos.imag not in range(WIDTH):
                continue
            if get_char_at(new_pos) == '#':
                continue
            if new_pos in visited:
                continue

            queue.append((new_pos,depth+1))


best = 0
queue = [(START, set(), 0)]
while queue:
    pos, visited, depth = queue.pop()
    if pos == END:
        best = max(best, depth)
        continue
    for neighbour in graph[pos]:
        if neighbour in visited:
            continue
        queue.append((neighbour, visited.union({pos}), depth+graph[pos][neighbour]))

print(best)
print()
