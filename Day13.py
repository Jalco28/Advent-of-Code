with open("Day13Input.txt", 'r') as f:
    lines = f.readlines()
lines = [line.strip('\n') for line in lines]
data = []
for line in lines:
    if line == '':
        continue
    else:
        data.append(eval(line))
correct_pair_indexs = []

def compare_lists(left:list, right:list):
    try:
        x = zip(left, right, strict=True)
        for a, b in x:
            if isinstance(a, int) and isinstance(b, int):
                if a < b:
                    return True
                elif a == b:
                    continue
                else:
                    return False
            elif isinstance(a,list) and isinstance(b,int):
                result = compare_lists(a,[b])
                if result is None:
                    continue
                else:
                    return result
            elif isinstance(a,int) and isinstance(b,list):
                result = compare_lists([a],b)
                if result is None:
                    continue
                else:
                    return result
            elif isinstance(a, list) and isinstance(b, list):
                result = compare_lists(a,b)
                if result is None:
                    continue
                else:
                    return result
    except ValueError:
        if len(left) < len(right):
            return True
        else:
            return False

for i in range(0,len(data), 2):
    if compare_lists(data[i], data[i+1]):
        correct_pair_indexs.append(i/2+1)
print(sum(correct_pair_indexs))

#Part 2
data.append([[2]])
data.append([[6]])
changes_made = True
while changes_made:
    changes_made = False
    for i in range(0,len(data)):
        try:
            if not compare_lists(data[i], data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                changes_made = True
        except IndexError:
            pass
print((data.index([[2]])+1) * (data.index([[6]])+1))