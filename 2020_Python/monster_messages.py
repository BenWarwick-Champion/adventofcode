# Advent of Code 2020
# Day 19: Monster Messages

import re
from functools import lru_cache

def parse_input(data):
    r = {}
    m = [line for line in data if line != '' and line[0].isalpha()]
    r = [r.setdefault(*line.split(': ')) for line in data if line != '' and line[0].isnumeric()]
    return r, m

@lru_cache(None)
def convert_to_re(rule):
    if '"' in rule:
        output = rule[1]
        print(output)
    elif '|' in rule:
        branch1, branch2 = rule.split(' | ')
        a = branch1.split()
        b = branch2.split()
        print(a, b)
        re1 = "(" + ")(".join([get_re(int(i)) for i in a]) + ")"
        re2 = "(" + ")(".join([get_re(int(i)) for i in b]) + ")"
        output = f"({re1}|{re2})"
    else:
        c = [int(i) for i in rule.split()]
        print(c)
        output = "(" + ")(".join([get_re(int(i)) for i in c]) + ")"
    return output

def get_re(rule_id):
    if rule_id in regexes:
        return regexes[rule_id]
    
    ans = convert_to_re(rules[rule_id])
    regexes[rule_id] = ans
    return ans

if __name__ == "__main__":
    with open("Data/day19.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    rules, msgs = parse_input(data)
    regexes = {}
    re_0 = get_re(0)

    part1 = sum(1 for msg in msgs if re.fullmatch(re_0, msg))
    
    print(rules, msgs)