import string
with open('Day3Input.txt','r') as f:
    bags = f.readlines()

bags = [bag.strip('\n') for bag in bags]

priorities = {}
for idx, letter in enumerate(string.ascii_letters):
    priorities[letter] = idx+1

total = 0
for bag in bags:
    first = bag[:int(len(bag)/2)]
    second = bag[int(len(bag)/2):]
    first = set(first)
    second = set(second)
    total += priorities[str(first.intersection(second))[2]]
# print(total)

#Part 2
total = 0
groups = []
line = 0
while line < 300:
    groups.append([bags[line], bags[line+1], bags[line+2]])
    line += 3
for group in groups:
    first = set(group[0])
    second = set(group[1])
    third = set(group[2])
    temp = first.intersection(second)
    final = temp.intersection(third)
    total += priorities[str(final)[2]]
print(total)