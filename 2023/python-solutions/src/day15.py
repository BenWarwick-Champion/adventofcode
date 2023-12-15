# Advent of Code 2023
# Day 15
from collections import OrderedDict
from pprint import pprint

def HASH(input: str):
    value = 0
    for char in input:
        val = ord(char)
        value += val
        value *= 17
        value = value % 256
    return value

def part_one(raw_data: str):
    instructions = raw_data.split(',')
    return sum(HASH(instr) for instr in instructions)

def calc_focusing_power(HASHMAP: dict[int, OrderedDict[str, str]]):
    power = 0
    for key in HASHMAP:
        if len(HASHMAP[key]) == 0:
            continue
        box_power = key + 1
        slot = 0
        for label in HASHMAP[key]:
            slot += 1
            power += box_power * slot * int(HASHMAP[key][label])
    return power

def part_two(raw_data):
    instructions = raw_data.split(',')
    HASHMAP = {i: OrderedDict() for i in range(256)}
    for instr in instructions:
        if '=' in instr:
            label, focal_length = instr.split('=')
            key = HASH(label)
            HASHMAP[key][label] = focal_length
        else:
            label = instr[:-1]
            key = HASH(label)
            if label in HASHMAP[key]:
                HASHMAP[key].pop(label)
    return calc_focusing_power(HASHMAP)

if __name__ == "__main__":
    with open("input/day15.txt") as f:
        raw_data = f.read().strip()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 517551

    print('---- Part Two ----')
    print(part_two(raw_data)) # 286097
