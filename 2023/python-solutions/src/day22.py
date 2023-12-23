# Advent of Code 2023
# Day 22

from collections import defaultdict

def parse_bricks(raw_data):
    bricks = []
    for line in raw_data:
        a, b = line.split('~')
        a = list(map(int, a.split(',')))
        b = list(map(int, b.split(',')))
        a.extend(b)
        bricks.append(a)
    return bricks

def dropped_brick(tallest, brick):
    peak = max(tallest[(x, y)] for x in range(brick[0], brick[3] + 1) for y in range(brick[1], brick[4] + 1))
    dz = max(brick[2] - peak - 1, 0)
    return (brick[0], brick[1], brick[2] - dz, brick[3], brick[4], brick[5] - dz)

def drop(bricks):
    tallest = defaultdict(int)
    new_tower = []
    falls = 0
    for brick in bricks:
        new_brick = dropped_brick(tallest, brick)
        if new_brick[2] != brick[2]:
            falls += 1
        new_tower.append(new_brick)
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                tallest[(x, y)] = new_brick[5]
    return falls, new_tower

def part_one(raw_data):
    bricks = parse_bricks(raw_data)
    bricks = sorted(bricks, key=lambda brick: brick[2])
    _, fallen = drop(bricks)
    answer = 0
    for i in range(len(fallen)):
        removed = fallen[:i] + fallen[i + 1:]
        falls, _ = drop(removed)
        if not falls:
            answer += 1
    return answer

def part_two(raw_data):
    bricks = parse_bricks(raw_data)
    bricks = sorted(bricks, key=lambda brick: brick[2])
    _, fallen = drop(bricks)
    answer = 0
    for i in range(len(fallen)):
        removed = fallen[:i] + fallen[i + 1:]
        falls, _ = drop(removed)
        if falls:
            answer += falls
    return answer

if __name__ == "__main__":
    with open("input/day22.txt") as f:
        raw_data = [line.strip() for line in f.readlines()]
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))
