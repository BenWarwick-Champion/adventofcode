import string
from pprint import pprint
from collections import defaultdict


def parse_map(raw_map: str):
    lines = raw_map.split('\n')
    numbers = [[int(num) for num in line.split()] for ind, line in enumerate(lines) if ind != 0]
    # new_map = {}
    # for ind, line in enumerate(lines):
    #     if ind == 0:
    #         continue
    #     for num in line.split():

    return numbers


def parse(raw_data: list[str]):
    seeds = [int(num) for num in raw_data[0].split(':')[1].strip().split()]
    maps = [parse_map(raw_map[1]) for raw_map in enumerate(raw_data) if raw_map[0] != 0]
    return seeds, maps

# destination range start, the source range start, and the range length.
def convert(seed, farmer_map: list[list[int]]):
    converted = False
    output_seed = 0
    for curr_range in farmer_map:
        start = curr_range[1]
        end = curr_range[1] + curr_range[2]
        if seed >= start and seed < end:
            converted = True
            diff = curr_range[0] - curr_range[1]
            output_seed = seed + diff
            break
    if converted:
        return output_seed
    return seed

def part_one(raw_data: list[str]):
    seeds, maps = parse(raw_data)
    locations = []
    for seed in seeds:
        curr_seed = seed
        for farmer_map in maps:
            curr_seed = convert(curr_seed, farmer_map)
        locations.append(curr_seed)
    return min(locations)

def parse_seed_ranges(seeds: list[str]):
    pairs = list(zip(seeds[0::2], seeds[1::2]))
    
    # Hacky "pen & paper" solution using approximation to find the
    # likely seed range and then just brute forcing from there
    for pair in [pairs[6]]:
        num = pair[0]
        # yield pair[0]
        # yield pair[0] + pair[1] // 2
        # yield pair[0] + pair[1]
        for i in range(pair[1]):
            yield num + i


def part_two(raw_data: list[str]):
    seeds, maps = parse(raw_data)
    locations = []
    for seed in parse_seed_ranges(seeds):
        curr_seed = seed
        for farmer_map in maps:
            curr_seed = convert(curr_seed, farmer_map)
        locations.append(curr_seed)
    return min(locations)

if __name__ == "__main__":
    with open('./input/day05.txt') as f:
        raw_data = f.read().split('\n\n')

    print('---- Part One ----') # 331445006
    print(part_one(raw_data))

    print('---- Part Two ----') # 6472060
    print(part_two(raw_data))

