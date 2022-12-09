# Advent of Code 2022
# Day 09

direction_map = {
    'R': 1,
    'L': -1,
    'D': -1j,
    'U': 1j,
}


def sign(num):
    return (num > 0) - (num < 0)


def complex_sign(c_num):
    return sign(c_num.real) + sign(c_num.imag) * 1j


def find_visited(instructions):
    rope = [0 for _ in range(10)]
    p1_visited = set()
    p2_visited = set()

    for instruction in instructions:
        direction, distance = instruction.split()

        for _ in range(int(distance)):
            rope[0] += direction_map[direction]
            for i in range(1, 10):
                diff = rope[i-1] - rope[i]

                if abs(diff) >= 2:
                    rope[i] += complex_sign(diff)

            p1_visited.add(rope[1])
            p2_visited.add(rope[-1])
    return p1_visited, p2_visited


if __name__ == "__main__":
    with open("input/day09.txt") as f:
        data = f.readlines()

    p1, p2 = find_visited(data)
    print('---- Part One ----')
    print(len(p1))  # 6339

    print('---- Part Two ----')
    print(len(p2))  # 2541
