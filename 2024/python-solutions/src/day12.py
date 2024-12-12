# Advent of Code 2023
# Day 12

from pprint import pprint
from math import inf

def parse_input(raw_data):
    garden = dict()
    for r, row in enumerate(raw_data.split('\n')):
        for c, char in enumerate(list(row)):
            garden[complex(r, c)] = char
    return garden

def find_neighbours(garden, pos):
    neighbours = []
    for direction in [complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)]:
        neighbour_pos = pos + direction
        neighbour_val = garden.get(neighbour_pos, 'oob')
        if neighbour_val == 'oob':
            continue
        if neighbour_val == garden[pos]:
            neighbours.append(neighbour_pos)
    return neighbours

def find_region(garden, pos):
    region = set()
    edges = set()
    candidates = set([pos])
    perimeter = 0
    while len(candidates) > 0:
        curr_pos = candidates.pop()
        region.add(curr_pos)
        neighbours = find_neighbours(garden, curr_pos)
        perimeter += 4 - len(neighbours)
        if (len(neighbours) < 4):
            edges.add(curr_pos)
        for neighbour in neighbours:
            if neighbour not in region:
                candidates.add(neighbour)
    return len(region), perimeter, region, edges    

def find_sides(region):
    # print('Region:', region)
    sides = 0
    min_row = min([pos.real for pos in region])
    min_imag = min([int(pos.imag) if pos.real == min_row else inf for pos in region])
    top_left = complex(min_row, min_imag)
    start_dir = complex(0, 1)

    curr_pos = top_left
    curr_dir = start_dir

    if len(region) == 1:
        return 4

    iteration = 0
    visited = set()
    while True:
        visited.add(curr_pos)
        next_pos = curr_pos + curr_dir
        turn_left_pos = curr_pos + curr_dir * 1j

        if (curr_pos == top_left) and (curr_dir == start_dir) and iteration > 0:
            break

        if turn_left_pos in region:
            sides += 1
            curr_dir *= 1j
            curr_pos = turn_left_pos
            continue

        if next_pos not in region:
            sides += 1
            curr_dir *= -1j
            continue

        iteration += 1
        curr_pos = next_pos

    print('Sides:', sides)
    return sides

def find_corners(region):
    sides = 0
    for pos in region:
        # Outer corners
        sides += pos - 1 not in region and pos - 1j not in region
        sides += pos + 1 not in region and pos - 1j not in region
        sides += pos - 1 not in region and pos + 1j not in region
        sides += pos + 1 not in region and pos + 1j not in region
        # Inner corners
        sides += pos - 1 in region and pos - 1j in region and pos - 1 - 1j not in region
        sides += pos + 1 in region and pos - 1j in region and pos + 1 - 1j not in region
        sides += pos - 1 in region and pos + 1j in region and pos - 1 + 1j not in region
        sides += pos + 1 in region and pos + 1j in region and pos + 1 + 1j not in region
    return sides

def part_one(raw_data):
    garden = parse_input(raw_data)
    seen = set()
    regions = []
    for pos in garden:
        if pos in seen:
            continue
        
        area, perimeter, region, _ = find_region(garden, pos)
        regions.append((garden[pos], area, perimeter))
        seen.update(region)

    return sum(p * r for _, p, r in regions)

def part_two(raw_data):
    garden = parse_input(raw_data)
    seen = set()
    regions = []
    for pos in garden:
        if pos in seen:
            continue
        area, perimeter, region, _ = find_region(garden, pos)
        sides = find_corners(region)
        regions.append((garden[pos], area, perimeter, sides))
        seen.update(region)
    return sum(p * s for _, p, _, s in regions)

if __name__ == "__main__":
    with open("input/day12.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 1424472

    print('---- Part Two ----')
    print(part_two(raw_data)) # 870202
