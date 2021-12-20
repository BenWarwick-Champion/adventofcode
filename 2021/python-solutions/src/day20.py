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

def solve(data, algo, part2=False):
  points = init_points(data)
  iterations = 50 if part2 else 2
  for i in range(iterations):
    if i % 2 == 0 or algo[0] == '.':
      default = algo[0]
    else:
      default = algo[-1]
    points = apply_algo(points, algo, default)
  return sum([1 for point in points if points[point] == '#'])

if __name__ == '__main__':
  with open('input/day20.txt', 'r') as f:
    algo, data = f.read().split('\n\n')
    data = [list(line) for line in data.splitlines()]

  print('---- Part One ----')
  print(solve(data, algo)) # 5489
  print('---- Part Two ----')
  print(solve(data, algo, part2=True)) # 19066

