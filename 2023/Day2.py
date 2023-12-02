with open('inputs/Day2.txt', 'r') as f:
    games = [line.strip() for line in f.readlines()]

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def game_possible(game: str):
    showings = game.split('; ')
    for cubes in showings:
        rgb_list = cubes.split(', ')
        for amount_colour in rgb_list:
            amount, colour = amount_colour.split(' ')
            amount = int(amount)
            if colour == 'red' and amount > MAX_RED:
                return False
            if colour == 'green' and amount > MAX_GREEN:
                return False
            if colour == 'blue' and amount > MAX_BLUE:
                return False
    return True


total = 0
for game in games:
    game_id, game_string = game.split(': ')
    game_id = game_id.split(' ')[1]
    if game_possible(game_string):
        total += int(game_id)

print(total)

# Part 2


def min_cubes_needed(game: str):
    max_red_found = 0
    max_green_found = 0
    max_blue_found = 0
    showings = game.split('; ')
    for cubes in showings:
        rgb_list = cubes.split(', ')
        for amount_colour in rgb_list:
            amount, colour = amount_colour.split(' ')
            amount = int(amount)
            if colour == 'red':
                max_red_found = max(max_red_found, amount)
            if colour == 'green':
                max_green_found = max(max_green_found, amount)
            if colour == 'blue':
                max_blue_found = max(max_blue_found, amount)
    return max_red_found*max_green_found*max_blue_found


total = 0
for game in games:
    game_string = game.split(': ')[1]
    total += min_cubes_needed(game_string)

print(total)
