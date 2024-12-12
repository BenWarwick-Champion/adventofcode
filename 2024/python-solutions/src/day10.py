# Advent of Code 2023
# Day 10

from collections import deque

def parse_input(raw_data):
    full_map = dict()
    trailheads = dict()
    for r, row in enumerate(raw_data.split('\n')):
        for c, char in enumerate(list(row)):
            full_map[complex(r, c)] = char
            if char == '0':
                trailheads[complex(r, c)] = 0
    return full_map, trailheads

def find_valid_neighbors(full_map, pos):
    neighbors = []
    for direction in [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]:
        neighbor_pos = pos + direction
        next_pos = full_map.get(neighbor_pos, 'oob')
        if next_pos != 'oob' and int(next_pos) == int(full_map[pos]) + 1:
            neighbors.append(neighbor_pos)
    return neighbors

def calc_trailhead_score(full_map, trailhead):
    curr_pos = trailhead
    trail_endings = []
    candidates = deque(find_valid_neighbors(full_map, curr_pos))

    while len(candidates) > 0:
        curr_pos = candidates.popleft()
        if full_map[curr_pos] == '9':
            trail_endings.append(curr_pos)
            continue
        neighbors = find_valid_neighbors(full_map, curr_pos)
        for neighbor in neighbors:
            candidates.append(neighbor)
    return trail_endings


def part_one(raw_data):
    full_map, trailheads = parse_input(raw_data)
    total = 0
    for trailhead in trailheads:
        print('Trailhead:', trailhead)
        total += len(set(calc_trailhead_score(full_map, trailhead)))
    return total

def part_two(raw_data):
    full_map, trailheads = parse_input(raw_data)
    total = 0
    for trailhead in trailheads:
        print('Trailhead:', trailhead)
        total += len(calc_trailhead_score(full_map, trailhead))
    return total

if __name__ == "__main__":
    with open("input/day10.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))
