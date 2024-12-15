# Advent of Code 2023
# Day 14

from math import prod
from collections import Counter
import time

AREA_WIDTH = 101
AREA_HEIGHT = 103

# AREA_WIDTH = 11
# AREA_HEIGHT = 7

SECONDS = 100

def print_area(robots):
    area = [['.' for _ in range(AREA_WIDTH)] for _ in range(AREA_HEIGHT)]
    for p, _ in robots:
        x, y = int(p.real), int(p.imag)
        if area[x][y] == '.':
            area[x][y] = '#'
        # if area[x][y] == '.':
        #     area[x][y] = 1
        # else:
        #     area[x][y] += 1
    for row in area:
        print(''.join(str(cell) for cell in row))

def parse_data(raw_data):
    robots = []
    for line in raw_data:
        p, v = line.split(' ')
        p = list(map(int, p.split('=')[1].split(',')))
        v = list(map(int, v.split('=')[1].split(',')))
        p = complex(p[1], p[0])
        v = complex(v[1], v[0])
        robots.append((p, v))
    return robots

def move_robots(robots):
    next_robots = []
    for robot in robots:
        p, v = robot
        p += v
        x = int(p.real) % AREA_HEIGHT
        y = int(p.imag) % AREA_WIDTH
        p = complex(x, y)
        next_robots.append((p, v))
    return next_robots

def safety_factor(robots):
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        p, _ = robot
        if p.real < AREA_HEIGHT // 2 and p.imag < AREA_WIDTH // 2:
            quadrants[0] += 1
        elif p.real < AREA_HEIGHT // 2 and p.imag > AREA_WIDTH // 2:
            quadrants[1] += 1
        elif p.real > AREA_HEIGHT // 2 and p.imag < AREA_WIDTH // 2:
            quadrants[2] += 1
        elif p.real > AREA_HEIGHT // 2 and p.imag > AREA_WIDTH // 2:
            quadrants[3] += 1
    return prod(quadrants)

def part_one(raw_data):
    robots = parse_data(raw_data)
    print_area(robots)
    for _ in range(SECONDS):
        robots = move_robots(robots)
    print([p for p, _ in robots])
    print_area(robots)
    return safety_factor(robots)

def candidate(robots):
    line = []
    for i in range(39, 60):
        if complex(63, i) in robots:
            line.append(complex(63, 1))

    if len(line) > 18:
        return True
    return False
    start = complex(64,39)
    end = complex(64, 60)
    for robot in robots:
        p, v = robot
        counter[p.imag] += 1
    if any(v > 30 for v in counter.values()):
        return True
    return False


def part_two(raw_data):
    robots = parse_data(raw_data)
    # print_area(robots)
    for _ in range(10000):
        robots = move_robots(robots)

        # if _ < 5000:
        #     continue

        if candidate(robots):
            print('SECONDS:', _ + 1)
            print_area(robots)
            time.sleep(1)

    # print([p for p, _ in robots])
    # print_area(robots)
    return safety_factor(robots)

if __name__ == "__main__":
    with open("input/day14.txt") as f:
        raw_data = f.readlines()
    
    print('---- Part One ----')
    # print(part_one(raw_data)) # 218433348

    print('---- Part Two ----')
    print(part_two(raw_data)) 
