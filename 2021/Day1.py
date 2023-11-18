from itertools import pairwise

with open('inputs/Day1.txt', 'r') as f:
    data = [int(x) for x in f.readlines()]

counter = 0

for a, b in pairwise(data):
    if b > a:
        counter += 1

print(counter)

# Part 2
counter = 0
for i, depth in enumerate(data):
    try:
        a = sum(data[i:i+3])
        b = sum(data[i+1:i+4])
    except IndexError:
        break
    if b > a:
        counter += 1

print(counter)
