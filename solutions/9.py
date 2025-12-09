def parse_input(file):
    red_tiles = []
    for line in file.readlines():
        line = line.strip()
        x, y = line.split(',')
        red_tiles.append((int(x), int(y)))
    return red_tiles

def solve_first(file):
    red_tiles = parse_input(file)

    max_size = 0
    for x1, y1 in red_tiles:
        for x2, y2 in red_tiles:
            size = abs(x2 - x1 + 1) * abs(y2 - y1 + 1)
            if size > max_size:
                max_size = size

    return max_size

def solve_second(file):
    red_tiles = parse_input(file)

    width = max([x for x, _ in red_tiles])
    height = max([y for _, y in red_tiles])

    red_or_green_by_row = [set() for _ in range(height + 1)]
    red_or_green_by_col = [set() for _ in range(width + 1)]
    reds_by_row = [set() for _ in range(height + 1)]
    reds_by_col = [set() for _ in range(width + 1)]

    for x, y in red_tiles:
        reds_by_row[y].add(x)
        reds_by_col[x].add(y)

    red_or_green_tiles = set()
    for (x1, y1), (x2, y2) in zip(red_tiles, red_tiles[1:] + [red_tiles[0]]):
        assert x1 == x2 or y1 == y2
        red_or_green_tiles.add((x1, y1))
        red_or_green_by_row[y1].add(x1)
        red_or_green_by_col[x1].add(y1)
        red_or_green_tiles.add((x2, y2))
        red_or_green_by_row[y2].add(x2)
        red_or_green_by_col[x2].add(y2)
        for lx in range(min(x1, x2), max(x1, x2)):
            red_or_green_tiles.add((lx, y1))
            red_or_green_by_row[y1].add(lx)
            red_or_green_by_col[lx].add(y1)
        for ly in range(min(y1, y2), max(y1, y2)):
            red_or_green_tiles.add((x1, ly))
            red_or_green_by_row[ly].add(x1)
            red_or_green_by_col[x1].add(ly)


    # NOTE: this is not needed for the final solution, but since it took a lot of effort I do not want to remove it
    def is_internal(x, y):
        if (x, y) in red_or_green_tiles:
            return True

        up_intersections = len([ry for ry in red_or_green_by_col[x] if ry < y])
        down_intersections = len([ry for ry in red_or_green_by_col[x] if ry > y])
        left_intersections = len([rx for rx in red_or_green_by_row[y] if rx < x])
        right_intersections = len([rx for rx in red_or_green_by_row[y] if rx > x])

        up_reds = len([ry for ry in reds_by_col[x] if ry < y])
        down_reds = len([ry for ry in reds_by_col[x] if ry > y])
        left_reds = len([rx for rx in reds_by_row[y] if rx < x])
        right_reds = len([rx for rx in reds_by_row[y] if rx > x])

        for reds, intersections in [(up_reds, up_intersections), (down_reds, down_intersections), (left_reds, left_intersections), (right_reds, right_intersections)]:
            if reds == 0:
                return intersections % 2 == 1

        raise ValueError("IMPOSSIBLE")

    def has_sides_fast(x1, y1, x2, y2):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for (rx1, ry1), (rx2, ry2) in zip(red_tiles, red_tiles[1:] + [red_tiles[0]]):
            if rx1 == rx2 and x1 < rx1 and x2 > rx1 and not (max(ry1, ry2) < y1 or min(ry1, ry2) > y2):
                return True
            if ry1 == ry2 and y1 < ry1 and y2 > ry1 and not (max(rx1, rx2) < x1 or min(rx1, rx2) > x2):
                return True
        return False

    def has_sides(x1, y1, x2, y2):
        for x in range(min(x1, x2) + 1, max(x1, x2)):
            for ry in red_or_green_by_col[x]:
                if ry > min(y1, y2) and ry < max(y1, y2):
                    return True
        return False

    max_size = 0
    for i, (x1, y1) in enumerate(red_tiles):
        for x2, y2 in red_tiles[i + 1:]:
            size = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

            if size < max_size:
                continue
            if has_sides(x1, y1, x2, y2):
                continue

            if size > max_size:
                max_size = size

    return max_size
