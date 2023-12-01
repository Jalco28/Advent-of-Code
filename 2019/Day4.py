from itertools import pairwise


low = 124075
high = 580769


def check(num):
    found_same = False
    for a, b in pairwise(str(num)):
        a = int(a)
        b = int(b)
        if b < a:
            return False
        if b == a:
            found_same = True
    return found_same


valid = [x for x in range(low, high+1) if check(x)]
print(len(valid))
