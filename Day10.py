with open('Day10Input.txt', 'r') as f:
    commands = f.readlines()

commands = (command.strip('\n') for command in commands)
x = 1
queue = []
cycle_number = 1
logs = []
screen = [['+' for j in range(40)] for i in range(6)]


def get_pixel_coordinates(number):
    x, y = 0, 0
    while number > 40:
        x += 1
        number -= 40
    y = number-1
    return (x, y)


def get_sprite_coordinates(number):
    values = []
    if number-1 >= 0:
        values.append(number-1)
    values.append(number)
    if number+1 <= 39:
        values.append(number+1)
    return tuple(values)


while True:
    try:
        if len(queue) == 0:
            command = next(commands).split(" ")
            queue.append([command, 1 if command[0] == 'noop' else 2])
        if cycle_number in [20, 60, 100, 140, 180, 220]:
            logs.append(x*cycle_number)
        for idx, instruction in enumerate(queue[:]):
            queue[idx] = [instruction[0], instruction[1]-1]
        #
        if get_pixel_coordinates(cycle_number)[1] in get_sprite_coordinates(x):
            screen[get_pixel_coordinates(cycle_number)[
                0]][get_pixel_coordinates(cycle_number)[1]] = '#'
        else:
            screen[get_pixel_coordinates(cycle_number)[
                0]][get_pixel_coordinates(cycle_number)[1]] = '.'
        #
        for idx, instruction in enumerate(queue):
            if instruction[1] <= 0:
                if instruction[0][0] == "addx":
                    x += int(instruction[0][1])
                queue.pop(idx)
                break
        cycle_number += 1
    except StopIteration:
        break
print(sum(logs))
for line in screen:
    for pixel in line:
        print(pixel, end='')
    print()
