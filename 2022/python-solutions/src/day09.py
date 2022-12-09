# Advent of Code 2022
# Day 09

direction_map = {
    'U': 1,
    'D': -1,
    'L': -1j,
    'R': 1j,
}


def find_visited(instructions):
    t_pos = complex(0, 0)
    h_pos = complex(0, 0)
    visited = set()
    for instruction in instructions:
        direction, distance = instruction.split()
        # print(instruction.strip())
        for step in range(int(distance)):
            h_pos += direction_map[direction]
            # visited.add(t_pos)

            diff = h_pos - t_pos
            # print(f'h_pos: {h_pos}, t_pos: {t_pos}, diff: {diff}')
            # print(f'abs diff.imag: {abs(diff.imag)}')
            if abs(diff.real) >= 2 or abs(diff.imag) >= 2:
                # We need to catch up
                if abs(diff.real) == 2 and diff.imag == 0:
                    t_pos += diff.real // 2
                elif abs(diff.real) == 2:
                    t_pos += complex(diff.real // 2, diff.imag)

                if abs(diff.imag) == 2 and diff.real == 0:
                    t_pos += complex(0, diff.imag // 2)
                elif abs(diff.imag) == 2:
                    t_pos += complex(diff.real, diff.imag // 2)
            visited.add(t_pos)

    return visited


if __name__ == "__main__":
    with open("input/day09.txt") as f:
        data = f.readlines()

    print('---- Part One ----')
    print(len(find_visited(data)))  # 6338 too low

    print('---- Part Two ----')
    print()
