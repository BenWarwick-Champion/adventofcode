# Advent of Code 2022
# Day 21

from pprint import pprint


def calculate_p1(lines):
    monkeys = {}
    for line in lines:
        key, value = line.strip().split(': ')
        monkeys[key] = value
    return int(calc(monkeys, 'root'))


def calculate_p2(lines):
    monkeys = {}
    for line in lines:
        key, value = line.strip().split(': ')
        monkeys[key] = value

    left, _, right = monkeys['root'].split()
    i = 3373767893000
    equal = False

    # monkeys['humn'] = f'{i}'
    # print(i, int(calc(monkeys, left)) > int(calc(monkeys, right)))
    # return int(calc(monkeys, left)), int(calc(monkeys, right))

    while not equal:
        i += 1
        monkeys['humn'] = f'{i}'
        if i % 1000 == 0:
            print(int(calc(monkeys, left)), int(calc(monkeys, right)))
        equal = int(calc(monkeys, left)) == int(calc(monkeys, right))

    return i


def calc(monkeys, monkey):
    if monkeys[monkey].isdecimal():
        return int(monkeys[monkey])

    match monkeys[monkey].split():
        case x, '+', y:
            return calc(monkeys, x) + calc(monkeys, y)
        case x, '-', y:
            return calc(monkeys, x) - calc(monkeys, y)
        case x, '*', y:
            return calc(monkeys, x) * calc(monkeys, y)
        case x, '/', y:
            return calc(monkeys, x) / calc(monkeys, y)
        case _:
            print('Balls')


if __name__ == "__main__":
    with open("input/day21.txt") as f:
        data = f.readlines()

    print('---- Part One ----')
    pprint(calculate_p1(data))

    print('---- Part Two ----')
    pprint(calculate_p2(data))
