# Advent of Code 2022
# Day 20

from collections import deque


def mix(original):
    nums = deque((i, n) for i, n in enumerate(original))

    for i, n in enumerate(original):
        idx = nums.index((i, n))
        nums.remove((i, n))
        nums.rotate(-n)
        nums.insert(idx, (i, n))

    return nums


def grove_coords(nums):
    final = [n for _, n in nums]
    zero_idx = final.index(0)

    return [final[(zero_idx + i * 1000) % len(nums)] for i in [1, 2, 3]]


if __name__ == "__main__":
    with open("input/day20.txt") as f:
        data = [int(line.strip()) for line in f.readlines()]

    print('---- Part One ----')
    print(sum(grove_coords(mix(data))))  # 7395
    print('---- Part Two ----')
    print()


# 1 moves between 2 and -3:
# 2, 1, -3, 3, -2, 0, 4

# 2 moves between -3 and 3:
# 1, -3, 2, 3, -2, 0, 4

# -3 moves between -2 and 0:
# 1, 2, 3, -2, -3, 0, 4

# 3 moves between 0 and 4:
# 1, 2, -2, -3, 0, 3, 4

# -2 moves between 4 and 1:
# 1, 2, -3, 0, 3, 4, -2

# 0 does not move:
# 1, 2, -3, 0, 3, 4, -2

# 4 moves between -3 and 0:
# 1, 2, -3, 4, 0, 3, -2
