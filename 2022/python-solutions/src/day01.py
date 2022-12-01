# Advent of Code 2022
#  Day 01:

def count_calories(elves):
    calorie_list = []
    for elf in elves:
        calories = sum([int(c) for c in elf.split('\n')])
        calorie_list.append(calories)
    return sorted(calorie_list)


def count_calories_concisely(elves):
    return sorted([sum([int(c) for c in elf.split('\n')]) for elf in elves])


if __name__ == "__main__":
    with open('./input/day01.txt') as f:
        new_data = f.read().split('\n\n')

    print('---- Part One ----')
    print(count_calories(new_data)[-1])  # 67658

    print('---- Part Two ----')
    print(sum(count_calories(new_data)[-3:]))  # 200158
