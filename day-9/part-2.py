
rope = [[0, 0] for _ in range(10)]

positions = set()


def is_adjacent(prev_knot, next_knot):
    x_distance = prev_knot[0] - next_knot[0]
    y_distance = prev_knot[1] - next_knot[1]

    if x_distance > 1 or y_distance > 1 or x_distance < -1 or y_distance < -1:
        return False

    return True


def calculate_follow_position(prev_knot, next_knot):
    head_x, head_y = prev_knot
    tail_x, tail_y = next_knot
    x_distance = head_x - tail_x
    y_distance = head_y - tail_y

    if x_distance >= 1:
        tail_x += 1

    if x_distance <= -1:
        tail_x -= 1

    if y_distance >= 1:
        tail_y += 1

    if y_distance <= -1:
        tail_y -= 1

    return [tail_x, tail_y]


head = rope[0]

with open("./input.txt") as input_file:
    for line in input_file:
        clean_line = line.strip()
        move_direction, move_distance = clean_line.split()
        move_distance = int(move_distance)

        for _ in range(0, move_distance):
            match move_direction:
                case "U":
                    head[1] -= 1
                case "D":
                    head[1] += 1
                case "L":
                    head[0] -= 1
                case "R":
                    head[0] += 1

            for i, knot in enumerate(rope):

                if i == 0:
                    continue

                if not is_adjacent(rope[i-1], knot):
                    rope[i] = calculate_follow_position(rope[i-1], knot)

                tail = rope[len(rope)-1]
                positions.add(f"{tail[0]}:{tail[1]}")

print(len(positions))
