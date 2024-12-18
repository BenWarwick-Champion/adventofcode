# Advent of Code 2023
# Day 18

from collections import deque

# Example
# MEMORY_SPACE = 7
# START = complex(0, 0)
# END = complex(6, 6)

# Real
MEMORY_SPACE = 71
START = complex(0, 0)
END = complex(70, 70)

def parse_data(raw_data, steps=1024):
    grid = {complex(r, c): '.' for r in range(MEMORY_SPACE) for c in range(MEMORY_SPACE)}
    blocks = dict()
    for i, line in enumerate(raw_data):
        if i == steps:
            break
        x, y = line.split(',')
        x = int(x)
        y = int(y)
        grid[complex(y, x)] = '#'
        blocks[complex(y, x)] = '#'
    return grid, blocks

def print_grid(grid):
    for r in range(MEMORY_SPACE):
        row = []
        for c in range(MEMORY_SPACE):
            row.append(grid[complex(r, c)])
        print(''.join(row))

def bfs(grid):
    start = START
    end = END
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        # visited.add(current)
        for direction in [1, -1, 1j, -1j]:
            new_pos = current + direction
            if new_pos in visited:
                continue
            if grid.get(new_pos, '#') == '.':
                queue.append((new_pos, steps + 1))
                visited.add(new_pos)
    return -1

def part_one(raw_data):
    grid, _ = parse_data(raw_data, 1024)
    print_grid(grid)
    return bfs(grid)

def part_two(raw_data):
    for i in range(1024, 9999):
        grid, blocks = parse_data(raw_data, i)
        if (bfs(grid) == -1):
            block = list(blocks.keys())[-1]
            return ','.join([str(int(block.imag)), str(int(block.real))])
    return None

if __name__ == "__main__":
    with open("input/day18.txt") as f:
        raw_data = f.readlines()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 272

    print('---- Part Two ----')
    print(part_two(raw_data)) # 16,44
