# Advent of Code 2020
# Day 24: Lobby Layout

def identify_tile(tile):
    instructions = []
    i = 0
    while i < len(tile):
        if tile[i] == 's' or tile[i] == 'n':
            instructions.append(tile[i:i+2])
            i += 2
        else:
            instructions.append(tile[i])
            i += 1

    pos = 0
    directions = {'e': 1, 'w': -1,
                'ne': 0.5+0.5j, 'sw': -0.5-0.5j,
                'nw': -0.5+0.5j, 'se': 0.5-0.5j}
    for instr in instructions:
        pos += directions[instr]
    return pos

def check_neighbours(pos, flipped):
    black_neighbours = 0
    for i in [1, -1, 0.5+0.5j, -0.5-0.5j, -0.5+0.5j, 0.5-0.5j]:
        if pos + i in flipped:
            black_neighbours += 1
    return black_neighbours

def next_day(flipped):
    new_flipped = flipped.copy()
    for pos in flipped:
        blk_neighbours = check_neighbours(pos, flipped)
        if blk_neighbours == 0 or blk_neighbours > 2:
            new_flipped.remove(pos)

        neighbours = [pos + step for step in [1, -1, 0.5+0.5j, -0.5-0.5j, -0.5+0.5j, 0.5-0.5j]]
        for neighbour in neighbours:
            blk_neighbours = check_neighbours(neighbour, flipped)
            if blk_neighbours == 2:
                new_flipped.add(neighbour)
    return new_flipped

if __name__ == "__main__":
    with open("Data/day24.txt", "r") as f:
        tiles = [l.strip() for l in f.readlines()]

    flipped = set()
    for tile in tiles:
        loc = identify_tile(tile)
        if loc in flipped:
            flipped.remove(loc)
        else:
            flipped.add(loc)
    
    print("Part 1 solution:", len(flipped)) # 495

    for _ in range(100):
        flipped = next_day(flipped)
    
    print("Part 2 solution:", len(flipped))
