with open('Day5Input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]
stacks = [[] for i in range(9)]
for i in range (8):
    if lines[i][1] != " ":
        stacks[0].append(lines[i][1])
    if lines[i][5] != " ":
        stacks[1].append(lines[i][5])
    if lines[i][9] != " ":
        stacks[2].append(lines[i][9])
    if lines[i][13] != " ":
        stacks[3].append(lines[i][13])
    if lines[i][17] != " ":
        stacks[4].append(lines[i][17])
    if lines[i][21] != " ":
        stacks[5].append(lines[i][21])
    if lines[i][25] != " ":
        stacks[6].append(lines[i][25])
    if lines[i][29] != " ":
        stacks[7].append(lines[i][29])
    if lines[i][33] != " ":
        stacks[8].append(lines[i][33])
def move(source, to):
    source = int(source)
    to = int(to)
    stacks[to-1].insert(0, stacks[source-1].pop(0))

for i in range(10,513):
    line = lines[i]
    line = line.split(" ")
    for i in range(int(line[1])):
        move(int(line[3]),int(line[5]))
# for item in stacks:
#     print(item[0])
# Part 2
stacks = [[] for i in range(9)]
for i in range (8):
    if lines[i][1] != " ":
        stacks[0].append(lines[i][1])
    if lines[i][5] != " ":
        stacks[1].append(lines[i][5])
    if lines[i][9] != " ":
        stacks[2].append(lines[i][9])
    if lines[i][13] != " ":
        stacks[3].append(lines[i][13])
    if lines[i][17] != " ":
        stacks[4].append(lines[i][17])
    if lines[i][21] != " ":
        stacks[5].append(lines[i][21])
    if lines[i][25] != " ":
        stacks[6].append(lines[i][25])
    if lines[i][29] != " ":
        stacks[7].append(lines[i][29])
    if lines[i][33] != " ":
        stacks[8].append(lines[i][33])

def move_multiple(source, to, number):
    source = int(source)
    to = int(to)
    number = int(number)
    indexs = list(range(0,number))[::-1]
    for index in indexs:
        stacks[to-1].insert(0, stacks[source-1].pop(index))
for i in range(10,513):
    line = lines[i]
    line = line.split(" ")
    move_multiple(int(line[3]),int(line[5]),int(line[1]))
for item in stacks:
    print(item[0], end='')
