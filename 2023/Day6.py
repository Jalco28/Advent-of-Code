from functools import reduce
from operator import add
with open('inputs/Day6.txt', 'r') as f:
    times, distances = (line.split(':')[1].strip().split() for line in f.readlines())

times = [int(time) for time in times]
distances = [int(distance) for distance in distances]

def try_all_times(race_length, record):
    winning_distances = 0
    for button_press_time in range(race_length+1):
        speed = button_press_time
        travel_time = race_length-button_press_time
        distance = speed*travel_time
        if distance > record:
            winning_distances +=1

    return winning_distances
total = None
for time, distance in zip(times, distances):
    result = try_all_times(time, distance)
    if total is None:
        total = result
    else:
        total *= result
print(total)


#Part 2
big_time = int(reduce(add, [str(time) for time in times]))
big_distance = int(reduce(add, [str(distance) for distance in distances]))
total = try_all_times(big_time, big_distance)
print(total)