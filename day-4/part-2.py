import re
from functools import reduce


def to_range(start, end):
    return set(range(int(start), int(end) + 1))


def calculate(count, line):
    elf_one_start, elf_one_end, elf_two_start, elf_two_end = re.split(
        ',|-', line.strip())
    elf_one_range = to_range(elf_one_start, elf_one_end)
    elf_two_range = to_range(elf_two_start, elf_two_end)

    duplicates = set.intersection(elf_one_range, elf_two_range)

    if len(duplicates) > 0:
        return count + 1
    else:
        return count


with open("input.txt") as input_file:
    print(reduce(calculate, input_file, 0))
