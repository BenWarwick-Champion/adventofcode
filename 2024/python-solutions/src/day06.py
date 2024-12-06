# Advent of Code 2023
# Day 06

def get_guard_direction(char: str):
    if char == '^':
        return complex(-1, 0)
    if char == 'v':
        return complex(1, 0)
    if char == '<':
        return complex(0, -1)
    if char == '>':
        return complex(0, 1)
    return None

def parse_map(raw_data):
    grid = dict()
    guard_pos = None
    guard_dir = None
    for r, row in enumerate(raw_data.split('\n')):
        for c, char in enumerate(list(row)):
            grid[complex(r, c)] = char
            if char not in ['.', '#']:
                guard_pos = complex(r, c)
                guard_dir = get_guard_direction(char)

    return grid, guard_pos, guard_dir

def move_guard(grid, guard_pos, guard_dir):
    visited = set()
    visited.add((guard_pos, guard_dir))

    curr_dir = guard_dir
    curr_pos = guard_pos

    loop = False
    seen_new_obstruction = False

    while True:
        next_pos = curr_pos + curr_dir
        next_val = grid.get(next_pos, '0')

        if seen_new_obstruction:
            if (next_pos, curr_dir) in visited:
                loop = True
                break

        if next_val == '0':
            break

        if next_val == 'N':
            seen_new_obstruction = True
            curr_dir *= -1j
            continue

        if next_val == '#':
            curr_dir *= -1j
            continue

        curr_pos = next_pos
        # print('Moving to:', curr_pos)
        visited.add((curr_pos, curr_dir))
    return visited, loop

def part_one(raw_data):
    grid, guard_pos, guard_dir = parse_map(raw_data)
    visited, _ = move_guard(grid, guard_pos, guard_dir)
    return len(set([pos for pos, _ in visited]))

def part_two(raw_data):
    grid, guard_pos, guard_dir = parse_map(raw_data)
    visited, _ = move_guard(grid, guard_pos, guard_dir)

    options = []
    i=1
    total = len(set([pos for pos, _ in visited]))
    for pos in set([pos for pos, _ in visited]):
        print('Checking:', i, 'of', total)
        
        if pos == guard_pos:
            i += 1
            continue
        # print('Checking:', pos)
        old_val = grid[pos]
        grid[pos] = 'N'
        _, loop = move_guard(grid, guard_pos, guard_dir)
        if loop:
            options.append(pos)
        grid[pos] = old_val
        i += 1

        
    return len(options)

if __name__ == "__main__":
    with open("input/day06.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 4374

    print('---- Part Two ----')
    print(part_two(raw_data)) # 1705
