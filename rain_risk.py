# Advent of Code 2020
# Day 12: Rain Risk

def follow_path(path):
    pos = 0
    seen = []
    facing = 'E'
    direction = {'N' : 1j, 'S' : -1j, 'E' : 1, 'W' : -1}
    for instr in path:
        dir, dist = instr[0], int(instr[1:])
        if dir in direction:
            for _ in range(dist):
                pos += direction[dir]
                seen.append(pos)
        elif dir == 'F':
            for _ in range(dist):
                pos += direction[facing]
                seen.append(pos)
        else:
            facing = is_facing(dir, dist, facing)
    return seen

def follow_waypoint(path):
    w_pos = 10+1j
    s_pos = 0
    direction = {'N':1j, 'S':-1j, 'E':1, 'W':-1}
    for instr in path:
        dir, dist = instr[0], int(instr[1:])
        if dir in direction:
            for _ in range(dist):
                w_pos += direction[dir]
        elif dir == 'F':
            for _ in range(dist):
                s_pos += w_pos
        else:
            for _ in range(dist//90):
                if dir == 'L':
                    w_pos = w_pos * 1j
                else:
                    w_pos = w_pos * -1j
    return s_pos

def is_facing(dir, deg, facing):
    f_direction = ['E', 'N', 'W', 'S']
    if dir == 'L':
        ind = f_direction.index(facing) + (deg//90)
        if ind > 3: ind -= 4
        new_facing = f_direction[ind]
    else: #dir == 'R'
        ind = f_direction.index(facing) - (deg//90)
        if ind < 0: ind += 4
        new_facing = f_direction[ind]
    return new_facing

def find_distance(coord):
    return int(abs(coord.real) + abs(coord.imag))

if __name__ == "__main__":
    with open("Data/day12.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    journey = follow_path(data)

    part1 = find_distance(journey[-1])
    print("Part 1 solution:", part1) #845

    part2 = find_distance(follow_waypoint(data))
    print("Part 2 solution:", part2)
    