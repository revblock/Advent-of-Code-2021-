grid = []

with open("./input.txt") as input_file:
    for line in input_file:
        clean_line = line.strip()
        row = []
        grid.append(row)
        for tree in clean_line:
            row.append(int(tree))

scores = []

for y, row in enumerate(grid):
    for x, tree_height in enumerate(row):

        distance_up = 0
        distance_right = 0
        distance_down = 0
        distance_left = 0

        # UP
        if y != 0:
            for i in reversed(range(0, y)):
                distance_up += 1
                if grid[i][x] >= tree_height:
                    break

        # Right
        if x != len(row)-1:
            for i in range(x+1, len(row)):
                distance_right += 1
                if grid[y][i] >= tree_height:
                    break

        # Down
        if y != len(grid) - 1:
            for i in range(y+1, len(grid)):
                distance_down += 1
                if grid[i][x] >= tree_height:
                    break

        # Left
        if x != 0:
            for i in reversed(range(0, x)):
                distance_left += 1
                if grid[y][i] >= tree_height:
                    break

        scores.append(distance_right * distance_down *
                      distance_left * distance_up)

print(max(scores))
