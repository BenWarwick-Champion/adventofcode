# Advent of Code 2022
# Day 23

from pprint import pprint


def find_neighbours(curr, elves):
    neighbours = set()
    for dx in [-1, 0, 1]:
        for dy in [-1j, 0, 1j]:
            neighbour = curr + dx + dy
            if neighbour == curr:
                continue
            elif neighbour in elves:
                neighbours.add(neighbour)
    return neighbours


def solve(curr_elves, round):
    elves = set()
    for elf in curr_elves:
        print(len(elves), elf)
        neighbours = find_neighbours(elf, curr_elves)
        if len(neighbours) == 0:
            elves.add(elf)
            continue

        # north
        north = any(elf-1+i in neighbours for i in [-1j, 0, 1j])
        if not north:
            elves.add(elf - 1)
            continue
        # south
        south = any(elf+1+i in neighbours for i in [-1j, 0, 1j])
        if not south:
            elves.add(elf + 1)
            continue
        # west
        west = any(elf-1j+i in neighbours for i in [-1, 0, 1])
        if not west:
            elves.add(elf - 1j)
            continue
        # east
        east = any(elf+1j+i in neighbours for i in [-1, 0, 1])
        if not east:
            elves.add(elf + 1j)
            continue

        elves.add(elf)
    return elves


def calc(elves):
    n, s, e, w = 0, 0, 0, 0
    for elf in elves:
        real = int(elf.real)
        imag = int(elf.imag)
        n = min(n, real)
        s = max(s, real)
        e = max(e, imag)
        w = min(w, imag)

    print(n, s, e, w)

    empty = 0
    for x in range(n, s + 1):
        for y in range(w, e + 1):
            if complex(x, y) not in elves:
                empty += 1

    return empty


if __name__ == "__main__":
    with open("input/_day23.txt") as f:
        data = f.readlines()

    elves = set()
    for x, l in enumerate(data):
        for y, c in enumerate(l):
            if c == '#':
                elves.add(complex(x, y))

    # elves = {(x+y*1j) for x, l in enumerate(data)
    #          for y, c in enumerate(l) if c == '#'}

    print('---- Part One ----')
    for _ in range(10):
        elves = solve(elves)
        print(len(elves))

    print(elves)
    print(calc(elves))

    print('---- Part Two ----')
    print()
