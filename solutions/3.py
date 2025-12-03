def parse_input(file):
    return [line.strip() for line in file.readlines()]

def compute_bank_joltage(bank):
    max_index = 0
    for i in range(1, len(bank) - 1):
        if bank[i] > bank[max_index]:
            max_index = i
    return int(bank[max_index] + max(bank[max_index+1:]))

def compute_bank_joltage_n(bank, n_batteries):
    digits = []
    for digit_id in range(n_batteries - 1):
        max_index = 0
        for i in range(1, len(bank) - (n_batteries - digit_id) + 1):
            if bank[i] > bank[max_index]:
                max_index = i
        digits.append(bank[max_index])
        bank = bank[max_index+1:]
    return int(''.join(digits) + max(bank))

def solve_first(file):
    banks = parse_input(file)

    return sum([compute_bank_joltage(bank) for bank in banks])

def solve_second(file):
    banks = parse_input(file)

    return sum([compute_bank_joltage_n(bank, n_batteries=12) for bank in banks])
