# Advent of Code 2020
# Day 19: Monster Messages

def parse_input(data):
    r = {}
    m = [line for line in data if line != '' and line[0].isalpha()]
    for line in data:
        if line != '' and line[0].isnumeric():
            a, b = line.split(': ')
            if b == '"a"' or b == '"b"':
                r.setdefault(a, b[1])
            elif '|' in b:
                r.setdefault(a, [x.split() for x in b.split('|')])
            else:
                r.setdefault(a, b.split())
    return r, m

def create_match_strings(rule, rules):
    match_strings = []
    match_string = ''
    for i in rules[rule]:
        match_strings.append(expand_rule(i, rules, match_string))
    return match_strings

def expand_rule(rule, rules, match_string):
    if rules[rule] == 'a' or rules[rule] == 'b':
        match_string += rules[rule]
        return match_string
    else:
        for i in rules[rule]:
            match_string += expand_rule(i, rules, match_string)
        return match_string

if __name__ == "__main__":
    with open("Test/day19.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    rules, msgs = parse_input(data)

    m_strs = create_match_strings('0', rules)

    print(rules, msgs)