# Advent of Code 2023
# Day 14

from pprint import pprint

# Don't move anything just keep a running list
# of the highest spot it could land and add that
# to a running total
def part_one(platform: list[list[str]]):
    weights = [0 for _ in platform[0]]
    blockers = [0 for _ in platform[0]]
    for r, row in enumerate(platform):
        for c, char in enumerate(row):
            match char:
                case '#':
                    blockers[c] = r + 1
                    continue
                case 'O':
                    weights[c] += len(platform) - blockers[c]
                    blockers[c] += 1
                    continue
    return sum(weights)

def rotate(platform: list[list[str]]):
    new_platform = [['?' for _ in range(len(platform[0]))] for _ in range(len(platform))]
    for r, row in enumerate(platform):
        for c, char in enumerate(row):
            new_platform[c][len(row) - 1 - r] = char
    return new_platform

def tiltEast(platform: list[list[str]]):
    new_platform = []
    for row in platform:
        line = ''.join(row)
        while 'O.' in line:
            line = line.replace('O.', '.O')
        new_platform.append(list(line))
    return new_platform

def calc_load(platform: list[list[str]]):
    weight = 0
    for r, row in enumerate(platform):
        for c, char in enumerate(row):
            if char == 'O':
                weight += len(platform) - r
    return weight

def part_two(platform: list[list[str]]):
    new = rotate(platform)
    seen = {}
    target = 1_000_000_000
    cycle = 0
    while cycle < target:
        cycle += 1
        for _ in range(4):
            new = rotate(tiltEast(new))
        key = tuple(tuple(row) for row in new)
        if key in seen:
            cycle_length = cycle - seen[key]
            skip_amount = (target - cycle) // cycle_length
            cycle += skip_amount * cycle_length
        seen[key] = cycle

    final = rotate(rotate(rotate(new))) # undo initial rotate
    return calc_load(final)

if __name__ == "__main__":
    with open("input/day14.txt") as f:
        data = [list(line.strip()) for line in f.readlines()]
    
    print('---- Part One ----')
    print(part_one(data)) # 110128

    print('---- Part Two ----')
    print(part_two(data)) # 103861
