grid = []

with open("./input.txt") as input_file:
    for line in input_file:
        clean_line = line.strip()
        row = []
        for char in clean_line:
            row.append(char)
        grid.append(row)

print(grid)