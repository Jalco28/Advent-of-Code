with open('Day2Input.txt','r') as f:
    rounds = f.readlines()

rounds = [round.strip('\n') for round in rounds]

total_score = 0

for round in rounds:
    theirs = round[0]
    yours = round[2]
    match yours:
        case "X":
            yours_translated = "A"
        case "Y":
            yours_translated = "B"
        case "Z":
            yours_translated = "C"
    if theirs == yours_translated:
        result_points = 3   #Draw
    else:
        match round:
            case "A Y":
                result_points = 6
            case "A Z":
                result_points = 0
            case "B X":
                result_points = 0
            case "B Z":
                result_points = 6
            case "C X":
                result_points = 6
            case "C Y":
                result_points = 0
    piece_points = {'X': 1, 'Y': 2, 'Z': 3}
    total_score += piece_points[yours] + result_points
print(total_score)

#Part two
total_score = 0
for round in rounds:
    theirs = round[0]
    result = round[2]
    piece_points = {'A': 1, 'B': 2, 'C': 3}
    result_points = {'X': 0, 'Y': 3, 'Z': 6}

    if result == 'X':
        match theirs:
            case "A":
                yours = 'C'
            case "B":
                yours = "A"
            case "C":
                yours = "B"
    if result == 'Y':
        yours = theirs
    if result == 'Z':
        match theirs:
            case "A":
                yours = 'B'
            case "B":
                yours = "C"
            case "C":
                yours = "A"
    total_score += result_points[result]+piece_points[yours]
print(total_score)
