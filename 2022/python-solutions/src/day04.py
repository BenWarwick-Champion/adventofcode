# Advent of Code 2022
# Day 04

def is_fully_contained(pair):
    elf1, elf2 = pair.split(',')
    e1l, e1h = [int(num) for num in elf1.split('-')]
    e2l, e2h = [int(num) for num in elf2.split('-')]

    e1range = set(range(e1l, e1h + 1))
    e2range = set(range(e2l, e2h + 1))

    return (e1range.issubset(e2range) or e2range.issubset(e1range))


def is_overlapping(pair):
    elf1, elf2 = pair.split(',')
    e1l, e1h = [int(num) for num in elf1.split('-')]
    e2l, e2h = [int(num) for num in elf2.split('-')]

    e1range = set(range(e1l, e1h + 1))
    e2range = set(range(e2l, e2h + 1))

    return not e1range.isdisjoint(e2range)


if __name__ == "__main__":
    with open("input/day04.txt") as f:
        data = f.readlines()

    print('---- Part One ----')
    print(sum([is_fully_contained(pair) for pair in data]))

    print('---- Part Two ----')
    print(sum([is_overlapping(pair) for pair in data]))
