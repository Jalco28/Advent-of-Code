from copy import copy
with open('inputs/Day2.txt', 'r') as f:
    program = [int(num) for num in f.readline().split(',')]

program[1] = 12
program[2] = 2


def get_at_address(location):
    return program[location]


program_counter = 0
while True:
    if program[program_counter] == 99:
        break
    elif program[program_counter] == 1:
        result = get_at_address(
            program[program_counter+1]) + get_at_address(program[program_counter+2])
    elif program[program_counter] == 2:
        result = get_at_address(
            program[program_counter+1]) * get_at_address(program[program_counter+2])
    program[program[program_counter+3]] = result
    program_counter += 4

print(program[0])

# Part 2

with open('inputs/Day2.txt', 'r') as f:
    original_program = [int(num) for num in f.readline().split(',')]


def get_result(noun, verb):
    program = copy(original_program)
    program[1] = noun
    program[2] = verb
    program_counter = 0
    while True:
        if program[program_counter] == 99:
            break
        elif program[program_counter] == 1:
            result = program[
                program[program_counter+1]] + program[program[program_counter+2]]
        elif program[program_counter] == 2:
            result = program[
                program[program_counter+1]] * program[program[program_counter+2]]
        program[program[program_counter+3]] = result
        program_counter += 4

    return program[0]


limit = 110
solved = False
for noun in range(limit):
    for verb in range(limit):
        if get_result(noun, verb) == 19690720:
            print(f'{noun=}, {verb=}')
            print(100*noun+verb)
            solved = True
        if solved:
            break
    if solved:
        break