# Advent of Code 2020
# Day 23: Crab Cups

from collections import deque

def play_game(cups, moves):
    for _ in range(moves):
        cup = cups.popleft()
        cups = play_round(cups, cup)
    return cups

def play_round(cups, cup):
    r_cups = []
    for _ in range(3):
        r_cups.append(cups.popleft())
    cups.append(cup)

    dest_cup = cup - 1
    while cups.count(dest_cup) == 0:
        if dest_cup < min(cups):
            dest_cup = max(cups)
        else:
            dest_cup -= 1

    d_cup = cups.index(dest_cup) + 1
    for r_cup in r_cups[::-1]:
        cups.insert(d_cup, r_cup)
    return cups

def print_labels(cups):
    ind_1 = cups.index(1)
    str_cups = [str(num) for num in cups]
    first = "".join(str_cups[ind_1:])
    last = "".join(str_cups[:ind_1])
    print("Final labels: " + first[1:] + last)


def init_cups(part2=False):
    with open("Data/day23.txt", "r") as f:
        cups = [int(num) for num in list(f.readline().strip())]
    if part2:
        cups.extend(range(max(cups)+1, 1000000))
    return deque(cups)

if __name__ == "__main__":
    p1_cups = init_cups()
    p1_cups = play_game(p1_cups, 100)
    print_labels(p1_cups) # Part 1: 47382659

    p2_cups = init_cups(part2=True)
    p2_cups = play_game(p2_cups, 10000000)
    print_labels(p2_cups)
