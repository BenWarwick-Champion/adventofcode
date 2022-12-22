# Advent of Code 2022
# Day 22

from re import findall


def parse(data):
    field, instr = data.split('\n\n')
    nums = [int(n) for n in findall(r'\d+', instr)]
    turns = findall(r'[A-Z]+', instr)

    lines = field.split('\n')
    pos = lines[0].index('.') * 1j

    grid = {(x+y*1j): c for x, l in enumerate(lines)
            for y, c in enumerate(l) if c in '.#'}
    return grid, zip(nums, turns), pos


def wrap(pos, direction):
    x, y = pos.real, pos.imag
    match direction, x//50, y//50:
        case  1j, 0, _: return complex(149-x, 99), -1j
        case  1j, 1, _: return complex(49, x + 50), -1
        case  1j, 2, _: return complex(149-x, 149), -1j
        case  1j, 3, _: return complex(149, x-100), -1
        case -1j, 0, _: return complex(149-x,  0),  1j
        case -1j, 1, _: return complex(100, x - 50),  1
        case -1j, 2, _: return complex(149-x, 50),  1j
        case -1j, 3, _: return complex(0, x-100),  1
        case  1, _, 0: return complex(0, y+100),  1
        case  1, _, 1: return complex(100+y, 49), -1j
        case  1, _, 2: return complex(-50+y, 99), -1j
        case -1, _, 0: return complex(50+y, 50),  1j
        case -1, _, 1: return complex(100+y,  0),  1j
        case -1, _, 2: return complex(199, y-100), -1


def solve(data):
    grid, instr, pos = parse(data)
    direction = 1j

    for num, turn in instr:

        for _ in range(num):
            p, d = pos + direction, direction

            if p not in grid:
                p, d = wrap(p, d)

            if grid[p] == '.':
                pos, direction = p, d

        if turn == 'L':
            direction *= +1j
        elif turn == 'R':
            direction *= -1j

    return pos, direction


def calc(pos, direction):
    return 1000 * (pos.real+1) + 4 * (pos.imag+1) + [1j, 1, -1j, -1].index(direction)


if __name__ == "__main__":
    with open("input/day22.txt") as f:
        data = f.read()

    print('---- Part One ----')
    # print(calc(solve(data)))

    print('---- Part Two ----')
    print(calc(*solve(data)))
