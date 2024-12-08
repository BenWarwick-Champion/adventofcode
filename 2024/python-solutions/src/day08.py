# Advent of Code 2023
# Day 08

from collections import defaultdict

def parse_map(raw_data):
    full_map = dict()
    frequencies = defaultdict(list)
    for r, row in enumerate(raw_data.split('\n')):
        for c, char in enumerate(list(row)):
            full_map[complex(r, c)] = char
            if char != '.':
                frequencies[char].append(complex(r, c))
    return full_map, frequencies

def get_antinode(pos1, pos2):
    real_diff = pos2.real - pos1.real
    imag_diff = pos2.imag - pos1.imag
    return complex(pos2.real + real_diff, pos2.imag + imag_diff)


def find_antinodes(full_map, frequency: list):
    antinodes = set()
    for pos1 in frequency:
        for pos2 in frequency:
            if pos1 == pos2:
                continue
            antinode = get_antinode(pos1, pos2)
            if full_map.get(antinode, 'oob') != 'oob':
                antinodes.add(antinode)
    return antinodes

def part_one(raw_data):
    full_map, frequencies = parse_map(raw_data)
    antinodes_map = dict()
    for frequency in frequencies:
        print('Frequency:', frequency)
        antinodes = find_antinodes(full_map, frequencies[frequency])
        print('Antinodes:', antinodes)
        for antinode_pos in antinodes:
            antinodes_map[antinode_pos] = antinodes_map.get(antinode_pos, 0) + 1
    return len(antinodes_map)


def get_antinode_dir(pos1, pos2):
    real_diff = pos2.real - pos1.real
    imag_diff = pos2.imag - pos1.imag
    return complex(real_diff, imag_diff)


def find_antinodes_p2(full_map, frequency: list):
    antinodes = set()
    for pos1 in frequency:
        for pos2 in frequency:
            if pos1 == pos2:
                continue
            antinode_dir = get_antinode_dir(pos1, pos2)
            i = 1
            while full_map.get(pos1 + antinode_dir * i, 'oob') != 'oob':
                antinode = pos1 + antinode_dir * i
                antinodes.add(antinode)
                i += 1
    return antinodes

def part_two(raw_data):
    full_map, frequencies = parse_map(raw_data)
    antinodes_map = dict()
    for frequency in frequencies:
        # print('Frequency:', frequency)
        antinodes = find_antinodes_p2(full_map, frequencies[frequency])
        # print('Antinodes:', antinodes)
        for antinode_pos in antinodes:
            antinodes_map[antinode_pos] = antinodes_map.get(antinode_pos, 0) + 1
    return len(antinodes_map)

if __name__ == "__main__":
    with open("input/day08.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 364

    print('---- Part Two ----')
    print(part_two(raw_data)) # 1231
