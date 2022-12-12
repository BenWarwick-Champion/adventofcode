# Advent of Code 2022
# Day 12

from collections import defaultdict, deque
from pprint import pprint


# Create a map of complex coords to height values
def parse_map(data):
    nodes = {}
    line_count = len(data)
    for ind, line in enumerate(data):
        for i, val in enumerate(list(line)):
            pos = complex(line_count - ind, i)
            match val:
                case 'S':
                    start = pos
                    nodes[pos] = 'a'
                case 'E':
                    end = pos
                    nodes[pos] = 'z'
                case _:
                    nodes[pos] = val
    return nodes, start, end


def shortest_path(nodes, start, end):
    distances = {coord: None for coord in nodes}  # using None as unvisited

    # Determine neighbours of each node
    neighbours = defaultdict(list)
    for node in nodes:
        for delta in [1, -1, 1j, -1j]:
            val = nodes.get(node + delta)
            if val and ord(val) - ord(nodes[node]) <= 1:
                neighbours[node].append(node + delta)

    Q = deque()
    Q.append(start)
    distances[start] = 0

    while len(Q) != 0:
        current = Q.popleft()
        for neighbour in neighbours[current]:
            if distances[neighbour] == None:
                distances[neighbour] = distances[current] + 1
                Q.append(neighbour)

    return distances[end]


if __name__ == "__main__":
    with open("input/day12.txt") as f:
        data = f.readlines()

    print('---- Part One ----')
    pprint(shortest_path(*parse_map(data)))

    print('---- Part Two ----')
    print()
