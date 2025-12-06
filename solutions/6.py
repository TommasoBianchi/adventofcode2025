def parse_input(file):
    grid = []
    for line in file.readlines():
        grid.append(list(line.replace('\n', '')))
    return grid

def compute(op, ops):
        res = 0 if op == "+" else 1
        for o in ops:
            if op == "+":
                res += o
            else:
                res *= o
        return res

def transpose(grid):
    transposed = [[] for _ in grid[0]]
    for row_index, row in enumerate(grid):
        for col_index, el in enumerate(row):
            transposed[col_index].append(el)
    return transposed

def solve_first(file):
    # Solved on mobile
    lines = [line.strip() for line in file.readlines() if line.strip() != ""]
    operations = [[int(el)] for el in lines[0].split(' ') if len(el) > 0]
    for line in lines[1:-1]:
        for el, ops in zip([x for x in line.split(' ') if len(x) > 0], operations):
            ops.append(int(el))
    
    result = 0 
    for ops, symbol in zip(operations, [s for s in lines[-1].split(' ') if len(s) > 0]):
        result += compute(symbol, ops)

    return result

def solve_second(file):
    grid = parse_input(file)

    transposed = transpose(grid)
    problems = []
    current_operands = []
    current_operator = None
    for row in transposed:
        if row[-1] in ['+', '*']:
            current_operator = row[-1]
            row[-1] = ''
        
        joined = ''.join(row).strip()
        if joined == '':
            problems.append((current_operands, current_operator))
            current_operands = []
            current_operator = None
            continue

        current_operands.append(int(joined))
    problems.append((current_operands, current_operator))
    
    result = 0 
    for operands, operator in problems:
        result += compute(operator, operands)

    return result
