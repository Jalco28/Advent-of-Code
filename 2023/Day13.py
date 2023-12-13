from collections import defaultdict
from copy import deepcopy


with open('inputs/Day13.txt', 'r') as f:
    data = [group.split() for group in f.read().split('\n\n')]

# Reflection point n is between lines n and n+1
# Eg. RP 2 is between lines 2 and 3

memory = defaultdict(list)


def find_reflection(block, smudged=None):
    if smudged is not None:
        tup = tuple(smudged)
    else:
        tup = tuple(block)

    for rp in range(len(block)-1):
        before = list(reversed(block[:rp+1]))
        after = block[rp+1:]
        if all(a == b for a, b in zip(before, after)):
            try:
                old_rp = memory[tup]
            except KeyError:  # Not known in memory
                old_rp = -1
            if rp not in old_rp:
                # if smudged is None:  # Only remember values during part 1
                memory[tup].append(rp)
                return rp+1  # Rows before RP
    return 0


def transpose(block):
    width = len(block[0])
    height = len(block)
    final = []
    curr = ''
    for i in range(width):
        for j in reversed(range(height)):
            curr += block[j][i]
        final.append(curr)
        curr = ''
    return final


total = 0
for block in data:
    total += 100*find_reflection(block)

for tblock in (transpose(block) for block in data):
    total += find_reflection(tblock)

print(total)

# Part 2


def replace_str_char(string, char, idx):
    return string[:idx]+char+string[idx+1:]


TRANSLATE = {'#': '.', '.': '#'}
total = 0
for block in data:
    width = len(block[0])
    height = len(block)
    for row in range(height):
        for col in range(width):
            tempblock = deepcopy(block)
            tempblock[row] = replace_str_char(
                tempblock[row], TRANSLATE[tempblock[row][col]], col)
            result = 100*find_reflection(tempblock, block)
            total += result

for tblock in (transpose(block) for block in data):
    width = len(tblock[0])
    height = len(tblock)
    for row in range(height):
        for col in range(width):
            tempblock = deepcopy(tblock)
            tempblock[row] = replace_str_char(
                tempblock[row], TRANSLATE[tempblock[row][col]], col)
            result = find_reflection(tempblock, tblock)
            total += result
print(total)
