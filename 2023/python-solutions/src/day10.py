
joining_pipes = {
    '|': [1, -1],
    '-': [-1j, 1j],
    'L': [-1, 1j],
    'J': [-1, -1j],
    '7': [1, -1j],
    'F': [1, 1j],
}

visualisation = {
    '|': '║',
    '-': '═',
    'L': '╚',
    'J': '╝',
    '7': '╗',
    'F': '╔',
}

def find_start(raw_data: list[list[str]]):
    for r, row in enumerate(raw_data):
        for c, char in enumerate(row):
            if char == 'S':
                return complex(r, c)
    return complex(0, 0)

def find_joining_pipes(current: complex, raw_data: list[list[str]]):
    connecting = []
    r = int(current.real)
    c = int(current.imag)
    # North
    if raw_data[r - 1][c] in ['F', '|', '7']:
        connecting.append(current - 1)
    
    # South
    if raw_data[r + 1][c] in ['L', '|', 'J']:
        connecting.append(current + 1)

    # West
    if raw_data[r][c - 1] in ['L', '-', 'F']:
        connecting.append(current - 1j)

    # East
    if raw_data[r][c + 1] in ['J', '-', '7']:
        connecting.append(current + 1j)

    return connecting


def part_one(raw_data: list[list[str]]):
    start = find_start(raw_data)
    connecting = find_joining_pipes(start, raw_data)

    current = connecting[0]
    last = start
    steps = 0

    output = [['.' for _ in row] for row in raw_data]
    output[int(start.real)][int(start.imag)] = visualisation['J']

    while current != start:
        steps += 1
        r = int(current.real)
        c = int(current.imag)
        pipe = raw_data[r][c]
        output[r][c] = visualisation[pipe]
        for d in joining_pipes[pipe]:
            if (current + d) != last:
                last = current
                current = current + d
                break  
    
    with open('./output/day10_1.txt', 'w') as f:
        f.write('\n'.join([''.join(line) for line in output]))
    return (steps + 1) // 2

def is_inside(point: complex, loop: list[list[str]]):
    crosses = 0
    r = int(point.real)
    c = int(point.imag)
    while c < len(loop[0]) and r < len(loop):
        curr = loop[r][c]
        if curr != '.' and curr != visualisation['L'] and curr != visualisation['7']:
            crosses += 1
        r += 1
        c += 1
    
    return (crosses % 2 == 1)

def part_two(raw_data: list[list[str]]):
    start = find_start(raw_data)
    connecting = find_joining_pipes(start, raw_data)

    current = connecting[0]
    last = start
    steps = 0

    output = [['.' for _ in row] for row in raw_data]
    output[int(start.real)][int(start.imag)] = visualisation['J']

    while current != start:
        steps += 1
        r = int(current.real)
        c = int(current.imag)
        pipe = raw_data[r][c]
        output[r][c] = visualisation[pipe]
        for d in joining_pipes[pipe]:
            if (current + d) != last:
                last = current
                current = current + d
                break  
    
    inside = 0
    for r, row in enumerate(output):
        for c, char in enumerate(row):
            if char == '.':
                if is_inside(complex(r, c), output):
                    inside += 1
    return inside

if __name__ == "__main__":
    with open('./input/day10.txt') as f:
        raw_data = [list(line.strip()) for line in f.readlines()]

    print('---- Part One ----') # 6733
    print(part_one(raw_data))

    print('---- Part Two ----') # 435
    print(part_two(raw_data))
