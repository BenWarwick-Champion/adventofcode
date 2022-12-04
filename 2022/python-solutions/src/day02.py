# Advent of Code 2022
# Day 02:

def calc_win(a, b):
    value = {
        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3,
    }
    return value[a + b]


def calc_round(round):
    a, b = round.split()
    value = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    return value[b] + calc_win(a, b)


def calc_round2(round):
    a, b = round.split()
    value = {
        'AX': 0 + 3,
        'AY': 3 + 1,
        'AZ': 6 + 2,
        'BX': 0 + 1,
        'BY': 3 + 2,
        'BZ': 6 + 3,
        'CX': 0 + 2,
        'CY': 3 + 3,
        'CZ': 6 + 1,
    }
    return value[a + b]


if __name__ == "__main__":
    with open('./input/day02.txt') as f:
        data = f.readlines()

    print('---- Part One ----')
    print(sum([calc_round(round) for round in data]))

    print('---- Part Two ----')
    print(sum(calc_round2(round) for round in data))
