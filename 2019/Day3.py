with open('inputs/Day3.txt', 'r') as f:
    instructions_1 = f.readline().strip().split(',')
    instructions_2 = f.readline().strip().split(',')


def get_visits(instructions):
    pos = [0, 0]
    result = set()
    for instruction in instructions:
        delta = int(instruction[1:])
        if instruction[0] == 'U':
            for i in range(1, delta+1):
                pos[1] += 1
                result.add(tuple(pos))
        elif instruction[0] == 'D':
            for i in range(1, delta+1):
                pos[1] -= 1
                result.add(tuple(pos))
        elif instruction[0] == 'L':
            for i in range(1, delta+1):
                pos[0] -= 1
                result.add(tuple(pos))
        elif instruction[0] == 'R':
            for i in range(1, delta+1):
                pos[0] += 1
                result.add(tuple(pos))
    return result


rope_1 = get_visits(instructions_1)
rope_2 = get_visits(instructions_2)

intersections = rope_1.intersection(rope_2)

print(min([abs(point[0])+abs(point[1]) for point in intersections]))

# Part 2
def get_visits(instructions):
    pos = [0, 0]
    result = set()
    steps = {}
    current_steps = 1
    for instruction in instructions:
        delta = int(instruction[1:])
        if instruction[0] == 'U':
            for i in range(1, delta+1):
                pos[1] += 1
                temp = tuple(pos)
                result.add(temp)
                if temp not in steps:
                    steps[temp] = current_steps
                current_steps += 1

        elif instruction[0] == 'D':
            for i in range(1, delta+1):
                pos[1] -= 1
                temp = tuple(pos)
                result.add(temp)
                if temp not in steps:
                    steps[temp] = current_steps
                current_steps += 1

        elif instruction[0] == 'L':
            for i in range(1, delta+1):
                pos[0] -= 1
                temp = tuple(pos)
                result.add(temp)
                if temp not in steps:
                    steps[temp] = current_steps
                current_steps += 1

        elif instruction[0] == 'R':
            for i in range(1, delta+1):
                pos[0] += 1
                temp = tuple(pos)
                result.add(temp)
                if temp not in steps:
                    steps[temp] = current_steps
                current_steps += 1

    return result, steps
rope_1, rope_1_steps = get_visits(instructions_1)
rope_2, rope_2_steps = get_visits(instructions_2)

intersections = rope_1.intersection(rope_2)

poi = min(intersections, key=lambda pos: rope_1_steps[pos]+rope_2_steps[pos])
print(rope_1_steps[poi]+rope_2_steps[poi])
print()
