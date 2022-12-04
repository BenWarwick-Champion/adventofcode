# Advent of Code 2022
# Day 03

def appears_twice(rucksack):
    first_half = rucksack[:len(rucksack)//2]
    second_half = rucksack[len(rucksack)//2:]

    set_second = set(second_half)
    for char in first_half:
        if char in set_second:
            return calc_value(char)


def calc_value(char):
    if char.islower():
        return ord(char) - 96

    return ord(char) - 64 + 26


def common_item(rucksacks):
    total = 0
    sets = []
    for rucksack in rucksacks:
        sets.append(set(rucksack))

        if len(sets) == 3:
            difference = sets[0] & sets[1] & sets[2]
            difference.discard('\n')
            char = list(difference)[0]
            total += calc_value(char)
            sets.clear()

    return total


if __name__ == "__main__":
    with open("input/day03.txt") as f:
        rucksacks = f.readlines()
    print('---- Part One ----')
    print(sum([appears_twice(rs) for rs in rucksacks]))

    print('---- Part Two ----')
    print(common_item(rucksacks))
