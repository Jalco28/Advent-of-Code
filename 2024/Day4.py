with open('inputs/Day4.txt', 'r') as f:
# with open('inputs/test.txt', 'r') as f:
    grid = [[char for char in line.strip()] for line in f.readlines()]

vectors = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]


def search(start_row, start_col, dir, word):
    for i, letter in enumerate(word):
        next_row = start_row+i*dir[0]
        next_col = start_col+i*dir[1]
        if next_row < 0 or next_row > len(grid)-1:
            return False
        if next_col < 0 or next_col > len(grid[0])-1:
            return False
        if grid[next_row][next_col] != letter:
            return False
    return True


words = 0
crosses = 0
A_coords = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        for idx, direction in enumerate(vectors):
            found = search(row, col, direction, 'XMAS')
            if found:
                words += 1

            if idx in (0, 2, 5, 7):
                found = search(row, col, direction, 'MAS')
                if found:
                    A_coords.append((row+direction[0], col+direction[1]))

# Find and count any double counted 'A's
A_count = {coord:A_coords.count(coord) for coord in A_coords}
for count in A_count.values():
    if count == 2:
        crosses += 1

print(words)
print(crosses)
