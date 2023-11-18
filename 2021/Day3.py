from copy import copy


with open('inputs/Day3.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

gamma = ''
epsilon = ''

for i in range(12):
    digits = []
    for number in data:
        digits.append(number[i])
    num0 = digits.count('0')
    num1 = len(data) - num0
    if num0 > num1:
        gamma += '0'
        epsilon += '1'
    elif num0 < num1:
        gamma += '1'
        epsilon += '0'
    else:
        raise Exception('Equal number of bits')

print(int(gamma, 2)*int(epsilon, 2))

# Part 2
working_data = copy(data)
for i in range(12):
    digits = []
    for number in working_data:
        digits.append(number[i])
    num0 = digits.count('0')
    num1 = len(working_data) - num0
    if num0 == num1:
        mcb = "1"
    else:
        mcb = "1" if num1 > num0 else "0"
    working_data = [number for number in working_data if number[i] == mcb]
    if len(working_data) == 1:
        break
o2rating = int(working_data[0], 2)

working_data = copy(data)
for i in range(12):
    digits = []
    for number in working_data:
        digits.append(number[i])
    num0 = digits.count('0')
    num1 = len(working_data) - num0
    if num0 == num1:
        lcb = "0"
    else:
        lcb = "1" if num1 < num0 else "0"
    working_data = [number for number in working_data if number[i] == lcb]
    if len(working_data) == 1:
        break
co2rating = int(working_data[0], 2)

print(o2rating*co2rating)
