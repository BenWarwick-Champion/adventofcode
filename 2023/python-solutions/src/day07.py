import string
from pprint import pprint
from collections import defaultdict
from functools import cmp_to_key

values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

joker_values = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14,
}

# 6 Five of a kind, where all five cards have the same label: AAAAA
# 5 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 4 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 3 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 2 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 1 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 0 High card, where all cards' labels are distinct: 23456

def calc_hand_strength(hand: str):
    hand = list(hand)
    hand_set = set(hand)

    if len(hand_set) == 1:
        return 6 # Five of a kind
    elif len(hand_set) == 2:
        for char in hand_set:
            if hand.count(char) == 4:
                return 5 # Four of a kind
        return 4 # Full house
    elif len(hand_set) == 3:
        for char in hand_set:
            if hand.count(char) == 3:
                return 3 # Three of a kind
        return 2 # Two pair
    elif len(hand_set) == 4:
        return 1 # One pair
    else:
        return 0 # High card

def compare(hand1: (str, str), hand2: (str, str)):
    hand1, hand2 = list(hand1[0]), list(hand2[0])
    for cards in zip(hand1, hand2):
        if cards[0] == cards[1]:
            continue
        else:
            if values[cards[0]] > values[cards[1]]:
                return 1
            else: 
                return -1
    return 0


def part_one(raw_data: list[str]):
    strengths = defaultdict(list)
    for game in raw_data:
        hand, bid = game.strip().split()
        strength = calc_hand_strength(hand)
        strengths[strength].append((hand, bid))
    
    output = []
    for i in range(7):
        sorted_bucket = sorted(strengths[i], key=cmp_to_key(compare))
        output.extend(sorted_bucket)
    return sum([(i+1)*int(hand[1]) for i, hand in enumerate(output)])

def calc_hand_strength2(hand: str):
    hand = list(hand)
    hand_set = set(hand)
    jokers = hand.count('J')
    hand_set.discard('J')

    if len(hand_set) == 0:
        return 6 # Five of a kind (Jokers)
    if len(hand_set) == 1:
        return 6 # Five of a kind
    elif len(hand_set) == 2:
        for char in hand_set:
            if hand.count(char) == 4 - jokers:
                return 5 # Four of a kind
        return 4 # Full house
    elif len(hand_set) == 3:
        for char in hand_set:
            if hand.count(char) == 3 - jokers:
                return 3 # Three of a kind
        return 2 # Two pair
    elif len(hand_set) == 4:
        return 1 # One pair
    else:
        return 0 # High card

def compare2(hand1: (str, str), hand2: (str, str)):
    hand1, hand2 = list(hand1[0]), list(hand2[0])
    for cards in zip(hand1, hand2):
        if cards[0] == cards[1]:
            continue
        else:
            if joker_values[cards[0]] > joker_values[cards[1]]:
                return 1
            else: 
                return -1
    return 0

def part_two(raw_data: list[str]):
    strengths = defaultdict(list)
    for game in raw_data:
        hand, bid = game.strip().split()
        strength = calc_hand_strength2(hand)
        strengths[strength].append((hand, bid))
    
    output = []
    for i in range(7):
        sorted_bucket = sorted(strengths[i], key=cmp_to_key(compare2))
        output.extend(sorted_bucket)
    return sum([(i+1)*int(hand[1]) for i, hand in enumerate(output)])

if __name__ == "__main__":
    with open('./input/day07.txt') as f:
        raw_data = f.readlines()

    print('---- Part One ----') # 246795406
    print(part_one(raw_data))

    print('---- Part Two ----') # 249356515
    print(part_two(raw_data))

