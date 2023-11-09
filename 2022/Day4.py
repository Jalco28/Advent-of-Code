with open('Day4Input.txt', 'r') as f:
    pairs = f.readlines()

pairs = [pair.strip('\n') for pair in pairs]
total = 0
for pair in pairs:
    pair = pair.split(',')
    pair = [item.split("-") for item in pair]
    pair = pair[0]+pair[1]
    pair = [int(item) for item in pair]
    if pair[0] <= pair[2] and pair[1] >= pair[3]:
        total += 1
    elif pair[2] <= pair[0] and pair[3] >= pair[1]:
        total += 1
# print(total)

#Part 2
total = 0
for pair in pairs:
    pair = pair.split(',')
    pair = [item.split("-") for item in pair]
    pair = pair[0]+pair[1]
    pair = [int(item) for item in pair]
    elf_one = set(range(pair[0], pair[1]+1))
    elf_two = set(range(pair[2], pair[3]+1))
    if elf_one.intersection(elf_two) != set():
        total += 1
print(total)