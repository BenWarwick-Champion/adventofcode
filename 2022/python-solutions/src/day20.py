# Advent of Code 2022
# Day 20

from collections import deque


def mix(original, times=1):
    nums = deque((i, n) for i, n in enumerate(original))

    for _ in range(times):
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
    DECRYPTION_KEY = 811589153  # 1640221678213
    print(sum(grove_coords(mix([n * DECRYPTION_KEY for n in data], 10))))
