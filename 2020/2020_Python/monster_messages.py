# Advent of Code 2020
# Day 19: Monster Messages

import re
from functools import lru_cache

def parse_input(data):
    r = {}
    m = [line for line in data if line != '' and line[0].isalpha()]
    for line in data:
        if line != '' and line[0].isnumeric():
            id, rule = line.split(': ')
            r.setdefault(int(id), rule)
    return r, m

@lru_cache(None)
def convert_to_re(rule):
    if '"' in rule:
        output = rule[1]
    elif '|' in rule:
        branch1, branch2 = rule.split(' | ')
        re1 = '(' + ')('.join([get_re(int(i)) for i in branch1.split()]) + ')'
        re2 = '(' + ')('.join([get_re(int(i)) for i in branch2.split()]) + ')'
        output = f"({re1})|({re2})"
    else:
        output = '(' + ')('.join([get_re(int(i)) for i in rule.split()]) + ')'
    return output

def get_re(rule_id):
    if rule_id == 8:
        return re_8
    elif rule_id == 11:
        return re_11

    if rule_id in regexes:
        return regexes[rule_id]
    regexes[rule_id] = convert_to_re(rules[rule_id])
    return regexes[rule_id]

if __name__ == "__main__":
    with open("Data/day19.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    rules, msgs = parse_input(data)
    regexes = {}

    # Uncomment for part 1
    # re_0 = get_re(0)
    # part1 = sum(1 for msg in msgs if re.fullmatch(re_0, msg))
    # print("Part 1 solution:", part1) # 190

    re_42 = get_re(42)
    re_8 = f"({re_42})+"

    re_31 = get_re(31)
    re_11 = '(' + '|'.join(f"({re_42}){{{n}}}({re_31}){{{n}}}" for n in range(1, 11)) + ')'

    re_0 = get_re(0)
    part2 = sum(1 for msg in msgs if re.fullmatch(re_0, msg))
    print("Part 2 solution:", part2) # 311
