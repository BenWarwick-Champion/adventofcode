import string
from pprint import pprint
from collections import defaultdict
from functools import cmp_to_key
import math

def parse_nodes(nodes: str):
    lines = nodes.split('\n')
    node_map = {}
    for line in lines:
        key, value = line.split(' = ')
        value = value.strip('()')
        left, right = value.split(', ')
        node_map[key] = (left, right)
    return node_map

def part_one(instructions: str, nodes: dict[str, tuple[str, str]]):
    current = 'AAA'
    instr_index = 0
    steps = 0
    while True:
        if current == 'ZZZ':
            return steps
        steps += 1
        instr = instructions[instr_index % len(instructions)]
        instr_index += 1
        left, right = nodes[current]
        if instr == "L":
            current = left
        else:
            current = right


def part_two(instructions: str, nodes: dict[str, tuple[str, str]]):
    starts = [key for key in nodes if key[2] == 'A']
    answer = 1
    for start in starts:
        current = start
        instr_index = 0
        while not current[2] == 'Z':
            instr = instructions[instr_index % len(instructions)]
            instr_index += 1
            left, right = nodes[current]
            if instr == "L":
                current = left
            else:
                current = right
        answer = math.lcm(answer, instr_index)
    return answer

if __name__ == "__main__":
    with open('./input/day08.txt') as f:
        instructions, nodes = f.read().split('\n\n')

    print('---- Part One ----') # 20569
    print(part_one(instructions, parse_nodes(nodes)))

    print('---- Part Two ----') # 21366921060721
    print(part_two(instructions, parse_nodes(nodes)))
