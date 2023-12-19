# Advent of Code 2023
# Day 16

from pprint import pprint

def parse(raw_data: list[str]):
    grid = {}
    for r, row in enumerate(raw_data):
        for c, char in enumerate(row.strip()):
            grid[complex(r, c)] = char
    return grid

def count(grid: dict[complex, str], pos: complex, dir: complex):
    todo = set([(pos, dir)])
    done = set()
    while todo:
        p, d = todo.pop()
        while not (p, d) in done:
            done.add((p, d))
            p += d
            match grid.get(p):
                case '-': 
                    if d == 1 or d == -1:
                        d = 1j
                        todo.add((p, -d))
                case '|':
                    if d == 1j or d == -1j:
                        d = 1
                        todo.add((p, -d))
                case '/': 
                    d = -complex(d.imag, d.real)
                case '\\':
                    d = complex(d.imag, d.real)
                case None:
                    break

    return len(set(x for x, _ in done)) - 1

def part_one(raw_data):
    grid = parse(raw_data)
    return count(grid, -1j, 1j)

def part_two(raw_data):
    grid = parse(raw_data)
    counts = []
    for _dir in [1, -1, 1j, -1j]:
        for pos in grid:
            if pos - _dir not in grid:
                counts.append(count(grid, pos - _dir, _dir))
    return max(counts)

if __name__ == "__main__":
    with open("input/day16.txt") as f:
        raw_data = f.readlines()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 8112

    print('---- Part Two ----')
    pprint(part_two(raw_data)) # 8314
