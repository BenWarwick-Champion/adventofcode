import string
from pprint import pprint
from collections import defaultdict
from functools import cmp_to_key
import math

def predict(sequence: list[int]):
    if sequence.count(0) == len(sequence):
        return 0
    diffs = []
    for ind in range(len(sequence) - 1):
        diffs.append(sequence[ind + 1] - sequence[ind])
    return sequence[-1] + predict(diffs)

def part_one(raw_data: list[str]):
    output = []
    for ind, line in enumerate(raw_data):
        sequence = [int(num) for num in line.strip().split()]
        output.append(predict(sequence))
    return sum(output)


def part_two(raw_data: list[str]):
    output = []
    for ind, line in enumerate(raw_data):
        sequence = [int(num) for num in line.strip().split()[::-1]]
        output.append(predict(sequence))
    return sum(output)

if __name__ == "__main__":
    with open('./input/day09.txt') as f:
        raw_data = f.readlines()

    print('---- Part One ----') #
    print(part_one(raw_data))

    print('---- Part Two ----') #
    print(part_two(raw_data))
