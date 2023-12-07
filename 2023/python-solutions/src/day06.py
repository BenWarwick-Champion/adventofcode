import string
from pprint import pprint
from collections import defaultdict

def parse(raw_data: list[str]):
    times = [int(num) for num in raw_data[0].split(':')[1].strip().split()]
    distances = [int(num) for num in raw_data[1].split(':')[1].strip().split()]
    return times, distances

def calc_distance(hold_time: int, total_time: int):
    velocity = hold_time
    distance = (total_time - hold_time) * velocity
    return distance

def part_one(raw_data: list[str]):
    times, distances = parse(raw_data)
    total = 1
    for time, distance in zip(times, distances):
        beat_record = []
        for i in range(time):
            if calc_distance(i, time) > distance:
                beat_record.append(i)
        total *= len(beat_record)
    return total

def part_two(raw_data: list[str]):
    time = int(''.join(raw_data[0].split(':')[1].strip().split()))
    distance = int(''.join(raw_data[1].split(':')[1].strip().split())) 
    ways = 0
    for i in range(time):
        if calc_distance(i, time) > distance:
            ways += 1
    return ways

if __name__ == "__main__":
    with open('./input/day06.txt') as f:
        raw_data = f.read().split('\n')

    print('---- Part One ----') # 160816
    print(part_one(raw_data))

    print('---- Part Two ----') # 
    print(part_two(raw_data))

