# Advent of Code 2020
# Day 22: Crab Combat

def play_game(p1, p2, part2 = False):
    seen = set()
    while not (len(p1) == 0 or len(p2) == 0):
        p1, p2 = play_round(p1, p2, seen, part2)
    return p1, p2

def play_round(p1, p2, seen, part2):
    if part2:
        rnd = str(p1) + str(p2)
        if rnd in seen:
            p2 = []
            return p1, p2
        else:
            seen.add(rnd)

    p1_top = p1.pop(0)
    p2_top = p2.pop(0)

    if part2 and len(p1) >= p1_top and len(p2) >= p2_top:
        _, p2r = play_game(p1[:p1_top], p2[:p2_top], part2=True)
        if len(p2r) == 0:
            p1.extend([p1_top, p2_top])
        else:
            p2.extend([p2_top, p1_top])
        return p1, p2
    else:
        if p1_top > p2_top:
            p1.extend([p1_top, p2_top])
        else:
            p2.extend([p2_top, p1_top])
        return p1, p2

def count_score(player):
    return sum((ind+1)*card for ind, card in enumerate(player[::-1]))

def init_players(data):
    p1 = [int(card) for card in data[1:26]]
    p2 = [int(card) for card in data[28:]]
    return p1, p2

def print_winner(p1, p2):
    if len(p2) == 0:
        print("Player 1 wins - Score:", count_score(p1))
    else:
        print("Player 2 wins - Score:", count_score(p2))


if __name__ == "__main__":
    with open("Data/day22.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    player1, player2 = init_players(data)
    player1, player2 = play_game(player1, player2)
    print_winner(player1, player2)

    player1, player2 = init_players(data)
    player1, player2 = play_game(player1, player2, part2=True)
    print_winner(player1, player2)

    # Part 1: Player 1 wins - Score: 35370
    # Part 2: Player 1 wins - Score: 36246
    # Crab wins boths times!
