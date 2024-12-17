# Advent of Code 2024
# Day 16

import heapq

class Complex(complex):
    __lt__=lambda s,o: (s.imag,s.real) < (o.imag,o.real)
    __add__=lambda s,o: Complex(complex(s)+o)

def parse_data(raw_data):
    maze = dict()
    for r, row in enumerate(raw_data):
        for c, char in enumerate(row):
            maze[Complex(r, c)] = char
            if char == 'S':
                start = Complex(r, c)
            if char == 'E':
                end = Complex(r, c)
    return maze, start, end

def dijkstra(maze, start, end):
    queue = [(0, start, 1j, [start])]
    visited = dict()
    best = set()
    low = float('inf')

    while queue:
        cost, pos, direction, path = heapq.heappop(queue)
        if cost > low: break
        if pos == end:
            if low > cost: best.clear()
            low = cost
            best |= set(path)
        visited[pos, direction] = cost

        for d in map(Complex, (1, -1, 1j, -1j)):
            if maze.get(pos + d, '#') == '#': continue
            additional_cost = 1001 if d != direction else 1
            if visited.get((pos + d, d), float('inf')) > cost + additional_cost:
                heapq.heappush(queue, (cost + additional_cost, pos + d, d, path + [pos + d]))
    return low, best

def part_one(raw_data):
    maze, start, end = parse_data(raw_data)
    cost, _ = dijkstra(maze, start, end)
    return cost

def part_two(raw_data):
    maze, start, end = parse_data(raw_data)
    _, best = dijkstra(maze, start, end)
    return len(best)

if __name__ == "__main__":
    with open("input/day16.txt") as f:
        raw_data = f.readlines()
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))

