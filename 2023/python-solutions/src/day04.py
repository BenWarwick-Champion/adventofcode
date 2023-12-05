import string
from pprint import pprint
from collections import defaultdict

def parse_line(line: str):
    winning_numbers, my_numbers = line.split(':')[1].split('|')
    winning_numbers = [int(num) for num in winning_numbers.strip().split()]
    my_numbers = [int(num) for num in my_numbers.strip().split()]
    return winning_numbers, my_numbers

def part_one(lines: list[str]):
    scores: dict[int, int] = {}
    for card_index, line in enumerate(lines):
        winning_numbers, my_numbers = parse_line(line)
        winning = set(winning_numbers)
        for num in my_numbers:
            if num in winning:
                card_score = scores.get(card_index, 0)
                if card_score > 0:
                    scores[card_index] = 2 * card_score
                else:
                    scores[card_index] = 1
    return sum(scores.values())

def part_two(lines: list[str]):
    win_map: dict[int, int] = defaultdict(int)
    for card_index, line in enumerate(lines):
        wins = 0
        winning_numbers, my_numbers = parse_line(line)
        winning = set(winning_numbers)
        for num in my_numbers:
            if num in winning:
                wins += 1
        win_map[card_index] = wins

    cards = defaultdict(int)
    for card in win_map:
        cards[card] += 1
        for i in range(win_map[card]):
            cards[card + (i + 1)] += 1 * cards[card]
    return sum(cards.values())

if __name__ == "__main__":
    with open('./input/day04.txt') as f:
        raw_data = [line.strip() for line in f.readlines()]

    print('---- Part One ----') # 26914
    print(part_one(raw_data))

    print('---- Part Two ----') # 13080971
    print(part_two(raw_data))

