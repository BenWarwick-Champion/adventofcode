import string
from pprint import pprint


def parse_hand(hand: str):
    counts = {}
    colours = hand.split(',')
    for colour in colours: # ' 2 red'
        num, col = colour.strip().split()
        num = int(num)
        if num > counts.get(col, 0):
            counts[col] = num
    return counts

def parse_game(raw_game: str):
    game_id, hands = raw_game.strip().split(':')
    id = int(game_id.strip(string.ascii_letters))
    hands = hands.strip().split(';')

    hands = [parse_hand(hand) for hand in hands]
    # 1, [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]
    return id, hands

def part_one(games: dict[int, list[dict[str, int]]]):
    impossible = []
    for game in games:
        for hand in games[game]:
            for colour, count in hand.items():
                if colour == 'red' and count > 12:
                    impossible.append(game)
                if colour == 'green' and count > 13:
                    impossible.append(game)
                if colour == 'blue' and count > 14:
                    impossible.append(game)

    return sum(games) - sum(set(impossible))


def part_two(games: dict[int, list[dict[str, int]]]):
    total = 0
    for game in games:
        r, g, b = 0, 0, 0
        for hand in games[game]:
            for colour, count in hand.items():
                if colour == 'red' and count > r:
                    r = count
                if colour == 'green' and count > g:
                    g = count
                if colour == 'blue' and count > b:
                    b = count
        total += (r * g * b)
    return total


if __name__ == "__main__":
    with open('./input/day02.txt') as f:
        raw_data = f.readlines()

    print('---- Part One ----')
    games = dict([parse_game(game) for game in raw_data])
    # pprint(games)
    print(part_one(games))
    


    print('---- Part Two ----')
    print(part_two(games))

