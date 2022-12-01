# Advent of Code 2022
#  Day 01:

def find_max_calories(carry_list):
    elf = 0
    elves = {0: 0}
    for calories in carry_list:
        if (calories == ''):
            elf += 1
            elves[elf] = 0
            continue

        elves[elf] += int(calories)

    return max(elves.values())


def find_max_three_calories(carry_list):
    elf = 0
    elves = {0: 0}
    for calories in carry_list:
        if (calories == ''):
            elf += 1
            elves[elf] = 0
            continue

        elves[elf] += int(calories)

    calorie_list = [count for count in elves.values()]
    calorie_list.sort()
    return sum(calorie_list[-3:])


if __name__ == "__main__":
    with open('./input/day01.txt') as f:
        data = [line.strip() for line in f.readlines()]
        print('---- Part One ----')
        print(find_max_calories(data))

        print('---- Part Two ----')
        print(find_max_three_calories(data))
