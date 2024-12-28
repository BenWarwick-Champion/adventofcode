# Advent of Code 2023
# Day 25

from pprint import pprint

def parse(raw_data):
    keys = []
    locks = []
    for item in raw_data.split('\n\n'):
        lines = item.split('\n')
        if all(char == '#' for char in lines[0]):
            locks.append(item)
        else:
            keys.append(item)
    return keys, locks

def part_one(raw_data):
    keys, locks = parse(raw_data)
    keySets = []
    lockSets = []
    for key in keys:
        keySet = set(complex(r, c) for r, line in enumerate(key.split('\n')) for c, char in enumerate(line) if char == '#')
        keySets.append(keySet)
    for lock in locks:
        lockSet = set(complex(r, c) for r, line in enumerate(lock.split('\n')) for c, char in enumerate(line) if char == '#')
        lockSets.append(lockSet)

    fits = 0
    for lock in lockSets:
        for key in keySets:
            if len(lock.intersection(key)) == 0:
                fits += 1
        
    return fits


def part_two(raw_data):
    return "Deliver the chronicle!"

if __name__ == "__main__":
    with open("input/day25.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))
