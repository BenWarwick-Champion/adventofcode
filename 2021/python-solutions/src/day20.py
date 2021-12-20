# Advent of Code
# Day 20

from collections import defaultdict


def enhance(points, algo, point):
  r, c = point
  binary = []
  for dr in [-1, 0, 1]:
    for dc in [-1, 0, 1]:
      if points[f'{r+dr},{c+dc}'] == '#':
        binary.append('1')
      else:
        binary.append('0')
  index = int(''.join(binary), 2)
  return algo[index]

def apply_algo(points, algo, default='.'):
  new_points = defaultdict(lambda: default)
  old_points = points.copy()
  for point in old_points:
    r, c = [int(x) for x in point.split(',')]
    for dr in [-1, 0, 1]:
      for dc in [-1, 0, 1]:
        new_points[f'{r+dr},{c+dc}'] = enhance(points, algo, (r+dr, c+dc))
  return new_points

def init_points(data):
  points = defaultdict(lambda: '.')
  for r, _ in enumerate(data):
    for c, _ in enumerate(data[r]):
      points[f'{r},{c}'] = data[r][c]
  return points

def part1(data, algo):
  points = init_points(data)
  for i in range(2):
    if i % 2 == 0:
      default = '#'
    else:
      default = '.'
    points = apply_algo(points, algo, default)
  return sum([1 for point in points if points[point] == '#'])

def part2(data, algo):
  points = init_points(data)
  for i in range(50):
    if i % 2 == 0:
      default = '#'
    else:
      default = '.'
    points = apply_algo(points, algo, default)
  return sum([1 for point in points if points[point] == '#'])

if __name__ == '__main__':
  with open('input/day20.txt', 'r') as f:
    algo, data = f.read().split('\n\n')
    data = [list(line) for line in data.splitlines()]

  print('---- Part One ----')
  print(part1(data, algo)) # 5489
  print('---- Part Two ----')
  print(part2(data, algo)) # 19066

