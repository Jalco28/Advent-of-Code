with open('inputs/Day1.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for line in data:
    value = ''
    for char in line:
        try:
            int(char)
        except ValueError:
            continue
        value += char
        break
    for char in reversed(line):
        try:
            int(char)
        except ValueError:
            continue
        value += char
        break
    total += int(value)

print(total)

# Part 2
nums = {1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'}


def find_written_number_indexes(x):
    # idx -> digit written
    result = {}
    for digit, written in nums.items():
        idx = x.find(written)
        if idx != -1:
            result[idx] = digit
    for digit, written in nums.items():
        idx = find_reversed(x, written)
        if idx != -1:
            result[idx] = digit
    return result


def find_reversed(string, value):
    string = string[::-1]
    idx = string.find(value[::-1])
    if idx == -1:
        return idx
    return len(string)-idx-1


total = 0
for line in data:
    indexes = find_written_number_indexes(line)
    for i in range(1, 10):
        idx = line.find(str(i))
        if idx != -1:
            indexes[idx] = i
    for i in range(1, 10):
        idx = find_reversed(line, str(i))
        if idx != -1:
            indexes[idx] = i
    first = min(indexes.items(), key=lambda x: x[0])[1]
    last = max(indexes.items(), key=lambda x: x[0])[1]
    value = str(first) + str(last)
    total += int(value)

print(total)
