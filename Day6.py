with open('Day6Input.txt', 'r') as f:
    line = f.readline()

def detect_uniques(string, length):
    if len(set(string)) == length:
        return True
    else:
        return False
for i in range(len(line)):
    string = line[i:i+4]
    if detect_uniques(string, 4):
        print(string)
        print(i+4)
        break

# Part 2
for i in range(len(line)):
    string = line[i:i+14]
    if detect_uniques(string, 14):
        print(string)
        print(i+14)
        break