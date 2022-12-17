# Advent of Code 2022
# Day 17

ROCKS = [
    [(2, 0), (3, 0), (4, 0), (5, 0)],  # Horizontal Line
    [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],  # Plus
    [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],  # L
    [(2, 0), (2, 1), (2, 2), (2, 3)],  # Vertical Bar
    [(2, 0), (2, 1), (3, 0), (3, 1)],  # Square
]


def run_sim(jets, no_of_rounds):
    TOWER_WIDTH = 7
    tower = {(x, 0) for x in range(TOWER_WIDTH)}
    tower_height = 0

    current_round = 0
    jet_index = 0

    while current_round < no_of_rounds:
        # Select rock
        rock_index = current_round % len(ROCKS)
        rock = ROCKS[rock_index]

        # Initialise rock position
        y_offset = tower_height + 4
        rock = [(x, y + y_offset) for x, y in rock]

        while True:
            # Evaluate jet
            jet = -1 if jets[jet_index] == '<' else 1
            jet_index = (jet_index + 1) % len(jets)

            next_rock = [(x + jet, y) for x, y in rock]
            if any(x < 0 or x >= TOWER_WIDTH for x, y in next_rock):
                next_rock = rock
            elif any(coord in tower for coord in next_rock):
                next_rock = rock

            rock = next_rock

            # Evaluate gravity
            next_rock = [(x, y - 1) for x, y in rock]
            if any(coord in tower for coord in next_rock):
                # Rock stopped
                tower.update(rock)
                tower_height = max(tower_height, max(y for x, y in rock))
                break
            else:
                rock = next_rock

        current_round += 1
    return tower_height


if __name__ == "__main__":
    with open("input/day17.txt") as f:
        data = list(f.read().strip())

    print('---- Part One ----')
    print(run_sim(data, 2022))

    print('---- Part Two ----')
    print(run_sim(data, 1_000_000_000_000))
