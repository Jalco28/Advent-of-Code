import itertools


with open('inputs/Day2.txt', 'r') as f:
    data = [list(map(int, line.split())) for line in f.readlines()]


def analyse_report(report):
    deltas = [a-b for a, b in itertools.pairwise(report)]
    delta_sign = [x >= 0 for x in deltas]
    if len(set(delta_sign)) > 1:
        return False
    for d in deltas:
        if 1 <= abs(d) <= 3:
            pass
        else:
            return False
    return True


safe_number = 0
for report in data:
    if analyse_report(report):
        safe_number += 1

print(safe_number)

# Part 2
safe_number = 0
for report in data:
    # index -1 means no missing level
    for missing_index in range(-1, len(report)):
        if missing_index == -1:
            safe = analyse_report(report)
            if safe:
                break
        else:
            new_report = report[:missing_index] + report[missing_index+1:]
            safe = analyse_report(new_report)
            if safe:
                break

    if safe:
        safe_number += 1
print(safe_number)
