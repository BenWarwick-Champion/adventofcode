# Advent of Code 2022
# Day 18

def count_sides(cubes, part=1):
    side_count = 0
    for cube in cubes:
        for side in sides(*cube):
            if side not in cubes:
                side_count += 1

    if part == 1:
        return side_count

    seen = set()
    todo = [(-1, -1, -1)]

    while todo:
        here = todo.pop()
        todo += [s for s in (sides(*here) - cubes - seen)
                 if all(-1 <= c <= 25 for c in s)]
        seen |= {here}

    return sum((s in seen) for c in cubes for s in sides(*c))


def sides(x, y, z):
    return {
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1)
    }


if __name__ == "__main__":
    with open("input/day18.txt") as f:
        data = [tuple([int(n) for n in line.strip().split(',')])
                for line in f.readlines()]

    print('---- Part One ----')
    cubes = set(data)
    print(count_sides(cubes))

    print('---- Part Two ----')
    print(count_sides(cubes, 2))
