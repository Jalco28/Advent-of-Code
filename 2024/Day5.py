from collections import defaultdict


with open('inputs/Day5.txt', 'r') as f:
    rules, updates = f.read().split('\n\n')

rules = [[int(num) for num in rule.split('|')] for rule in rules.split()]
updates = [[int(num) for num in update.split(',')]
           for update in updates.split()]
incorrect = []
counter = 0
for idx, pages in enumerate(updates):
    correct = True
    for first, last in rules:
        try:
            if pages.index(first) > pages.index(last):
                correct = False
                incorrect.append(idx)
                break
        except ValueError:
            pass
    if correct:
        counter += pages[int(len(pages)*0.5-0.5)]

print(counter)

# Part 2
# num: {numbers that must be before}
rules_dict = defaultdict(set)

for a, b in rules:
    rules_dict[b].add(a)

counter = 0
for idx in incorrect:
    pages = updates[idx]
    new_order = []
    for num in pages:
        min_index = -1
        for before in rules_dict[num]:
            try:
                min_index = max(min_index, new_order.index(before))
            except ValueError:
                pass
        new_order.insert(min_index+1, num)
    counter += new_order[int(len(new_order)*0.5-0.5)]
print(counter)
