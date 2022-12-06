with open('Day6Input.txt', 'r') as f:
    line = f.readline()

def detect_uniques(string):
    if len(set(string)) == 4:
        return True
    else:
        return False
for i in range(len(line)):
    string = line[i:i+4]
    if detect_uniques(string):
        print(string)
        print(i+4)
        break
# Part 2
def detect_uniques(string):
    if len(set(string)) == 14:
        return True
    else:
        return False

for i in range(len(line)):
    string = line[i:i+14]
    if detect_uniques(string):
        print(string)
        print(i+14)
        break