with open('inputs/Day2.txt', 'r') as f:
    entries = [line.strip() for line in f.readlines()]

valid_count = 0
for entry in entries:
    required, letter, password = entry.split(' ')
    min_count = int(required.split('-')[0])
    max_count = int(required.split('-')[1])
    letter = letter[0]
    amount = password.count(letter)
    if min_count <= amount <= max_count:
        valid_count += 1

print(valid_count)

# Part 2
valid_count = 0
for entry in entries:
    required, letter, password = entry.split(' ')
    first = int(required.split('-')[0])
    last = int(required.split('-')[1])
    letter = letter[0]
    count = 0
    if password[first-1] == letter:
        count += 1
    if password[last-1] == letter:
        count += 1
    if count == 1:
        valid_count += 1

print(valid_count)
