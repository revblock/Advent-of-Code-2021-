rows = []
columns = []

with open("./input.txt") as input_file:
    for y, line in enumerate(input_file):
        clean_line = line.strip()

        row = []
        for y, t in enumerate(clean_line):
            row.append(int(t))

            if len(columns) - 1 < y:
                columns.append([])

            columns[y].append(int(t))

        rows.append(row)


def xy_to_coords(x, y, flip_xy):
    if not flip_xy:
        return f"{x}:{y}"
    else:
        return f"{y}:{x}"


def find_visible(items, flip_xy=False):

    visible = {}

    for y, row in enumerate(items):
        tallest = []
        tallest_xy = []

        for x, tree in enumerate(row):
            if y == 0 or y == len(rows) - 1 or x == 0 or x == len(row)-1:
                visible[xy_to_coords(x, y, flip_xy)] = tree

            if len(tallest) == 0 or tree > max(tallest):
                tallest.append(tree)
                tallest_xy.append(xy_to_coords(x, y, flip_xy))

        for i, t in enumerate(tallest_xy):
            visible[t] = tallest[i]

        tallest = []
        tallest_xy = []

        for x, tree in reversed(list(enumerate(row))):
            if y == 0 or y == len(rows) - 1 or x == 0 or x == len(row)-1:
                visible[xy_to_coords(x, y, flip_xy)] = tree

            if len(tallest) == 0 or tree > max(tallest):
                tallest.append(tree)
                tallest_xy.append(xy_to_coords(x, y, flip_xy))

        for i, t in enumerate(tallest_xy):
            visible[t] = tallest[i]

    return visible


visible_rows = find_visible(rows)
visible_columns = find_visible(columns, True)
visible_grid = visible_rows | visible_columns

print(visible_grid)
print(len(visible_grid))
