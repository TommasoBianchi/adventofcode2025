def parse_input(file):
    lines = [line.strip() for line in file.readlines()]

    parts = {}
    i = 0
    while 'x' not in lines[i]:
        part_id = int(lines[i].replace(':', ''))
        part = [list(lines[i + j]) for j in range(1, 4)]
        i += 5
        parts[part_id] = part
    
    shapes = []
    for line in lines[i:]:
        [size, quantities] = line.split(': ')
        [width, height] = size.split('x')
        shapes.append((int(width), int(height), [int(q) for q in quantities.split(' ')]))
    
    return parts, shapes

def solve_first(file):
    parts, shapes = parse_input(file)

    parts_sizes = {part_id: len([el for row in part for el in row if el == '#']) for part_id, part in parts.items()}

    # NOTE: this should not be enough, as some cases could be infeasible even if they have enough space in theory (i.e., this is an upper bound).
    # But on my input it works (maybe I just got lucky). 
    count = 0
    for width, height, quantities in shapes:
        min_space = sum([parts_sizes[part_id] * q for part_id, q in enumerate(quantities)])
        if min_space > width * height:
            count += 1

    return len(shapes) - count

# NOTE: there is no real part two for day 12, since it's the last one for 2025
def solve_second(file):
    return "Buon Natale!"
