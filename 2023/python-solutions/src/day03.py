import string
from pprint import pprint


def part_number_from_row(row: list[str]):
    part_numbers = []
    curr_num = []
    for ind, char in enumerate(row):
        if char.isdigit():
            curr_num.append(char)
            if ind == len(row) - 1:
                part_numbers.append(int(''.join(curr_num)))
                curr_num = [] 
        elif len(curr_num) > 0:
            part_numbers.append(int(''.join(curr_num)))
            curr_num = []
        else:
            continue
    return part_numbers

def part_one(schematic: list[list[str]]):
    valid_numbers = []
    for r, row in enumerate(schematic):
        numbers = part_number_from_row(row)
        if len(numbers) == 0:
            continue
        numbers_seen = 0
        number_seen_last = False
        numbers_added = set()
        for c, char in enumerate(row):
            if char.isdigit():
                if number_seen_last == False:
                    numbers_seen += 1
                number_seen_last = True
                for dr in [-1, 0, 1]:
                    if r + dr < 0 or r + dr >= len(schematic):
                        continue
                    for dc in [-1, 0, 1]:
                        if c + dc < 0 or c + dc >= len(schematic[0]):
                            continue
                        if schematic[r+dr][c+dc].isdigit() or schematic[r+dr][c+dc] == '.':
                            continue
                        # char is symbol
                        if numbers_seen not in numbers_added:
                            numbers_added.add(numbers_seen)
                            valid_numbers.append(numbers[numbers_seen-1])
            else:
                number_seen_last = False
    return sum(valid_numbers)

def part_number_and_coords(schematic: list[list[str]]):
    part_numbers = {}
    for r, row in enumerate(schematic):
        curr_num = []
        for ind, char in enumerate(row):
            if char.isdigit():
                curr_num.append(char)
                if ind == len(row) - 1:
                    for d in range(len(curr_num)):
                        part_numbers[(r, ind - 1 - d)] = int(''.join(curr_num))
                    curr_num = [] 
            elif len(curr_num) > 0:
                for d in range(len(curr_num)):
                    part_numbers[(r, ind - 1 - d)] = int(''.join(curr_num))
                curr_num = []
            else:
                continue
    return part_numbers

def part_two(schematic: list[list[str]]):
    valid_gear_ratios = []
    potential_gears: list[tuple[int, int]] = []
    for r, row in enumerate(schematic):
        for c, char in enumerate(row):
            if char == '*':
                potential_gears.append((r, c))

    part_numbers = part_number_and_coords(schematic)

    for gear in potential_gears:
        r, c = gear
        parts = set()
        for dr in [-1, 0, 1]:
            if r + dr < 0 or r + dr >= len(schematic):
                continue
            for dc in [-1, 0, 1]:
                if c + dc < 0 or c + dc >= len(schematic[0]):
                    continue
                if schematic[r+dr][c+dc].isdigit():
                    coord = r+dr, c+dc
                    parts.add(part_numbers[coord])
        if len(parts) == 2:
            gear1 = parts.pop()
            gear2 = parts.pop()
            valid_gear_ratios.append(gear1 * gear2)

    return sum(valid_gear_ratios)


if __name__ == "__main__":
    with open('./input/day03.txt') as f:
        raw_data = [list(line.strip()) for line in f.readlines()]

    print('---- Part One ----') # 540131
    print(part_one(raw_data))

    print('---- Part Two ----') # 86879020
    print(part_two(raw_data))

