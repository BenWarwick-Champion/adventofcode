# Advent of Code 2022
# Day 21

from pprint import pprint


def calculate_p1(lines):
    monkeys = {}
    for line in lines:
        key, value = line.strip().split(': ')
        monkeys[key] = value
    return int(calc(monkeys, 'root'))


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
    print()
