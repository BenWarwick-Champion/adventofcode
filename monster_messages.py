# Advent of Code 2020
# Day 19: Monster Messages

if __name__ == "__main__":
    with open("Data/day19.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    rules = {}
    for line in data:
        if line != '' and line[0].isnumeric():
            a, b = line.split(': ')
            rules.setdefault(a, b)

    msgs = [line for line in data if line != '' and line[0].isalpha()]


    print(rules, msgs)