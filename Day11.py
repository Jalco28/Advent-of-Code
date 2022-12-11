class Monkey:
    def __init__(self, id, items:list[int], operation:list[str, int], test:int, throw_to:list[int]) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_to = throw_to
        self.id = id
        self.items_inspected = 0
    def inspect_all_items(self):
        for item in self.items:
            self.items_inspected += 1
            eval_string = f'{item} {self.operation}'
            item = eval(eval_string)%m#//3
            if item % self.test == 0:
                monkeys[self.throw_to[0]].items.append(item)
            else:
                monkeys[self.throw_to[1]].items.append(item)
        self.items = []

with open('Day11Input.txt') as f:
    data = f.readlines()
data = [line.strip("\n") for line in data]
monkeys = []
m=1
for line in data:
    if line == "":
        monkeys.append(Monkey(id, items, operation, test, [true, false]))
    elif line[0] == "M":
        id = line[7]
    elif line[2] == "S":
        items = line[18:].split(', ')
        items = [int(item) for item in items]
    elif line[2] == "O":
        operation = line[23:]
    elif line[2] == "T":
        test = int(line[21:])
    elif line[7] == "t":
        true = int(line[-1])
    elif line[7] == "f":
        false = int(line[-1])
for monkey in monkeys:
    m *= monkey.test
for i in range(10000):
    for monkey in monkeys:
        monkey.inspect_all_items()
scores = [monkey.items_inspected for monkey in monkeys]
print(scores)
print(sorted(scores, reverse=True)[0]*sorted(scores, reverse=True)[1])