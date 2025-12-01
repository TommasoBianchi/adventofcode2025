def parse_input(file):
    return [line.strip() for line in file.readlines()]

def solve_first(file):
    count = 0
    position = 50
    for line in parse_input(file):
        sign = 1 if line[0] == 'R' else -1
        position = (position + sign * int(line[1:])) % 100
        if position == 0:
            count += 1

    return count

def solve_second(file):
    count = 0
    position = 50
    for line in parse_input(file):
        sign = 1 if line[0] == 'R' else -1
        delta = sign * int(line[1:])
        original_position = position
        position = position + delta
        while position < 0 or position >= 100:
            count += 1
            position += (-1 if position > 0 else 1) * 100
        if original_position == 0 and sign < 0:
            count -= 1
        if position == 0 and sign < 0:
            count += 1

    return count
