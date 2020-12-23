# Advent of Code 2020
# Day 23: Crab Cups

def play_game(cups, moves):
    cup = cups[0]
    for _ in range(moves):
        cups, cup = play_round(cups, cup)
        if cups.index(cup) + 1 >= len(cups):
            cup = cups[0]
        else:
            cup = cups[cups.index(cup) + 1]
    return cups

def play_round(cups, cup):
    c_cup = cups.index(cup)
    r_cups = []
    for _ in range(3):
        if c_cup + 1 >= len(cups):
            c_cup = -1
        r_cups.append(cups.pop(c_cup+1))

    dest_cup = cup - 1
    while cups.count(dest_cup) == 0:
        if dest_cup < min(cups):
            dest_cup = max(cups)
        else:
            dest_cup -= 1

    d_cup = cups.index(dest_cup) + 1
    for r_cup in r_cups[::-1]:
        cups.insert(d_cup, r_cup)
    return cups, cup

def print_labels(cups):
    ind_1 = cups.index(1)
    str_cups = [str(num) for num in cups]
    first = "".join(str_cups[ind_1:])
    last = "".join(str_cups[:ind_1])
    print("Final labels: " + first[1:] + last)


if __name__ == "__main__":
    with open("Data/day23.txt", "r") as f:
        cups = [int(num) for num in list(f.readline().strip())]

    cups = play_game(cups, 100)
    print_labels(cups) # Part 1: 47382659
