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


def shortest_path(nodes, start, end, part=1):
    distances = {coord: None for coord in nodes}  # using None as unvisited

    # Determine neighbours of each node
    neighbours = defaultdict(list)
    for node in nodes:
        for delta in [1, -1, 1j, -1j]:
            val = nodes.get(node + delta)
            if part == 1:
                if val and ord(val) - ord(nodes[node]) <= 1:
                    neighbours[node].append(node + delta)
            else:
                if val and (ord(val) - ord(nodes[node]) == 0 or ord(val) - ord(nodes[node]) == -1):
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

            if part == 2 and nodes[neighbour] == 'a':
                return distances[neighbour]

    return distances[end] if part == 1 else distances[complex(40, 1)]


if __name__ == "__main__":
    with open("input/day12.txt") as f:
        data = f.readlines()

    nodes, start, end = parse_map(data)
    print('---- Part One ----')
    print(shortest_path(nodes, start, end))

    print('---- Part Two ----')
    # By inspection know that start pos will be the leftmost
    # column of the input... so just check them all ¯\_(ツ)_/¯
    print(min([shortest_path(nodes, complex(a, 0), end)
          for a in range(1, 41)]))
