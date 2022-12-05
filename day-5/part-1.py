import re

stacks = []
instructions = []


with open("input.txt") as input_file:
    for line in input_file:
        stripped_line = line.strip("\n")

        if not stripped_line or stripped_line.startswith(" 1"):
            continue

        if stripped_line.startswith("move"):
            instructions.append([int(s) for s in re.findall(
                r'\b\d+\b', stripped_line)])
            continue

        columns = [stripped_line[idx]
                   for idx in range(1, len(stripped_line), 4)]
        columns.reverse()

        if len(stacks) == 0:
            stacks = [[] for x in range(len(columns))]

        for idx, col in enumerate(columns):
            if col != " ":
                stacks[idx].append(col)

stacks.reverse()
print(stacks)

for instruction in instructions:
    count, move_from, move_to = instruction

    for _ in range(count):
        item = stacks[move_from - 1].pop(0)
        stacks[move_to - 1].insert(0, item)

result = ""
for stack in stacks:
    top = stack.pop(0)
    result += top

print(result)
