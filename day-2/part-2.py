class Play:
    def __init__(self, opponent, player, score):
        self.opponent = opponent
        self.player = player
        self.score = score


class Result:
    def __init__(self, value, score):
        self.value = value
        self.score = score


rock = Play("A", "X", 1)
paper = Play("B", "Y", 2)
scissors = Play("C", "Z", 3)

rock.beats = scissors
paper.beats = rock
scissors.beats = paper

plays = [rock, paper, scissors]

loss = Result("X", 0)
draw = Result("Y", 3)
win = Result("Z", 6)

results = [loss, draw, win]

score = 0

with open("input.txt") as input_file:
    for line in input_file:
        opponent, expected = line.strip().split()
        opponent_play = next(filter(lambda x: x.opponent == opponent, plays))
        expected_result = next(filter(lambda x: x.value == expected, results))
        player_play: Play
        match expected:
            case "X":
                player_play = opponent_play.beats
            case "Y":
                player_play = opponent_play
            case "Z":
                player_play = next(
                    filter(lambda x: x.beats == opponent_play, plays))

        score += player_play.score
        if player_play.beats == opponent_play:
            score += win.score
        elif player_play == opponent_play:
            score += draw.score
        else:
            score += loss.score

print(score)
