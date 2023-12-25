from collections import defaultdict

with open('inputs/Day25.txt', 'r') as f:
    data = [[block.split(' ') for block in line.strip().split(': ')]
            for line in f.readlines()]
for idx, line in enumerate(data):
    data[idx] = line[0]+line[1]

graph = defaultdict(list)
for line in data:
    first = line[0]
    for second in line[1:]:
        graph[first].append(second)
        graph[second].append(first)
NUM_NODES = len(graph)


def explore(graph: defaultdict):
    queue = [next(iter(graph))]
    visited = set()
    while queue:
        curr = queue.pop()
        if curr in visited:
            continue
        visited.add(curr)
        for neighbour in graph[curr]:
            queue.append(neighbour)
    if len(visited) == NUM_NODES:
        return None
    return len(visited), NUM_NODES-len(visited)


# From graphiz (misc/Day25.png)
a1 = 'htb'
a2 = 'bbg'
b1 = 'pcc'
b2 = 'htj'
c1 = 'pjj'
c2 = 'dlk'

graph[a1].remove(a2)
graph[a2].remove(a1)

graph[b1].remove(b2)
graph[b2].remove(b1)

graph[c1].remove(c2)
graph[c2].remove(c1)
first, second = explore(graph)
print(first*second)
