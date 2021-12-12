# Advent of Code 2021
# Day 11: Dumbo Octopus

from copy import deepcopy

def simulate_step(levels):
  for r, _ in enumerate(levels):
    for c, _ in enumerate(levels[0]):
      levels[r][c] += 1

  flashed = True
  while flashed:
    flashed = False
    for r, _ in enumerate(levels):
      for c, _ in enumerate(levels[0]):
        if levels[r][c] != '#' and levels[r][c] > 9:
          levels[r][c] = '#'
          flashed = True
          for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
              if dr == 0 and dc == 0:
                continue
              if r + dr < 0 or r + dr >= len(levels) or c + dc < 0 or c + dc >= len(levels[0]):
                continue
              if levels[r+dr][c+dc] == '#':
                continue
              levels[r+dr][c+dc] += 1

  for r, _ in enumerate(levels):
    for c, _ in enumerate(levels[0]):
      if levels[r][c] == '#':
        levels[r][c] = 0
  return levels

def part1(data):
  flashes = 0
  for _ in range(100):
    data = simulate_step(data)
    flashes += sum(sum(1 for c in row if c == 0) for row in data)
  return flashes

def part2(data):
  step, flashes = 0, 0
  while flashes < 100:
    flashes = 0
    data = simulate_step(data)
    step += 1
    flashes = sum(sum(1 for c in row if c == 0) for row in data)
  return step

if __name__ == "__main__":
  with open('./input/day11.txt') as f:
    data = [[int(num) for num in line.strip()] for line in f.readlines()]

  print('---- Part One ----')
  print(part1(deepcopy(data))) # 1729
  print('---- Part Two ----')
  print(part2(deepcopy(data))) # 237
