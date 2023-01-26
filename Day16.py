from collections import defaultdict


class Valve:
    def __init__(self, name, flow_rate) -> None:
        self.name: str = name
        self.flow_rate = int(flow_rate)
        self.connections: list[Valve] = []
        self.distance = 0
        self.distances = defaultdict(lambda: 0)

    def __repr__(self) -> str:
        return f'Valve {self.name}'


def bfs(root: Valve):
    queue: list[Valve] = [root]
    visited: list[Valve] = [root]
    root.distance = 0
    while queue:
        current_node = queue.pop(0)
        for connection in current_node.connections:
            if connection not in visited:
                connection.distance = current_node.distance + 1
                connection.distances[root.name] = connection.distance
                queue.append(connection)
                visited.append(connection)


def score(solution: dict):
    total = 0
    for valve, time_left in solution.items():
        total += valves[valve].flow_rate * time_left
    return total


with open("Day16TestInput.txt", 'r') as f:
    data = f.readlines()

data = [valve.strip('\n').split(" ") for valve in data]
valves = {}
for valve in data:
    valves[valve[1]] = Valve(valve[1], valve[4].split('=')[1][:-1])
for valve in data:
    connections = valve[9:]
    connections = [connection.strip(',') for connection in connections]
    for connection in connections:
        valves[valve[1]].connections.append(valves[connection])

for valve in valves.values():
    bfs(valve)
good_valves = dict(filter(lambda valve:valve[1].flow_rate > 0, valves.items()))
stack = [(30, 'AA', {})]
solutions = []
# time_left, current node, {open node:time left when opened}
while stack:
    state = stack.pop(0)
    time_left, current, opened = state
    if time_left < 2:
        solutions.append((opened))
        continue
    for node in good_valves.values():
        new_time = time_left - 1 - valves[current].distances[node.name]
        if new_time >= 0 and node.name not in opened.keys():
            stack.insert(0, (new_time, node.name,opened|{node.name:new_time}))
        else:
            solutions.append((opened))

print(max((score(solution)) for solution in solutions))



print()