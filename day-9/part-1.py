head = [0, 0]
tail = [0, 0]

positions = set()


def is_adjacent(head, tail):
    x_distance = head[0] - tail[0]
    y_distance = head[1] - tail[1]

    if x_distance > 1 or y_distance > 1 or x_distance < -1 or y_distance < -1:
        return False

    return True


def calculate_follow_position(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
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

            if not is_adjacent(head, tail):
                tail = calculate_follow_position(head, tail)

            positions.add(f"{tail[0]}:{tail[1]}")

print(len(positions))
