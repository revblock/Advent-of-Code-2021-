class Play:
    def __init__(self, opponent, player, score):
        self.opponent = opponent
        self.player = player
        self.score = score


rock = Play("A", "X", 1)
paper = Play("B", "Y", 2)
scissors = Play("C", "Z", 3)

rock.beats = scissors
paper.beats = rock
scissors.beats = paper

plays = [rock, paper, scissors]

loss = 0
draw = 3
win = 6

results = [loss, draw, win]

score = 0

with open("input.txt") as input_file:
    for line in input_file:
        opponent, player = line.strip().split()
        opponentPlay = next(filter(lambda x: x.opponent == opponent, plays))
        playerPlay = next(filter(lambda x: x.player == player, plays))
        score += playerPlay.score
        if playerPlay.beats == opponentPlay:
            score += win
        elif playerPlay == opponentPlay:
            score += draw
        else:
            score += loss

print(score)
