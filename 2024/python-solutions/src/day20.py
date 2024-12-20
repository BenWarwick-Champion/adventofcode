# Advent of Code 2023
# Day 20

from collections import deque
from itertools import combinations

def parse_data(raw_data):
    grid = dict()
    for r, row in enumerate(raw_data.split('\n')):
        for c, char in enumerate(row):
            if char != '#':
                grid[complex(r, c)] = char
            if char == 'S':
                start = complex(r, c)
            if char == 'E':
                end = complex(r, c)
    return grid, start, end

def part_one(raw_data):
    grid, start, end = parse_data(raw_data)

    distances = dict()
    queue = deque([start])
    distances[start] = 0

    # Flood fill the grid with distances
    while queue:
        current = queue.popleft()
        for direction in [1, -1, 1j, -1j]:
            new_pos = current + direction
            if new_pos in grid and new_pos not in distances:
                distances[new_pos] = distances[current] + 1
                queue.append(new_pos)

    # Distance between every pair of points
    total = 0
    for (pos1, dist1), (pos2, dist2) in combinations(distances.items(), 2):
        d = abs((pos1 - pos2).real) + abs((pos1 - pos2).imag)
        if d == 2:
            if dist2 - dist1 - d >= 100:
                total += 1

    return total

def part_two(raw_data):
    grid, start, end = parse_data(raw_data)

    distances = dict()
    queue = deque([start])
    distances[start] = 0

    # Flood fill the grid with distances
    while queue:
        current = queue.popleft()
        for direction in [1, -1, 1j, -1j]:
            new_pos = current + direction
            if new_pos in grid and new_pos not in distances:
                distances[new_pos] = distances[current] + 1
                queue.append(new_pos)

    # Distance between every pair of points
    total = 0
    for (pos1, dist1), (pos2, dist2) in combinations(distances.items(), 2):
        d = abs((pos1 - pos2).real) + abs((pos1 - pos2).imag)
        if d <= 20:
            if dist2 - dist1 - d >= 100:
                total += 1

    return total

if __name__ == "__main__":
    with open("input/day20.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 1409

    print('---- Part Two ----')
    print(part_two(raw_data)) # 1012821
