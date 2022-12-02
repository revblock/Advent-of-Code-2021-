from functools import reduce

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 0,
    "Y": 3,
    "Z": 6
}

beat_map = {
    "A": "C",
    "B": "A",
    "C": "B"
}

loss_map = {v: k for k, v in beat_map.items()}


def line_score(score, line):
    opponent, expected = line.strip().split()
    match expected:
        case "X":
            player = beat_map[opponent]
        case "Y":
            player = opponent
        case "Z":
            player = loss_map[opponent]
    return score + scores[player] + scores[expected]


with open("input.txt") as input_file:
    print(reduce(line_score, input_file, 0))
