# Advent of Code 2023
# Day 11

from collections import deque, Counter

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

def blink(stone):
    if stone == 0:
        return 1
    if len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        return [int(str(stone)[:half]), int(str(stone)[half:])]
    return stone * 2024

def part_one(raw_data):
    line = deque(int(stone) for stone in raw_data.split())
    for _ in range(25):
        new_line = deque()
        while line:
            stone = line.popleft()
            new_stones = blink(stone)
            if isinstance(new_stones, list):
                new_line.extend(new_stones)
            else:
                new_line.append(new_stones)
        line = new_line
    return len(line)

def blink_p2(stone_count):
    new_stone_count = Counter()
    for stone in stone_count:
        new_stones = blink(stone)

        increment = max(stone_count[stone], 1)

        if isinstance(new_stones, list):
            new_stone_count[new_stones[0]] += increment
            new_stone_count[new_stones[1]] += increment
        else:
            new_stone_count[new_stones] += increment
    return new_stone_count


def part_two(raw_data):
    line = [int(stone) for stone in raw_data.split()]
    stone_count = Counter(line)
    for _ in range(75):
        stone_count = blink_p2(stone_count)
    return sum(stone_count.values())

if __name__ == "__main__":
    with open("input/day11.txt") as f:
        raw_data = f.read().strip()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 188902

    print('---- Part Two ----')
    print(part_two(raw_data))
