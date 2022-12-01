elf_calories = []
total_calories = []

with open("./input.txt") as input_file:
    for line in input_file:
        if line.strip().isnumeric():
            calories = int(line)
            elf_calories.append(calories)
        else:
            total_calories.append(sum(elf_calories))
            elf_calories = []

if len(elf_calories) > 0:
    total_calories.append(sum(elf_calories))

total_calories.sort(reverse=True)
result = sum(total_calories[0:3])
print(result)
