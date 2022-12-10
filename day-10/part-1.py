x = 1
command_queue = []

with open("./input.txt") as input_file:
    for line in input_file:
        command = line.strip().split()
        if command[0] == "noop":
            command_queue.append([1, 0])
        else:
            command_parameter = int(command[1])
            command_queue.append([2, command_parameter])

cycles_to_check = [20, 60, 100, 140, 180, 220]
current_cycle = 0
x_cycle_values = []
for command in command_queue:
    wait, value = command
    for _ in range(0, wait):
        current_cycle += 1
        if current_cycle in cycles_to_check:
            x_cycle_values.append(x * current_cycle)
    x += value

print(sum(x_cycle_values))
