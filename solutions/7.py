# Fully solved on mobile (cleaned-up version)

def parse_input(file):
    lines = [line.strip() for line in file.readlines()]
    start = None
    splits = []
    for i, line in enumerate(lines):
        start_col = line.find('S')
        if start_col >= 0:
            start = (i, start_col)
            continue
        split_indices = [j for j, c in enumerate(line) if c == '^']
        assert all([b - a > 1 for a, b in zip(split_indices, split_indices[1:])])
        if len(split_indices) > 0:
            splits.append((i, split_indices))
    return start, splits, (len(lines), len(lines[0]))
        

def solve_first(file):
    start, splits, _ = parse_input(file)

    cols = [start[1]]
    num_split = 0

    for _, split_cols in splits:
        new_cols = set()
        for col in cols:
            if col in split_cols:
                num_split += 1
                new_cols.add(col - 1)
                new_cols.add(col + 1)
            else:
                new_cols.add(col)
        cols = list(sorted(new_cols))

    return num_split

def solve_second(file):
    start, splits, (_, width) = parse_input(file)

    cols = [start[1]]
    num_split = 0
    num_rays = [0 for _ in range(width)]
    num_rays[start[1]] = 1

    for _, split_cols in splits:
        new_cols = set()
        for col in cols:
            if col in split_cols:
                num_split += 1
                assert num_rays[col] > 0
                num_rays[col - 1] += num_rays[col]
                num_rays[col + 1] += num_rays[col]
                num_rays[col] = 0
                new_cols.add(col - 1)
                new_cols.add(col + 1)
            else:
                new_cols.add(col)
        cols = list(sorted(new_cols))

    return sum(num_rays)
