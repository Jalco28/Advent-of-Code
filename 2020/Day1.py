import sys
with open('Day1Input.txt', 'r') as f:
    nums = [int(num) for num in f]

for num in nums:
    if 2020 - num in nums:
        print(num*(2020-num))
        break

#Part 2
for first in nums:
    for second in nums:
        if 2020-(first+second) in nums:
            print(first*second*(2020-(first+second)))
            sys.exit()