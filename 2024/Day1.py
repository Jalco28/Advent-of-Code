with open('inputs/Day1.txt', 'r') as f:
    data = [list(map(int, line.split('   '))) for line in f.readlines()]

list1 = [data[i][0] for i in range(len(data))]
list2 = [data[i][1] for i in range(len(data))]

compare = zip(sorted(list1), sorted(list2))
total = 0
for a, b in compare:
    total += abs(a-b)
print(total)

# Part 2
similarity = 0
for item in list1:
    similarity += item*list2.count(item)
print(similarity)
