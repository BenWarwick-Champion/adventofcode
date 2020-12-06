# Advent of Code 2020
# Day 6: Custom Customs

def check_group(group):
    questions = set()
    people = group.split()
    for person in people:
        for char in person:
            questions.add(char)
    questions.discard(' ')
    return len(questions)


def check_group_everyone(group):
    question_sets = []
    per_questions = set()
    people = group.split()
    for person in people:
        per_questions.clear()
        for char in person:
            per_questions.add(char)
        question_sets.append(per_questions.copy())

    questions = set.intersection(*question_sets)
    questions.discard(' ')
    return len(questions)


if __name__ == "__main__":
    with open("Data/day6.txt", "r") as f:
        input_data = f.readlines()

    lastline = ''
    groups = []
    for line in input_data:
        if line == '\n':
            groups.append(lastline)
            lastline = ''
        else:
            lastline = (lastline + line).replace('\n', ' ')
    groups.append(lastline)

    # Part 1 solution:
    sum_part1 = 0
    for group in groups:
        sum_part1 += check_group(group)
    print(f'The total sum is: {sum_part1}')

    # Part 2 solution:
    sum_part2 = 0
    for group in groups:
        sum_part2 += check_group_everyone(group)
    print(f'The total sum is: {sum_part2}')
