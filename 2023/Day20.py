from collections import defaultdict
from math import lcm


class FlipFlop:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
        self.on = False

    def high(self, sender):
        return []

    def low(self, sender):
        self.on = not self.on
        return [(dest, self.on, self.name) for dest in self.connections]


class Conjunction:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
        # Tuple-dict of self.memory -> last time seen
        self.memory_squared = {}

    def pulse(self, sender, high):
        self.memory[sender] = high
        # Nodes that connect to zp which connects to rx. Detected using graphiz
        if self.name in ['sb', 'nd', 'ds', 'hf']:
            self.check_memory_recognition()
        all_high = all(self.memory.values())
        if all_high:
            return [(dest, False, self.name) for dest in self.connections]
        else:
            return [(dest, True, self.name) for dest in self.connections]

    def check_memory_recognition(self):
        current_mem = tuple(self.memory.items())
        if current_mem in self.memory_squared:
            print(
                f'{self.name} recognises {current_mem} from {(loop_length := button_presses-self.memory_squared[current_mem])} ago')
            loop_lengths.append(loop_length)
        if all(not m for m in self.memory.values()):
            self.memory_squared[current_mem] = button_presses

    def high(self, sender):
        return self.pulse(sender, True)

    def low(self, sender):
        return self.pulse(sender, False)

    def set_inputs(self, inputs):
        self.memory = {module: False for module in inputs}


class Broadcast:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def low(self, sender):
        return [(dest, False, self.name) for dest in self.connections]

    def high(self, sender):
        return [(dest, True, self.name) for dest in self.connections]


class Dummy:
    def __init__(self):
        pass

    def low(self, sender):
        return []

    def high(self, sender):
        return []


with open('inputs/Day20.txt', 'r') as f:
    data = [line.strip().split(' -> ') for line in f.readlines()]
modules = defaultdict(Dummy)
con_inputs = {}
for curr, connections in data:
    connections = connections.split(', ')
    if curr == 'broadcaster':
        modules[curr] = Broadcast(curr, connections)
    else:
        module_type, name = curr[0], curr[1:]
        if module_type == '%':
            modules[name] = FlipFlop(name, connections)
        else:
            con_inputs[name] = []
            modules[name] = Conjunction(name, connections)


# Detect conjunction inputs after all nodes defined
for curr, connections in data:
    connections = connections.split(', ')
    if curr == 'broadcaster':
        for module in connections:
            if module in con_inputs.keys():
                con_inputs[module].append(curr)
    else:
        name = curr[1:]
        for module in connections:
            if module in con_inputs.keys():
                con_inputs[module].append(name)

for module, inputs in con_inputs.items():
    modules[module].set_inputs(inputs)

queue = []
loop_lengths = []
high_pulses = 0
low_pulses = 0
button_presses = 0
while True:
    if len(loop_lengths) == 4:  # Num of nodes attatched to binary counter zp which is attatched to rx
        break
    assert not queue
    queue.append(('broadcaster', False, 'button'))
    button_presses += 1
    while queue:
        dest, high, sender = queue.pop(0)
        # print(f'{sender} -{"high" if high else "low"}-> {dest}')
        if high:
            high_pulses += 1
            new_pulses = modules[dest].high(sender)
        else:
            low_pulses += 1
            new_pulses = modules[dest].low(sender)
        queue.extend(new_pulses)
    if button_presses == 1000:
        print(f'Part 1: {high_pulses*low_pulses}')
print(f'Part 2: {lcm(*loop_lengths)}')
