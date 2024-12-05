# Advent of Code 2023
# Day 04

from pprint import pprint

def parse_input(raw_data):
    grid = dict()
    for r, row in enumerate(raw_data.split('\n')):
        for c, col in enumerate(list(row)):
            grid[complex(r, c)] = col
    return grid

def search_xmas(grid, pos):
    xmas_found = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            direction = complex(i, j)
            xmas_len = 3
            found = []
            search_pos = pos
            for _ in range(xmas_len):
                search_pos += direction
                found.append(grid.get(search_pos, '.'))

            # print('Found:', found)
            xmas = 'X' + ''.join(found)

            if xmas == 'XMAS':
                xmas_found += 1
    return xmas_found

def search_x_mas(grid, pos):
    xmas_found = 0
    mas_list = []
    for i in [-1, 1]:
        direction = complex(1, i)
        found = []
        search_pos = pos
        # print('Searching:', pos, 'Direction:', direction)
        for diff in [-1, 0 ,1]:
            search_pos = pos + (direction * diff)
            found.append(grid.get(search_pos, '.'))

        # print('Found:', found)
        mas = ''.join(found)
        if mas in ['MAS', 'SAM']:
            mas_list.append(mas)

    if len(mas_list) == 2:
        xmas_found += 1
    return xmas_found

def part_one(raw_data):
    grid = parse_input(raw_data)
    total = 0
    for pos, val in grid.items():
        if val == 'X':
            xmas_found = search_xmas(grid, pos)
            # print('XMAS found:', xmas_found, 'at:', pos)
            total += xmas_found
    return total

def part_two(raw_data):
    grid = parse_input(raw_data)
    total = 0
    for pos, val in grid.items():
        if val == 'A':
            xmas_found = search_x_mas(grid, pos)
            # print('XMAS found:', xmas_found, 'at:', pos)
            total += xmas_found
    return total

if __name__ == "__main__":
    with open("input/day04.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    pprint(part_one(raw_data)) # 2583

    print('---- Part Two ----')
    print(part_two(raw_data)) # 1978
