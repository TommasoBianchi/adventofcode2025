def parse_input(file):
    junctions = []
    for line in file.readlines():
        line = line.strip()
        x, y, z = line.split(',')
        junctions.append((int(x), int(y), int(z)))
    return junctions

def solve_first(file):
    junctions = parse_input(file)

    pairwise_distances = []
    for i in range(len(junctions)):
        x1, y1, z1 = junctions[i]
        for j in range(i + 1, len(junctions)):
            x2, y2, z2 = junctions[j]
            squared_distance = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            pairwise_distances.append((squared_distance, i, j))
    
    closest_junctions = list(sorted(pairwise_distances))[:1000]

    groups = [-1 for _ in junctions]
    group_sizes = [0 for _ in range(500)]
    next_group_id = 0

    for _, i, j in closest_junctions:
        group1 = groups[i]
        group2 = groups[j]

        if group1 == -1 and group2 == -1:
            groups[i] = next_group_id
            groups[j] = next_group_id
            group_sizes[next_group_id] += 2
            next_group_id += 1
        elif group1 == -1 or group2 == -1:
            group = max(group1, group2)
            groups[i] = group
            groups[j] = group
            group_sizes[group] += 1
        elif group1 == group2:
            pass
        else:
            group = min(group1, group2)
            other_group = max(group1, group2)
            groups[i] = group
            groups[j] = group
            group_sizes[group] += group_sizes[other_group]
            group_sizes[other_group] = 0
            for k in range(len(groups)):
                if groups[k] == other_group:
                    groups[k] = group

    largest_groups = list(sorted(group_sizes, reverse=True))[:3]
    return largest_groups[0] * largest_groups[1] * largest_groups[2]

def solve_second(file):
    junctions = parse_input(file)

    pairwise_distances = []
    for i in range(len(junctions)):
        x1, y1, z1 = junctions[i]
        for j in range(i + 1, len(junctions)):
            x2, y2, z2 = junctions[j]
            squared_distance = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            pairwise_distances.append((squared_distance, i, j))
    
    closest_junctions = list(sorted(pairwise_distances))

    groups = [-1 for _ in junctions]
    group_sizes = [0 for _ in range(len(junctions))]
    next_group_id = 0

    for _, i, j in closest_junctions:
        group1 = groups[i]
        group2 = groups[j]

        if group1 == -1 and group2 == -1:
            group = next_group_id
            groups[i] = group
            groups[j] = group
            group_sizes[group] += 2
            next_group_id += 1
        elif group1 == -1 or group2 == -1:
            group = max(group1, group2)
            groups[i] = group
            groups[j] = group
            group_sizes[group] += 1
        elif group1 == group2:
            group = group1
        else:
            group = min(group1, group2)
            other_group = max(group1, group2)
            groups[i] = group
            groups[j] = group
            group_sizes[group] += group_sizes[other_group]
            group_sizes[other_group] = 0
            for k in range(len(groups)):
                if groups[k] == other_group:
                    groups[k] = group
        
        if group_sizes[group] == len(junctions):
            return junctions[i][0] * junctions[j][0]
    
    assert False
