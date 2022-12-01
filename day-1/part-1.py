elf_calories = []
max_calories = 0

with open("input.txt") as input_file:
    for line in input_file:
        if line.strip().isnumeric():
            calories = int(line)
            elf_calories.append(calories)
        else:
            total_calories = sum(elf_calories)
            max_calories = (
                total_calories if total_calories > max_calories else max_calories
            )
            elf_calories = []

print(max_calories)
