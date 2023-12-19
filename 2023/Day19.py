from copy import deepcopy
import operator as op

char_to_op = {
    '>': op.gt,
    '<': op.lt
}


with open('inputs/Day19.txt', 'r') as f:
    raw_rules, raw_parts = map(str.split, f.read().split('\n\n'))
workflows = {}
for rule in raw_rules:
    name, raw_conditions = rule.split('{')
    # [(part_attribute, operator, number, action), (action)]
    rules = []
    for condition in raw_conditions.split(','):
        if condition[-1] == '}':  # end condition
            rules.append((condition[:-1],))
            continue
        pa = condition[0]
        comparison_op = char_to_op[condition[1]]
        condition = condition[2:].split(':')
        num = int(condition[0])
        action = condition[1]
        rules.append((pa, comparison_op, num, action))
    workflows[name] = rules

parts = []
for raw_part in raw_parts:
    part = {}
    raw_part = raw_part[1:-1]
    for attribute in raw_part.split(','):
        name, num = attribute.split('=')
        part[name] = int(num)
    parts.append(part)


def is_accepted(workflow_name, part: dict[str, int]):
    workflow = workflows[workflow_name]
    for rule in workflow:
        if len(rule) == 1:  # End rule
            if rule[0] == 'A':
                return True
            elif rule[0] == 'R':
                return False
            else:
                return is_accepted(rule[0], part)

        attribute, func, num, action = rule
        if func(part[attribute], num):
            if action == 'A':
                return True
            elif action == 'R':
                return False
            else:
                return is_accepted(action, part)


parts = [part for part in parts if is_accepted('in', part)]

total = 0
for part in parts:
    for attribute in part.values():
        total += attribute

print(total)

# Part 2
def possibilities(chunk:dict):
    chunk.pop('wf')
    result = 1
    for start, end in chunk.values():
        result *= end-start+1
    return result

def calc_new_range(func, limit, start, end):
    if func == op.lt and start<limit:
        return [start, limit-1]
    if func == op.gt and end > limit:
        return [limit+1, end]
    return None


queue = [{letter: [1, 4000] for letter in 'xmas'} | {'wf': 'in'}]
"""
Iterate through each rule in workflow
Chop and send chunks to queue with new workflow name as you go
You only need to change one attributes range per rule
"""
total = 0

while queue:
    chunk = queue.pop()
    for rule in workflows[chunk['wf']]:
        if len(rule) != 1:
            attribute, func, limit, action = rule
            new_range = calc_new_range(func, limit, chunk[attribute][0], chunk[attribute][1])
            if new_range:
                #Bit that doesn't fit rule
                if func == op.lt:
                    chunk[attribute][0] = limit
                else:
                    chunk[attribute][1] = limit

                #Bit that does
                new_chunk = deepcopy(chunk)|{attribute:new_range, 'wf':action}
                if action == 'A':
                    total += possibilities(new_chunk)
                elif action != 'R':
                    queue.append(new_chunk)

        else:
            #end mapping
            action = rule[0]
            if action == 'A':
                total += possibilities(chunk)
            elif action != 'R':
                queue.append(deepcopy(chunk)|{'wf':action})

print(total)
print()
