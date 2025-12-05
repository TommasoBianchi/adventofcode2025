def parse_input(file):
    fresh_ranges = []
    available_ingredients = []

    for line in file.readlines():
        line = line.strip()
        if "-" in line:
            [start, end] = line.split("-")
            fresh_ranges.append((int(start), int(end)))
        elif len(line) > 0:
            available_ingredients.append(int(line))

    return fresh_ranges, available_ingredients

def merge_ranges(r1, r2):
    if r1[1] < r2[0] or r2[1] < r1[0]:
        return r1, r2
    return (min(r1[0], r2[0]), max(r1[1], r2[1])), None

def solve_first(file):
    fresh_ranges, available_ingredients = parse_input(file)

    count = 0
    for ingredient in available_ingredients:
        if any([ingredient >= start and ingredient <= end for start, end in fresh_ranges]):
            count += 1

    return count

def solve_second(file):
    fresh_ranges, _ = parse_input(file)

    can_merge = True
    while can_merge:
        can_merge = False
        for i in range(len(fresh_ranges)):
            r1 = fresh_ranges[i]
            if r1 is None:
                continue
            for j in range(i+1, len(fresh_ranges)):
                r2 = fresh_ranges[j]
                if r2 is None:
                    continue
                r1, new_r2 = merge_ranges(r1, r2)
                if new_r2 is None:
                    fresh_ranges[i] = r1
                    fresh_ranges[j] = None
                    can_merge = True

    return sum([r[1] - r[0] + 1 for r in fresh_ranges if r is not None])
