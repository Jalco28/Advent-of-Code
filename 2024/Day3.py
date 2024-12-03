# with open('inputs/test.txt', 'r') as f:
with open('inputs/Day3.txt', 'r') as f:
    data = f.read()

counter = 0
for start_index in range(len(data)):
    if data[start_index:start_index+4] != 'mul(':
        continue

    current_index = start_index+4
    num1 = [current_index, None]  # Index range of nums
    num2 = [None, None]

    while data[current_index].isdecimal():
        current_index += 1
    num1[1] = current_index-1

    if data[current_index] != ',':
        continue
    current_index += 1

    num2[0] = current_index
    while data[current_index].isdecimal():
        current_index += 1
    if data[current_index] != ')':
        continue
    num2[1] = current_index-1

    counter += int(data[num1[0]:num1[1]+1]) * int(data[num2[0]:num2[1]+1])
print(counter)

# Part 2
enabled = True
counter = 0
for start_index in range(len(data)):
    if data[start_index:start_index+7] == 'don\'t()':
        enabled = False
        continue
    if data[start_index:start_index+4] == 'do()':
        enabled = True
        continue
    if data[start_index:start_index+4] != 'mul(' or not enabled:
        continue

    current_index = start_index+4
    num1 = [current_index, None]  # Index range of nums
    num2 = [None, None]

    while data[current_index].isdecimal():
        current_index += 1
    num1[1] = current_index-1

    if data[current_index] != ',':
        continue
    current_index += 1

    num2[0] = current_index
    while data[current_index].isdecimal():
        current_index += 1
    if data[current_index] != ')':
        continue
    num2[1] = current_index-1

    counter += int(data[num1[0]:num1[1]+1]) * int(data[num2[0]:num2[1]+1])
print(counter)
