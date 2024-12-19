# Advent of Code 2023
# Day 19

from functools import cache

def parse_data(raw_data):
    towels, patterns = raw_data.split('\n\n')
    towels = frozenset([t.strip() for t in towels.split(',')])
    patterns = [p.strip() for p in patterns.split('\n')]
    return towels, patterns

# @lru_cache(maxsize=None)
# def check_design(design, patterns):
#     if not design:
#         return True
#     return sum(
#         check_design(remove_prefix(pattern, design), patterns)
#         for pattern in patterns
#         if design.startswith(pattern)
#     )

@cache
def match(towels, pattern):
    if not pattern:
        return 1
    return sum(
        match(towels, pattern[len(towel):])
        for towel in towels 
        if pattern.startswith(towel)
    )

def part_one(raw_data):
    towels, patterns = parse_data(raw_data)
    total = 0
    for pattern in patterns:
        if match(towels, pattern):
            total += 1
    return total

def part_two(raw_data):
    towels, patterns = parse_data(raw_data)
    total = 0
    for pattern in patterns:
        total += match(towels, pattern)
    return total

if __name__ == "__main__":
    with open("input/day19.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 278

    print('---- Part Two ----')
    print(part_two(raw_data)) # 569808947758890
