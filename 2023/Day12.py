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
# for line in data:
#     working_combinations = list(all_possible(line[0], line[1]))
#     total += len(working_combinations)


print(total)

# Part 2

@cache
def solve(chars: str, digits: tuple[int], current_block):
    if not chars:  # We've run out
        if len(digits) == 0 and current_block == 0:
            return 1
        elif len(digits) == 1 and digits[0] == current_block:
            return 1
        return 0

    if len(digits) > 0 and current_block > digits[0]:
        return 0  # Current block already to big
    if len(digits) == 0 and current_block > 0:
        return 0  # Making a block that isn't needed

    result = 0
    next_char = chars[0]
    if next_char in '#?':
        result += solve(chars[1:], digits, current_block+1)
    if next_char in '.?':
        if not current_block:
            result += solve(chars[1:], digits, 0)
        elif current_block == digits[0]:
            result += solve(chars[1:], digits[1:], 0)

    return result


def unfold(chars: str, digits: tuple[int]):
    chars = '?'.join([chars]*5)
    digits = list(digits)
    digits.extend(digits*4)
    return chars, tuple(digits)


edata = []
for line in data:
    edata.append(list(unfold(line[0], line[1])))

total = 0
for chars, digits in edata:
    total += solve(chars, digits, 0)

print(total)
