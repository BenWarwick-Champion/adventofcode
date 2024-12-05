# Advent of Code 2023
# Day 05

from collections import defaultdict
from functools import cmp_to_key

def parse_input(raw_data):
    rules, updates = raw_data.split('\n\n')
    rules = [rule.split('|') for rule in rules.split('\n')]
    updates = [update.split(',') for update in updates.split('\n')]

    checks = defaultdict(list)
    for k, v in rules:
        checks[k].append(v)
    return rules, updates, checks

def find_middle(update):
    return int(update[len(update) // 2])

def find_valid_updates(updates, checks):
    valid_updates = []
    invalid_updates = []
    for update in updates:
        valid = True
        for i, item in enumerate(update):
            if i == 0:
                continue
            previous = update[i::-1]
            for num in previous:
                if num in checks[item]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates

def part_one(raw_data):
    rules, updates, checks = parse_input(raw_data)
    valid_updates, _ = find_valid_updates(updates, checks)    
    return sum([find_middle(update) for update in valid_updates])

def part_two(raw_data):
    rules, updates, checks = parse_input(raw_data)
    _, invalid_updates = find_valid_updates(updates, checks)


    def compare(a: str, b: str):
        # print('Comparing:', a, b)
        # print('a:', checks[a], 'b:', checks[b])
        if a in checks[b]:
            return 1
        if b in checks[a]:
            return -1
        return 0

    fixed_updates = []
    for update in invalid_updates:
        fixed = sorted(update, key=cmp_to_key(compare))
        # print('Update:', update, 'Fixed:', fixed)
        fixed_updates.append(fixed)

    return sum([find_middle(update) for update in fixed_updates])

if __name__ == "__main__":
    with open("input/day05.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 4609

    print('---- Part Two ----')
    print(part_two(raw_data)) # 5723
