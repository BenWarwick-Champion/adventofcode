# Advent of Code 2021
# Day 09:

from math import prod

def find_low_points(grid):
  low_points = []
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      lowest = True
      for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if r + dr < 0 or r + dr >= len(grid) or c + dc < 0 or c + dc >= len(grid[0]):
          continue
        if grid[r+dr][c+dc] <= grid[r][c]:
          lowest = False
          break
      if lowest:
        low_points.append((r, c))
  return low_points

def part1(grid):
  return sum(grid[r][c] + 1 for r, c in find_low_points(grid))

def part2(grid):
  low_points = find_low_points(grid)
  sizes = []
  for r, c in low_points:
    area = {(r, c)}
    last_size = 0
    while len(area) > last_size:
      last_size = len(area)
      new_area = set()
      for cr, cc in area:
        if grid[cr][cc] == 9:
          continue
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
          if cr + dr < 0 or cr + dr >= len(grid) or cc + dc < 0 or cc + dc >= len(grid[0]):
            continue
          if grid[cr+dr][cc+dc] == 9:
            continue
          if grid[cr+dr][cc+dc] >= grid[cr][cc]:
            new_area.add((cr+dr, cc+dc))
      area = area | new_area
    sizes.append(len(area))
  sizes.sort()
  return prod(sizes[-3:])

if __name__ == "__main__":
  with open('./input/day09.txt') as f:
    data = [[int(num) for num in list(line.strip())] for line in f.readlines()]

  print('---- Part One ----')
  print(part1(data)) # 436
  print('---- Part Two ----')
  print(part2(data)) # 1317792
