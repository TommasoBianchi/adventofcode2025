def parse_input(file):
    grid = []
    for line in file.readlines():
        line = line.strip()
        grid.append(list(line))
    return grid

def solve_first(file):
    grid = parse_input(file)

    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != '@':
                continue
            count = 0
            for delta_row in [-1, 0, 1]:
                for delta_col in [-1, 0, 1]:
                    if delta_row == 0 and delta_col == 0:
                        continue
                    if row + delta_row >= 0 and row + delta_row < len(grid) and col + delta_col >= 0 and col + delta_col < len(grid[row]) and grid[row + delta_row][col + delta_col] == '@':
                        count += 1
            if count < 4:
                result += 1

    return result

def solve_second(file):
    grid = parse_input(file)

    result = 0
    has_changed = True
    while has_changed:
        has_changed = False
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != '@':
                    continue
                count = 0
                for delta_row in [-1, 0, 1]:
                    for delta_col in [-1, 0, 1]:
                        if delta_row == 0 and delta_col == 0:
                            continue
                        if row + delta_row >= 0 and row + delta_row < len(grid) and col + delta_col >= 0 and col + delta_col < len(grid[row]) and grid[row + delta_row][col + delta_col] == '@':
                            count += 1
                if count < 4:
                    grid[row][col] = 'x'
                    has_changed = True
                    result += 1

    return result
