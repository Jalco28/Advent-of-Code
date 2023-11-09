conversion = {"1": 1, "2": 2, "-": -1, "=": -2, "0": 0}

with open('Day25Input.txt', 'r') as f:
    nums = f.read().split('\n')
decimal_numbers = []
for num in nums:
    count = 0
    num = reversed(num)
    for idx, char in enumerate(num):
        count += conversion[char] * 5**(idx)
    decimal_numbers.append(count)

total = sum(decimal_numbers)

output = ''
while total:
    total, digit = total//5, total % 5
    if digit > 2:
        total += 1

        if digit == 3:
            output += "="
        elif digit == 4:
            output += '-'
    else:
        output += str(digit)
print(output[::-1])
print()
