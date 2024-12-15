# Advent of Code 2023
# Day 15

def get_start_pos(grid):
    for pos in grid:
        if grid[pos] == '@':
            return pos

def parse_data(raw_data):
    area, moves = raw_data.split('\n\n')
    area = area.split('\n')
    moves = ''.join(moves.split())
    grid = dict()
    wide_grid = dict()
    wide_area = []
    for r, row in enumerate(area):
        wide_row = []
        for c, char in enumerate(list(row)):
            grid[complex(r, c)] = char            

            if char in ['#', '.']:
                wide_row.append(char)
                wide_row.append(char)
            if char == 'O':
                wide_row.append('[')
                wide_row.append(']')
            if char == '@':
                wide_row.append('@')
                wide_row.append('.')
        wide_area.append(''.join(wide_row))

    for r, row in enumerate(wide_area):
        for c, char in enumerate(list(row)):
            wide_grid[complex(r, c)] = char

    return grid, wide_grid, moves

def move_to_dir(move):
    if move == '^':
        return complex(-1, 0)
    if move == 'v':
        return complex(1, 0)
    if move == '<':
        return complex(0, -1)
    if move == '>':
        return complex(0, 1)
    return

def move(grid, m, pos):
    curr_pos = pos
    while True:
        next_pos = curr_pos + move_to_dir(m)
        if grid.get(next_pos) == '#':
            curr_pos = pos
            break
        if grid.get(next_pos) == '.':
            if grid[curr_pos] == 'O':
                grid[next_pos] = 'O'
                grid[pos] = '.'
                curr_pos = pos + move_to_dir(m)
                grid[curr_pos] = '@'
            else:
                grid[next_pos] = grid[pos]
                grid[pos] = '.'
                curr_pos = next_pos
            break
        curr_pos = next_pos
    return curr_pos, grid

def find_candidates(candidates, grid, m, pos):
    candidates[pos] = grid[pos]
    if grid[pos] == '[' and pos + 1j not in candidates:
        find_candidates(candidates, grid, m, pos + 1j)
    if grid[pos] == ']' and pos - 1j not in candidates:
        find_candidates(candidates, grid, m, pos - 1j)
    if grid[pos + move_to_dir(m)] in '[]' and pos + move_to_dir(m) not in candidates:
        find_candidates(candidates, grid, m, pos + move_to_dir(m))

def score(grid):
    return sum([int(pos.real)*100 + int(pos.imag) for pos in grid if grid[pos] in 'O['])

def print_grid(grid):
    n_rows, n_cols = 0, 0
    for pos in grid:
        n_rows = max(n_rows, int(pos.real))
        n_cols = max(n_cols, int(pos.imag))

    for r in range(n_rows + 1):
        row = []
        for c in range(n_cols + 1):
            row.append(grid.get(complex(r, c)))
        print(''.join(row))

def part_one(raw_data):
    grid, _, moves = parse_data(raw_data)
    pos = get_start_pos(grid)
    for m in moves:
        pos, grid = move(grid, m, pos)
        # print_grid(grid)
    return score(grid)

def part_two(raw_data):
    _, wide_grid, moves = parse_data(raw_data)
    print_grid(wide_grid)
    pos = get_start_pos(wide_grid)
    for m in moves:
        candidates = {}
        find_candidates(candidates, wide_grid, m, pos)
        # print('Candidates:', candidates)
        if all(wide_grid[p + move_to_dir(m)] != '#' for p in candidates):
            wide_grid.update({p: '.' for p in candidates})
            wide_grid.update({p + move_to_dir(m): c for p, c in candidates.items()})
            pos = pos + move_to_dir(m)
        # print_grid(wide_grid)
    return score(wide_grid)

if __name__ == "__main__":
    with open("input/day15.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))
