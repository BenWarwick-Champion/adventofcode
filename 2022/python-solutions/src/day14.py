# Advent of Code 2022
# Day 14

from collections import defaultdict


def sign(num):
    return (num > 0) - (num < 0)


def print_map(rocks):
    for y in range(11):
        line = []
        for x in range(490, 505):
            line.append(' ' if rocks[complex(x, y)] == 0 else '#')
        print(''.join(line))


def draw_rocks(rock_paths):
    abyss = 0
    rocks = defaultdict(int)
    for path in rock_paths:
        last_coord = path[0]
        for coord in path:
            x, y = coord
            lx, ly = last_coord
            dx, dy = x - lx, y - ly
            sx, sy = sign(dx), sign(dy)
            last_coord = coord
            abyss = max(abyss, y + 1)
            # print(f'dx {dx} and dy {dy}')

            if dx == 0:
                for i in range(abs(dy) + 1):
                    rocks[complex(lx, ly + (i * sy))] = 1
            else:
                for i in range(abs(dx) + 1):
                    rocks[complex(lx + (i * sx), ly)] = 1
    print_map(rocks)
    return rocks, abyss


def pour_sand(rocks, abyss, part=1):
    rocks_set = set(key for key in rocks if rocks[key] != 0)
    grains = 0
    while True:
        sand = complex(500, 0)
        while True:
            if part == 2 and sand in rocks_set:
                return grains
            if sand.imag >= abyss:
                if part == 1:
                    return grains
                else:
                    rocks_set.add(sand)
                    break
            if (sand + 1j) not in rocks_set:
                sand += 1j
                continue
            if (sand + 1j - 1) not in rocks_set:
                sand += 1j - 1
                continue
            if (sand + 1j + 1) not in rocks_set:
                sand += 1j + 1
                continue
            rocks_set.add(sand)
            grains += 1
            break


if __name__ == "__main__":
    with open("input/day14.txt") as f:
        data = [[[int(num) for num in coord.split(',')]
                 for coord in line.split(' -> ')] for line in f.readlines()]

    rocks, abyss = draw_rocks(data)
    print('---- Part One ----')
    print(pour_sand(rocks, abyss))

    print('---- Part Two ----')
    print(pour_sand(rocks, abyss + 1, 2))
