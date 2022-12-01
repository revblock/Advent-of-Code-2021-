elfCalories = []
maxCalories = 0

with open("input.txt") as input_file:
    for line in input_file:
        if line.strip().isnumeric():
            calories = int(line)
            elfCalories.append(calories)
        else:
            totalCalories = sum(elfCalories)
            maxCalories = totalCalories if totalCalories > maxCalories else maxCalories
            elfCalories = []

print(maxCalories)
