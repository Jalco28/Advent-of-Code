from itertools import pairwise


with open('inputs/Day9.txt', 'r') as f:
    histories = [list(map(int, line.split())) for line in f.readlines()]


def get_differences(line):
    differences = [line]
    curr_diff = line
    while set(curr_diff) != {0}:
        new = []
        for a, b in pairwise(curr_diff):
            new.append(b-a)
        curr_diff = new
        differences.append(curr_diff)
    return differences


def next_value(differences: list[list]):
    differences[-1].append(0)
    i = -2
    while True:
        try:
            differences[i].append(differences[i+1][-1]+differences[i][-1])
        except IndexError:
            break
        i -= 1
    return differences[0][-1]


total = 0
for row in histories:
    total += next_value(get_differences(row))

print(total)

# Part 2


def prev_value(differences: list[list]):
    differences[-1].insert(0, 0)
    i = -2
    while True:
        try:
            differences[i].insert(0, -differences[i+1][0]+differences[i][0])
        except IndexError:
            break
        i -= 1
    return differences[0][0]


total = 0
for row in histories:
    total += prev_value(get_differences(row))
print(total)
