command_queue = [1]

with open("./input.txt") as input_file:
    for line in input_file:
        command = line.strip().split()
        cursor_position = 1 if len(
            command_queue) == 0 else command_queue[len(command_queue)-1]
        if command[0] == "noop":
            command_queue.append(cursor_position)
        else:
            command_parameter = int(command[1])
            command_queue.append(cursor_position)
            command_queue.append(cursor_position + command_parameter)

line_width = 40
crt = ""
for line_cycle in range(0, 6):
    line = ""
    for cycle in range(0, line_width):
        cursor_position = command_queue[line_cycle * line_width + cycle]
        cursor_distance = cursor_position - cycle
        if cursor_distance >= -1 and cursor_distance <= 1:
            line = line + "#"
        else:
            line = line + "."
    crt = crt + line

n = 40
for line in [crt[i:i+n] for i in range(0, len(crt), n)]:
    print(line)
