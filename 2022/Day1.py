with open('Day1Input.txt', 'r') as file:
    input = file.readlines()

for index, item in enumerate(input[:]):
    try:
        input[index] = int(item)
    except ValueError:
        pass
number_of_elves = 0
for item in input:
    if item == '\n':
        number_of_elves += 1
number_of_elves += 1

calories = [0 for i in range(number_of_elves)]

current_elf = 0
for item in input:
    if item == '\n':
        current_elf += 1
        continue
    calories[current_elf] += item

biggest_value = max(calories)
biggest_elf = calories.index(biggest_value)+1
print(f'The elf with the most calories in elf number {biggest_elf}, they are carrying {biggest_value} calories')
#Part 2
calories.sort(reverse=True)

top_3_values = calories[0:3]
top_3_sum = sum(top_3_values)
print(top_3_sum)