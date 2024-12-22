# Advent of Code 2023
# Day 22

from collections import defaultdict
from itertools import product

def mix(given, secret):
    return given ^ secret

def prune(n):
    return n % 16777216

def evolve(secret):
    given = secret * 64
    secret = mix(given, secret)
    secret = prune(secret)

    given = secret // 32
    secret = mix(given, secret)
    secret = prune(secret)

    given = secret * 2048
    secret = mix(given, secret)
    secret = prune(secret)

    return secret

def part_one(raw_data):
    total = 0
    for num in raw_data.split('\n'):
        secret = int(num)
        for _ in range(2000):
            secret = evolve(secret)
        total += secret
    return total

def part_two(raw_data):
    total = 0
    totals = {}
    for num in raw_data.split('\n'):
        seen = defaultdict(int)
        secret = int(num)
        differences = []
        for _ in range(2000):
            last_price = int(str(secret)[-1])
            secret = evolve(secret)
            price = int(str(secret)[-1])
            diff = price - last_price
            differences.append(diff)
            if len(differences) < 4:
                continue
            last_4 = tuple(differences[-4:])
            if last_4 not in seen:
                seen[last_4] = price
        totals[num] = seen

    best = {}
    for sequence in product(range(-9, 10), repeat=4):
        total = 0
        for num in raw_data.split('\n'):
            total += totals[num].get(sequence, 0)
        best[sequence] = total
    
    return max(best.values())

if __name__ == "__main__":
    with open("input/day22.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 16953639210

    print('---- Part Two ----')
    print(part_two(raw_data)) # 1863
