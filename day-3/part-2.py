from itertools import islice


def ord_to_score(char):
    if (char > 96):
        return char - 96
    else:
        return char - 38


score = 0

with open("input.txt") as input_file:
    while True:
        group = [elf.rstrip('\n') for elf in islice(input_file, 3)]
        if not group:
            break
        duplicate = (set.intersection(*map(set, group))).pop()
        score += ord_to_score(ord(duplicate))

print(score)
