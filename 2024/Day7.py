from operator import add, mul
from typing import Callable


def conc(a, b):
    return int(str(a)+str(b))


# with open('inputs/test.txt', 'r') as f:
with open('inputs/Day7.txt', 'r') as f:
    data = [line.strip().split(':') for line in f.readlines()]

data = [[int(a), [int(num) for num in b.split()]] for a, b in data]


def eval(nums, ops: list[Callable[[int, int], int]]):
    total = ops[0](nums[0], nums[1])
    for idx, op in enumerate(ops[1:]):
        total = op(total, nums[idx+2])
    return total


counter = 0
for target, nums in data:
    q = [[add], [mul]]  # Part 1
    q = [[add], [mul], [conc]]  # Part 2
    while q:
        ops = q.pop()
        result = eval(nums, ops)
        if result <= target and len(ops) < len(nums)-1:
            q.append(ops+[add])
            q.append(ops+[mul])
            q.append(ops+[conc])  # Part 2
        elif result == target and len(ops) == len(nums)-1:
            counter += target
            break

print(counter)
