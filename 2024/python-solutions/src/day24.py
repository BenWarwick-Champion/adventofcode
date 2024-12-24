# Advent of Code 2023
# Day 24

def parse(raw_data):
    initial_state, raw_gates = raw_data.split('\n\n')
    wires = {}
    gates = {}
    for line in initial_state.split('\n'):
        wire, value = line.split(':')
        wires[wire] = int(value)
    for gate in raw_gates.split('\n'):
        operation, target = gate.split(' -> ')
        source1, operator, source2 = operation.split()
        gates[target] = (operator, source1, source2)
    return wires, gates

def operate(gate, wires):
    operator, source1, source2 = gate
    if operator == 'AND':
        return wires[source1] & wires[source2]
    if operator == 'OR':
        return wires[source1] | wires[source2]
    if operator == 'XOR':
        return wires[source1] ^ wires[source2]
    print('Operator not found:', operator)
    return

def part_one(raw_data):
    wires, gates = parse(raw_data)
    queue = list(gates.keys())
    while queue:
        gate = queue.pop(0)
        _, source1, source2 = gates[gate]
        if source1 not in wires or source2 not in wires:
            queue.append(gate)
            continue
        wires[gate] = operate(gates[gate], wires)

    zs = [wire for wire in wires if wire.startswith('z')]
    zs = sorted(zs, key=lambda x: int(x[1:]), reverse=True)
    return int(''.join([str(wires[z]) for z in zs]), 2)

def compute(wires, gates):
    queue = list(gates.keys())
    while queue:
        gate = queue.pop(0)
        _, source1, source2 = gates[gate]
        if source1 not in wires or source2 not in wires:
            queue.append(gate)
            continue
        wires[gate] = operate(gates[gate], wires)
    return wires

def num(wires, char):
    cs = [wire for wire in wires if wire.startswith(char)]
    cs = sorted(cs, key=lambda x: int(x[1:]), reverse=True)
    return ''.join([str(wires[c]) for c in cs])

def part_two(raw_data):
    wires, gates = parse(raw_data)
    wires = compute(wires, gates)

    wires_0 = {wire: 1 for wire in wires}
    wires = compute(wires_0, gates)


    x = num(wires, 'x')
    print('X:', x, int(x, 2))

    y = num(wires, 'y')
    print('Y:', y, int(y, 2))

    z = num(wires, 'z')
    print('Z:', z, int(z, 2))

    answer = int(x, 2) + int(y, 2)
    print('A:', bin(answer)[2:], answer)
    return

if __name__ == "__main__":
    with open("input/day24.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 38869984335432

    print('---- Part Two ----')
    print(part_two(raw_data))
