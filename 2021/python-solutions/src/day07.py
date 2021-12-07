# Advent of Code 2021
# Day 07:

import statistics, math

def part1(positions):
  median = int(statistics.median(positions))
  return sum(abs(x - median) for x in positions)

def part2(positions):
  mean = int(statistics.mean(positions))
  total_cost = 0
  for position in positions:
    delta = abs(position - mean)
    cost = 0
    for i in range(delta + 1):
      cost += i
    total_cost += cost
  return total_cost

if __name__ == "__main__":
  with open('./input/day07.txt') as f:
    data = [int(num) for num in f.read().split(',')]

  print('---- Part One ----')
  print(part1(data)) # 351901
  print('---- Part Two ----')
  print(part2(data)) # 101079875

