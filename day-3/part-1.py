from functools import reduce


def ord_to_score(char):
    if (char > 96):
        return char - 96
    else:
        return char - 38


def split_line(line):
    half_length = len(line)//2
    return line[:half_length], line[half_length:]


def find_duplicates(one, two):
    return (set(
            [item for item in one if item in two])).pop()


def calculate(score, line):
    one, two = split_line(line.strip())
    value = find_duplicates(one, two)
    return score + ord_to_score(ord(value))


with open("input.txt") as input_file:
    print(reduce(calculate, input_file, 0))
