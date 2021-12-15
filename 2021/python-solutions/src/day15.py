# Advent of Code
# Day 15

from collections import defaultdict
from heapq import heappush, heappop

def shortest_path(cave, start, end):
  visited = set()
  weights = defaultdict(lambda: float('inf'))
  weights[start] = 0
  queue = [(0, start)]
  directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

  while queue:
    dist, current = heappop(queue)

    if current == end:
      return dist

    if current in visited:
      continue

    visited.add(current)

    for dr, dc in directions:
      nr, nc = current[0] + dr, current[1] + dc

      if (nr < 0 or nr >= len(cave) or nc < 0 or nc >= len(cave[0])):
        continue


      alt = weights[current] + cave[nr][nc]
      if alt < weights[(nr, nc)]:
        weights[(nr, nc)] = alt
        heappush(queue, (alt, (nr, nc)))

  return weights[end]
  
def extend_cave(cave):
  tilew = len(cave)
  tileh = len(cave[0])
  for _ in range(4):
    for row in cave:
      tail = row[-tilew:]
      row.extend((x + 1) if x < 9 else 1 for x in tail)
      
  for _ in range(4):
    for row in cave[-tileh:]:
      row = [(x + 1) if x < 9 else 1 for x in row]
      cave.append(row)
  return cave

if __name__ == "__main__":
  with open('./input/day15.txt') as f:
    cave = [[int(num) for num in line.strip()] for line in f.readlines()]

  print('---- Part One ----')
  print(shortest_path(cave, (0, 0), (len(cave) - 1, len(cave[0]) - 1)))
  print('---- Part Two ----')
  print(shortest_path(extend_cave(cave), (0, 0), (len(cave) - 1, len(cave[0]) - 1)))
