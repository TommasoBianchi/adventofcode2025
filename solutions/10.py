import re
import numpy as np
from scipy.optimize import LinearConstraint, milp

def parse_input(file):
    machines = []
    for line in file.readlines():
        line = line.strip()
        match = re.match(r'\[(.*)\] (\(.*\))* \{(.*)\}', line)
        target, buttons, joltage = match.groups()
        machines.append((
            target,
            [[int(el) for el in b[1:-1].split(',')] for b in buttons.split(' ')],
            [int(j) for j in joltage.split(',')]
        ))
    return machines

def print_state(state):
    return str(bin(state)).replace('1', '#').replace('0', '.')

def compute_transition(state, button, num_lights):
    new_state = state
    for b in button:
        new_state = new_state ^ (1 << (num_lights - 1 - b))
    return new_state

def compute_shortest_path_length(num_lights, buttons, target):
    num_nodes = 2 ** num_lights
    distances = [num_nodes + 1 for _ in range(num_nodes)]
    distances[0] = 0
    open_set = [0]

    while len(open_set) > 0:
        state = open_set.pop()
        for button in buttons:
            new_state = compute_transition(state, button, num_lights)
            if distances[new_state] > distances[state] + 1:
                distances[new_state] = distances[state] + 1
                open_set.append(new_state)

    return distances[target]

def solve_first(file):
    machines = parse_input(file)

    result = 0
    for target, buttons, _ in machines:
        result += compute_shortest_path_length(len(target), buttons, int(target.replace('#', '1').replace('.', '0'), 2))

    return result

def solve_scipy(buttons, joltage):
    c = np.ones(len(buttons))
    integrality = np.ones(len(buttons))
    A = []
    for i in range(len(joltage)):
        row = []
        for button in buttons:
            row.append(1 if i in button else 0)
        A.append(row)
    A = np.array(A)
    b = np.array(joltage)
    constraints = LinearConstraint(A, b, b)
    res = milp(c=c, constraints=constraints, integrality=integrality)
    assert abs(res.fun - int(res.fun)) < 1e-6
    return int(res.fun)

def solve_second(file):
    machines = parse_input(file)

    result = 0
    for _, buttons, joltage in machines:
        result += solve_scipy(buttons, joltage)
    return result
