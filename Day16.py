class Valve:
    def __init__(self, name, flow_rate) -> None:
        self.name: str = name
        self.flow_rate = int(flow_rate)
        self.connections: list[Valve] = []
        self.distance = 0
        self.score = 0
        self.open = False

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
                queue.append(connection)
                visited.append(connection)


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

time_left = 30
best = valves['AA']
pressure_released = 0
while time_left > 0:
    bfs(best)
    for valve in valves.values():
        valve.score = (time_left - (valve.distance+1)) * valve.flow_rate

    candidates = [valve for valve in valves.values() if not valve.open]
    candidates.sort(reverse=True, key=lambda x: x.score)
    for candidate in candidates:
        if time_left - (candidate.distance+1) >= 0:
            best = candidate
            break
    best.open = True
    pressure_released += best.score
    time_left -= best.distance+1

print()
