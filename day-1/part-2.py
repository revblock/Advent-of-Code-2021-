elfCalories = []
totalCalories = []

with open("./input.txt") as input_file:
    for line in input_file:
        if line.strip().isnumeric():
            calories = int(line)
            elfCalories.append(calories)
        else:
            totalCalories.append(sum(elfCalories))
            elfCalories = []

if len(elfCalories) > 0:
    totalCalories.append(sum(elfCalories))

totalCalories.sort(reverse=True)
result = sum(totalCalories[0:3])
print(result)
