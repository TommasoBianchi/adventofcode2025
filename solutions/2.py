def parse_input(file):
    for line in file.readlines():
        line = line.strip()

    id_ranges = []
    for id_range in line.split(','):
        start = int(id_range.split('-')[0])
        end = int(id_range.split('-')[1])
        id_ranges.append((start, end))
    return id_ranges

def contains_duplication(n):
    digits = str(n)
    if len(digits) % 2 != 0:
        return False
    return digits[:len(digits) // 2] == digits[len(digits) // 2:]

def contains_repetition(n):
    digits = str(n)
    for l in range(1, 1 + len(digits) // 2):
        if digits[:l] * (len(digits) // l) == digits:
            return True
    return False

def solve_first(file):
    id_ranges = parse_input(file)

    result = 0
    for start, end in id_ranges:
        for id in range(start, end + 1):
            if contains_duplication(id):
                result += id

    return result

def solve_second(file):
    id_ranges = parse_input(file)

    result = 0
    for start, end in id_ranges:
        for id in range(start, end + 1):
            if contains_repetition(id):
                result += id

    return result
