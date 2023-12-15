from collections import defaultdict
from copy import copy


with open('inputs/Day15.txt', 'r') as f:
    data = f.read().split(',')


def hash_algo(chars):
    total = 0
    for char in chars:
        total += ord(char)
        total *= 17
        total %= 256
    return total


total = 0
for instruction in data:
    total += hash_algo(instruction)

print(total)

# Part 2

boxes = defaultdict(list)

for instruction in data:
    if '-' in instruction:
        lens_label = instruction[:-1]
        box_no = hash_algo(lens_label)
        boxes[box_no] = [lens for lens in boxes[box_no] if lens[0] != lens_label]
    else:
        lens_label, focal_length = instruction.split('=')
        focal_length = int(focal_length)
        box_no = hash_algo(lens_label)
        for idx, lens in enumerate(boxes[box_no]):
            if lens[0] == lens_label:
                boxes[box_no][idx] = (lens_label, focal_length)
                break
        else:
            boxes[box_no].append((lens_label, focal_length))

total_fp = 0
for box_no, box in boxes.items():
    for idx, lens in enumerate(box):
        lens_label, focal_length = lens
        fp = 1
        fp *= 1+box_no
        fp *= idx+1
        fp *= focal_length
        total_fp += fp

print(total_fp)
