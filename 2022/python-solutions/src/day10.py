# Advent of Code 2022
# Day 10

from collections import deque, defaultdict
from pprint import pprint


def execute(instructions):
    queue = deque()

    for instr in instructions:
        match instr.split():
            case 'addx', val:
                queue.append(0)
                queue.append(int(val))
            case ['noop']:
                queue.append(0)

    x = 1
    clock = 0
    x_map = defaultdict()
    for val in queue:
        clock += 1
        x_map[clock] = x
        x += val

    return x_map


def draw_CRT(x_map):
    screen = []
    for clock in x_map:
        pos = clock % 40
        num = x_map[clock]
        sprite = [num, num+1, num+2]
        draw = False
        for val in sprite:
            if pos == val:
                draw = True

        if draw:
            screen.append('#')
        else:
            screen.append(' ')

    lines = []
    for i in range(6):
        line = screen[i*40: (i+1) * 40]
        lines.append(''.join(line) + '\n')

    return ''.join(lines)


if __name__ == "__main__":
    with open("input/day10.txt") as f:
        data = [line.strip() for line in f.readlines()]

    x_map = execute(data)
    print('---- Part One ----')
    pprint(sum([num * x_map[num]
           for num in range(20, len(x_map), 40)]))  # 17840

    print('---- Part Two ----')
    print(draw_CRT(x_map))  # EALGULPG
