from itertools import islice
import ast

def is_correct(left, right):
    left_type = type(left)
    right_type = type(right)


    if left_type == list and right_type != list:
        right = [right]
        right_type = list

    if right_type == list and left_type != list:
        left = [left]
        left_type = list

    if left_type == list and right_type == list:
        count = 0
        while count < len(left) and count < len(right):
            result = is_correct(left[count], right[count])
            if result != "eq":
                return result
            count += 1

        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False
        
        return "eq"


    if left_type == int and right_type == int:
        if left == right:
            return "eq"
        return left < right

indicis = []
with open("./input.txt") as input_file:
    input = input_file.readlines()
    input = filter(lambda line: len(line) > 0, map(lambda line: line.strip(), input))
    temp_count = 1
    while True:
        pair = [line for line in islice(input, 2)]
        if not pair:
            break

        pair = list(map(lambda x: ast.literal_eval(x), pair))

        left, right = pair
        result = is_correct(left, right)

        print(f"Pair {temp_count} result {result}")
        if result:
            indicis.append(temp_count)

        temp_count += 1

print(sum(indicis))

