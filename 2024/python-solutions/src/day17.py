# Advent of Code 2023
# Day 17

def parse_data(raw_data):
    registers, instructions = raw_data.split('\n\n')
    registers = [int(r.split(':')[1].strip()) for r in registers.split('\n')]
    instructions = [int(n) for n in instructions.split(':')[1].strip().split(',')]
    return registers, instructions

def combo(literal, a, b, c):
    if literal < 4:
        return literal
    else:
        match literal:
            case 4: return a
            case 5: return b
            case 6: return c
            case 7: return None
            case _: return None

def run(registers, instructions):
    a, b, c = registers
    pos = 0
    output = []

    while pos < len(instructions):
        opcode = instructions[pos]
        operand = instructions[pos + 1]

        match opcode:
            case 0:
                a = int(a / (2**combo(operand, a, b, c)))
                pos += 2
            case 1:
                b = b ^ operand
                pos += 2
            case 2:
                b = combo(operand, a, b, c) % 8
                pos += 2
            case 3:
                if a == 0:
                    pos += 2
                else:
                    pos = operand
            case 4:
                b = b ^ c
                pos += 2
            case 5:
                output.append(combo(operand, a, b, c) % 8)
                pos += 2
            case 6:
                b = int(a / (2**combo(operand, a, b, c)))
                pos += 2
            case 7:
                c = int(a / (2**combo(operand, a, b, c)))
                pos += 2
            case _:
                print('Invalid opcode')
                break
    return a, b, c, output

def part_one(raw_data):
    registers, instructions = parse_data(raw_data)
    a, b, c, output = run(registers, instructions)
    return ','.join(str(n) for n in output)

def part_two(raw_data):
    registers, instructions = parse_data(raw_data)
    registers[0] += 1
    _, _, _, output = run(registers, instructions)


    todo = [(1, 0)]
    candidates = []
    for i, a in todo:
        for a in range(a, a+8):
            registers[0] = a
            _, _, _, output = run(registers, instructions)
            if output[-i:] == instructions[-i:]:
                todo += [(i+1, a*8)]
                if i == len(instructions):
                    candidates.append(a)
    return min(candidates)

    while len(output) < len(instructions):
        registers[0] *= 10
        _, _, _, output = run(registers, instructions)

    print('Registers:', registers)
    print('Instructions:', instructions)
    print('Output:      ', output)

    while output[-1] != instructions[-1]:
        registers[0] += 10**(len(str(registers[0])) - 4)
        _, _, _, output = run(registers, instructions)

    print('Registers:', registers)
    print('Instructions:', instructions)
    print('Output:      ', output)

    while \
        output[-6] != instructions[-6] or \
        output[-5] != instructions[-5] or \
        output[-4] != instructions[-4] or \
        output[-3] != instructions[-3] or \
        output[-2] != instructions[-2] or \
        output[-1] != instructions[-1]:
        registers[0] += 10**(len(str(registers[0])) - 7)
        _, _, _, output = run(registers, instructions)

    print('Registers:', registers)
    print('Instructions:', instructions)
    print('Output:      ', output)

    while \
        output[-9] != instructions[-9] or \
        output[-8] != instructions[-8] or \
        output[-7] != instructions[-7] or \
        output[-6] != instructions[-6] or \
        output[-5] != instructions[-5] or \
        output[-4] != instructions[-4] or \
        output[-3] != instructions[-3] or \
        output[-2] != instructions[-2] or \
        output[-1] != instructions[-1]:
        registers[0] += 10**(len(str(registers[0])) - 8)
        _, _, _, output = run(registers, instructions)

    print('Registers:', registers)
    print('Instructions:', instructions)
    print('Output:      ', output)

    while \
        output[-12] != instructions[-12] or \
        output[-11] != instructions[-11] or \
        output[-10] != instructions[-10] or \
        output[-9] != instructions[-9] or \
        output[-8] != instructions[-8] or \
        output[-7] != instructions[-7] or \
        output[-6] != instructions[-6] or \
        output[-5] != instructions[-5] or \
        output[-4] != instructions[-4] or \
        output[-3] != instructions[-3] or \
        output[-2] != instructions[-2] or \
        output[-1] != instructions[-1]:
        registers[0] += 10**(len(str(registers[0])) - 11)
        _, _, _, output = run(registers, instructions)

    print('Registers:', registers)
    print('Instructions:', instructions)
    print('Output:      ', output)

    while \
        output[-15] != instructions[-15] or \
        output[-14] != instructions[-14] or \
        output[-13] != instructions[-13] or \
        output[-12] != instructions[-12] or \
        output[-11] != instructions[-11] or \
        output[-10] != instructions[-10] or \
        output[-9] != instructions[-9] or \
        output[-8] != instructions[-8] or \
        output[-7] != instructions[-7] or \
        output[-6] != instructions[-6] or \
        output[-5] != instructions[-5] or \
        output[-4] != instructions[-4] or \
        output[-3] != instructions[-3] or \
        output[-2] != instructions[-2] or \
        output[-1] != instructions[-1]:
        registers[0] += 10**(len(str(registers[0])) - 14)
        _, _, _, output = run(registers, instructions)

    print('Registers:', registers)
    print('Instructions:', instructions)
    print('Output:      ', output)


    while output != instructions:
        registers[0] += 1
        _, _, _, output = run(registers, instructions)

    print('Registers:', registers)
    print('Instructions:', instructions)
    print('Output:      ', output)

    return registers

if __name__ == "__main__":
    with open("input/day17.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))

    # 207976803417103 too high
    # 190384617372687 too high
