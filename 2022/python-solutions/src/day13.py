# Advent of Code 2022
# Day 13

from ast import literal_eval
from functools import cmp_to_key


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    elif left and right:
        result = compare(left[0], right[0])
        if result:
            return result
        else:
            return compare(left[1:], right[1:])
    else:
        return 1 if left else (-1 if right else 0)


if __name__ == "__main__":
    with open("input/day13.txt") as f:
        data = f.read().split('\n\n')

    pairs, packets = [], [[[2]], [[6]]]
    for p in data:
        a, b = map(literal_eval, p.split('\n'))
        pairs.append((a, b))
        packets.extend([a, b])

    print('---- Part One ----')
    print(sum(i + 1 for i, x in enumerate(pairs)
              if compare(x[0], x[1]) == -1))

    print('---- Part Two ----')
    packets_sorted = sorted(packets, key=cmp_to_key(compare))
    print((1 + packets_sorted.index([[2]]))
          * (1 + packets_sorted.index([[6]])))
