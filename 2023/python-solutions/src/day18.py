# Advent of Code 2023
# Day 18

directions = {
    'U': -1,
    'D': 1,
    'L': -1j,
    'R': 1j,
    '0': 1j,
    '1': 1,
    '2': -1j,
    '3': -1,
}

def flood_fill(border: list[complex]):
    nodes = set(border)
    Q = {complex(1, 1)}
    while Q:
        curr = Q.pop()
        nodes.add(curr)
        for d in [1, -1, -1j, 1j]:
            if curr + d not in nodes:
                Q.add(curr + d)
    return len(nodes)
    

def part_one(raw_data):
    curr = complex(0)
    visited = [curr]
    for line in raw_data:
        _dir, dist, color = line.strip().split()
        for _ in range(int(dist)):
            curr += directions[_dir]
            visited.append(curr)
    return flood_fill(visited)

def part_two(raw_data):
    pos = 0
    ans = 1
    for line in raw_data:
        _, _, color = line.strip().split()
        color = color.strip('()')
        dist = int(color[1:-1], 16)
        _dir = color[-1]

        pos += directions[_dir].imag * dist
        ans += directions[_dir].real * dist * pos + dist/2
    return int(ans)

if __name__ == "__main__":
    with open("input/day18.txt") as f:
        raw_data = f.readlines()
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))
