# Advent of Code 2022
# Day 08

from collections import defaultdict
from math import prod


def find_visible_trees(tree_lists):
    directions = [1, 1j, -1, -1j]
    trees = defaultdict(int)
    scenic_scores = defaultdict(list)

    size = len(tree_lists)
    for r in range(size):
        for c in range(size):
            trees[complex(r, c)] = int(tree_lists[r][c])

    visible = set()
    for r in range(1, size - 1):
        for c in range(1, size - 1):
            for d in directions:
                pos = complex(r, c)
                next_pos = pos + d
                val = trees[pos]
                isVisible = True
                final_distance, distance = 0, 0
                while ((next_pos.real >= 0 and next_pos.real <= size - 1) and (next_pos.imag >= 0 and next_pos.imag <= size - 1)):
                    pos = next_pos
                    distance += 1
                    if trees[pos] >= val:
                        isVisible = False
                        if final_distance == 0:
                            final_distance = distance
                    next_pos = pos + d

                if final_distance == 0:
                    final_distance = distance
                scenic_scores[complex(r, c)].append(final_distance)
                if isVisible:
                    visible.add(complex(r, c))

    return visible, scenic_scores


def acc_scenic_scores(scenic_scores):
    final_scenic_scores = {}
    max_total = 0
    for key in scenic_scores:
        total = prod(scenic_scores[key])
        final_scenic_scores[key] = total
        if total > max_total:
            max_total = total

    return max_total


if __name__ == "__main__":
    with open("input/day08.txt") as f:
        data = [list(line) for line in f.readlines()]

    visible, scenic_scores = find_visible_trees(data)

    print('---- Part One ----')
    print(len(visible) + (len(data) * 4) - 4)

    print('---- Part Two ----')
    print(acc_scenic_scores(scenic_scores))
