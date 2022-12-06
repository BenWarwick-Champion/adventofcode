# Advent of Code 2022
# Day 05

def parse_start_pos(start_pos):
    stacks = {}
    for line in start_pos[::-1]:
        column_num = 1
        for item in line[1::4]:
            if column_num not in stacks:
                stacks[column_num] = [item]
            else:
                if item != ' ':
                    stacks[column_num].append(item)
            column_num += 1
    return stacks


def parse_move(move):
    return [int(num) for num in move.split() if num.isdigit()]


def execute_move_p1(pos, num, old, new):
    for i in range(1, num + 1):
        pos[new].append(pos[old].pop())


def execute_move_p2(pos, num, old, new):
    moved = pos[old][-num:]
    for i in range(1, num + 1):
        pos[old].pop()
    pos[new].extend(moved)


def execute_moves(pos, moves, part=1):
    for move in moves:
        num, old, new = parse_move(move)
        if part == 1:
            execute_move_p1(pos, num, old, new)
        elif part == 2:
            execute_move_p2(pos, num, old, new)
    return pos


if __name__ == "__main__":
    with open("input/day05.txt") as f:
        data = f.readlines()
        start_pos = data[:8]
        moves = data[10:]

    print('---- Part One ----')
    final_pos_p1 = execute_moves(parse_start_pos(start_pos), moves)
    print(''.join([final_pos_p1[key][-1] for key in final_pos_p1]))

    print('---- Part Two ----')
    final_pos_p2 = execute_moves(parse_start_pos(start_pos), moves, 2)
    print(''.join([final_pos_p2[key][-1] for key in final_pos_p2]))
