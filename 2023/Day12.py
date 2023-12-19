from copy import copy
from functools import cache

with open('inputs/Day12.txt') as f:
    data = [line.split() for line in f.readlines()]


@cache
def works(chars: str, digits: list[int]):
    brokens = []
    current = ''
    contains_q = False
    for char in chars:
        if char == '#':
            current += '#'
        elif char == '.':
            brokens.append(current)
            current = ''
        elif char == '?':
            contains_q = True
            break
    brokens = [broke for broke in brokens if broke != '']
    if char == '#' and not contains_q:  # Catch broken block at end
        brokens.append(current)

    if not contains_q:
        if len(brokens) != len(digits):
            return False
        for idx, broke in enumerate(brokens):
            if len(broke) != digits[idx]:
                return False
    else:
        for pattern, num in zip(brokens, digits):
            if len(pattern) != num:
                return False

    return True


@cache
def all_possible(chars: str, digits):
    to_eval = [chars]
    finals = []
    while to_eval:
        current = to_eval.pop()
        if not works(current, tuple(digits)):
            continue
        if current.count('?') != 0:
            to_eval.append(current.replace('?', '.', 1))
            to_eval.append(current.replace('?', '#', 1))
        else:
            finals.append(current)
    return finals


for idx, line in enumerate(copy(data)):
    chars, digits = line
    digits = [int(digit) for digit in digits.split(',')]
    data[idx] = [chars, tuple(digits)]

total = 0
for line in data:
    working_combinations = list(all_possible(line[0], line[1]))
    total += len(working_combinations)


print(total)
