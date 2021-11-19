# Advent of Code 2020
# Day 7: Handy Haversacks

# Data format:
# [colour] bags contain [num] [colour] bag(s), [num] [colour] bag(s).

def is_shiny(bag, test_colour):
    if test_colour in rules[colours.index(bag)]:
        return True
    return False

def calc_bags(bag):
    if not d_bag.get(bag):
        return 1
    bag_number = sum([int(item[0])*calc_bags(item[1]) for item in d_bag.get(bag)]) + 1
    return int(bag_number)

if __name__ == "__main__":
    with open("Data/day7.txt", "r") as f:
        input_data = [line.strip('\n') for line in f.readlines()]
    colours, rules = map(list, zip(*[line.split(' bags contain ') for line in input_data]))
    
    # Part 1
    shiny_bags = []
    uniques = set()
    for colour in colours:
        if is_shiny(colour, 'shiny gold'):
            shiny_bags.append(colour)
            uniques.add(colour)

    while shiny_bags:
        test_colour = shiny_bags.pop()
        for colour in colours:
            if is_shiny(colour, test_colour):
                shiny_bags.append(colour)
                uniques.add(colour)

    print("The number of bags that can contain a shiny gold bag:", len(uniques)) # 211 is correct

    # Part 2 
    rule_list = [rule.split() for rule in rules]
    rule_d = []
    for line in rule_list:
        d_list = []
        for ind, word in enumerate(line):
            if word.isnumeric():
                d_item = (int(word), (' '.join(line[ind+1 : ind+3])))
                d_list.append(d_item)
        rule_d.append(d_list)
    d_bag = dict(zip(colours, rule_d))

    # Now we have a dictionary of all the colours
    # light red bags contain 1 bright white bag, 2 muted yellow bags.
    # 'light red' : [(1, 'bright white'), (2, 'muted yellow')]

    # This should result in 126 for test2 data
    print("The number of bags in a shiny gold bag:", calc_bags('shiny gold')-1) # 12414 is correct
