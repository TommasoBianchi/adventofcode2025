def parse_input(file):
    outputs_by_device = {}
    for line in file.readlines():
        line = line.strip()
        [device, outputs] = line.split(': ')
        outputs_by_device[device] = outputs.split(' ')
    return outputs_by_device

def compute_num_paths(source, target, outputs_by_device):
    num_paths = {target: 1}

    def _compute_num_paths(device):
        if device in num_paths:
            return num_paths[device]
        
        n = sum([_compute_num_paths(output) for output in outputs_by_device.get(device, [])])
        num_paths[device] = n
        return n
    
    return _compute_num_paths(source)
    
def solve_first(file):
    outputs_by_device = parse_input(file)

    return compute_num_paths('you', 'out', outputs_by_device)

def solve_second(file):
    outputs_by_device = parse_input(file)

    result = 0
    for a, b in [('fft', 'dac'), ('dac', 'fft')]:
        result += compute_num_paths('svr', a, outputs_by_device) * compute_num_paths(a, b, outputs_by_device) * compute_num_paths(b, 'out', outputs_by_device)
    return result
