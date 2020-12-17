# Advent of Code 2020
# Day 17: Conway Cubes

import copy

def add_padding(init, cycles = 6):
    new = []
    pad = '.' * (cycles)
    for row in init:
        new.append(pad + row + pad)
    
    row_pad = '.' * len(new[0])
    for _ in range(cycles):
        new.insert(0, row_pad)
        new.append(row_pad)

    padded = [new]
    z_pad = [row_pad] * len(new)
    for _ in range(cycles):
        padded.insert(0, z_pad)
        padded.append(z_pad)

    return padded

def count_occupied(s, r, c, cube):
    occupied = 0
    for ds in [-1, 0, 1]:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if ds == 0 and dr == 0 and dc == 0:
                    continue
                i_s = s + ds
                i_r = r + dr
                i_c = c + dc
                if (0 <= i_s < len(cube) 
                and 0 <= i_r < len(cube[0]) 
                and 0 <= i_c < len(cube[0][0]) 
                and cube[i_s][i_r][i_c] == '#'):
                    occupied += 1
    return occupied

if __name__ == "__main__":
    with open("Data/day17.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    cycles = 6
    padded_data = add_padding(data, cycles)
    cube = [[list(row) for row in s] for s in padded_data]

    next_cube = copy.deepcopy(cube)
    for _ in range(cycles):
        last_cube = copy.deepcopy(next_cube)
        for s in range(len(cube)):
            for r in range(len(cube[0])):
                for c in range(len(cube[0][0])):
                    if last_cube[s][r][c] == '#' and not (count_occupied(s, r, c, last_cube) == 2 or count_occupied(s, r, c, last_cube) == 3):
                        next_cube[s][r][c] = '.'
                    if last_cube[s][r][c] == '.' and count_occupied(s, r, c, last_cube) == 3:
                        next_cube[s][r][c] = '#'

    active = 0
    for s in next_cube:
        for r in s:
            active += r.count('#')

    print("Part 1 solution is:", active) # 324
