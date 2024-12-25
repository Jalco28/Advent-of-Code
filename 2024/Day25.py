with open('inputs/Day25.txt', 'r') as f:
    # with open('inputs/test.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

schems = [set()]

row = 0
for line in data:
    if line == '':
        row = 0
        schems.append(set())
        continue
    for col, char in enumerate(line):
        if char == '#':
            schems[-1].add((row, col))
    row += 1

counter = 0
for schem1 in schems:
    for schem2 in schems:
        if schem1.isdisjoint(schem2):
            counter += 1

counter = counter//2
print(counter)
