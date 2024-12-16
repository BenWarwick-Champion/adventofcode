# Advent of Code 2023
# Day 16

from collections import deque

def parse_data(raw_data):
    maze = dict()
    walls = set()
    for r, row in enumerate(raw_data):
        for c, char in enumerate(row):
            maze[complex(r, c)] = char
            if char == '#':
                walls.add(complex(r, c))
            if char == 'S':
                start = complex(r, c)
            if char == 'E':
                end = complex(r, c)
    return maze, walls, start, end

def print_maze(maze, path):
    n_rows = int(max(p.real for p in maze) + 1)
    n_cols = int(max(p.imag for p in maze))
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            pos = complex(r, c)
            if pos in path:
                row.append('O')
            else:
                row.append(maze[pos])
        print(''.join(row))

def find_neighbours(maze, walls, pos):
    neighbours = []
    for d in [1, -1, 1j, -1j]:
        new_pos = pos + d
        if new_pos in maze and new_pos not in walls:
            neighbours.append(new_pos)
    return neighbours

def bfs(maze, walls, start, end):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            return path + [end]
        if pos in visited:
            continue
        visited.add(pos)
        for neighbour in find_neighbours(maze, walls, pos):
            queue.append((neighbour, path + [pos]))
    return -1

def score(path):
    direction = -1j
    total = 0
    for pos in path:
        if pos + direction in path:
            total += 1
        else:
            total += 1000
            if pos + direction * 1j in path:
                direction *= 1j
            else:
                direction *= -1j
    return total

def part_one(raw_data):
    maze, walls, start, end = parse_data(raw_data)
    shortest_path = bfs(maze, walls, start, end)
    print_maze(maze, shortest_path)
    return score(shortest_path)

def part_two(raw_data):
    return

if __name__ == "__main__":
    with open("input/_day16.txt") as f:
        raw_data = f.readlines()
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))
