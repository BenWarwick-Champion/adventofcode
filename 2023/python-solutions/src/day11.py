import itertools


def get_distance(pair: tuple[complex, complex], empty_rows: list[int], empty_cols: list[int], part1=True):
    a = int(pair[0].real)
    b = int(pair[0].imag)
    c = int(pair[1].real)
    d = int(pair[1].imag)
    distance = abs(a-c) + abs(b-d)

    for row in empty_rows:
        if (a > row and row > c) or (c > row and row > a):
            distance += 1 if part1 else 999_999
    
    for col in empty_cols:
        if (b > col and col > d) or (d > col and col > b):
            distance += 1 if part1 else 999_999
    return distance

def part_one(raw_data: list[list[str]]):
    galaxies = []
    empty_rows = []
    empty_cols = [c for c in range(len(raw_data[0]))]
    for r, row in enumerate(raw_data):
        if row.count('.') == len(row):
            empty_rows.append(r)
        for c, char in enumerate(row):
            if char == '#':
                if c in empty_cols:
                    empty_cols.remove(c)
                galaxies.append(complex(r, c))
    pairs = list(itertools.combinations(galaxies, 2))
    distances = []
    for pair in pairs:
        distances.append(get_distance(pair, empty_rows, empty_cols))

    return sum(distances)

def part_two(raw_data: list[list[str]]):
    galaxies = []
    empty_rows = []
    empty_cols = [c for c in range(len(raw_data[0]))]
    for r, row in enumerate(raw_data):
        if row.count('.') == len(row):
            empty_rows.append(r)
        for c, char in enumerate(row):
            if char == '#':
                if c in empty_cols:
                    empty_cols.remove(c)
                galaxies.append(complex(r, c))
    pairs = list(itertools.combinations(galaxies, 2))
    distances = []
    for pair in pairs:
        distances.append(get_distance(pair, empty_rows, empty_cols, part1=False))

    return sum(distances)

if __name__ == "__main__":
    with open('./input/day11.txt') as f:
        raw_data = [list(line.strip()) for line in f.readlines()]

    print('---- Part One ----') # 9684228
    print(part_one(raw_data))

    print('---- Part Two ----') # 483844716556
    print(part_two(raw_data))

