# Advent of Code 2023
# Day 13

def only_digits(s):
    return int(''.join([c for c in s if c.isdigit()]))

def parse_line(line):
    nums = list(map(only_digits, line.split(',')))
    return complex(nums[0], nums[1])

def parse_input(raw_data):
    raw_machines = raw_data.split('\n\n')
    machines = []
    for machine in raw_machines:
        lines = machine.split('\n')
        a = parse_line(lines[0])
        b = parse_line(lines[1])
        prize = parse_line(lines[2])
        machines.append((a, b, prize))
    return machines

def play_machine(machine):
    a, b, prize = machine
    candidates = []
    for x in range(100):
        for y in range(100):
            ans = a * x + b * y
            if (ans == prize):
                candidates.append((x, y))
    if len(candidates) == 0:
        return 0
    return min(x*3 + y for x, y in candidates)

def part_one(raw_data):
    machines = parse_input(raw_data)
    total = 0
    for machine in machines:
        total += play_machine(machine)
    return total

def part_two(raw_data):
    machines = parse_input(raw_data)
    conversion_error = 10_000_000_000_000
    total = 0
    for machine in machines:
        a, b, prize = machine
        prize = complex(prize.real + conversion_error, prize.imag + conversion_error)
        # Cramer's rule
        determinant = a.real * b.imag - a.imag * b.real
        a_presses = (prize.real * b.imag - prize.imag * b.real) / determinant
        b_presses = (a.real * prize.imag - a.imag * prize.real) / determinant

        if (a*int(a_presses) + b*int(b_presses) == prize):
            total += int(a_presses)*3 + int(b_presses)

    return total

if __name__ == "__main__":
    with open("input/day13.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 27157

    print('---- Part Two ----')
    print(part_two(raw_data)) # 104015411578548
