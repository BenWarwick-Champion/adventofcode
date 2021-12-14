# Advent of Code
# Day 13

from pprint import pprint

def do_fold(dots: set, fold):
  new_dots = set()
  direction, line = fold.split('=')
  if direction == 'x':
    for dot in dots:
      if dot[0] < int(line):
        new_dots.add(dot)
      elif dot[0] == int(line):
        continue
      else:
        delta = dot[0] - int(line)
        new_dots.add((int(line) - delta, dot[1]))
  else:
    for dot in dots:
      if dot[1] < int(line):
        new_dots.add(dot)
      elif dot[1] == int(line):
        continue
      else:
        delta = dot[1] - int(line)
        new_dots.add((dot[0], int(line) - delta))
  return new_dots


def part1(coords, folds):
  return len(do_fold(set(coords), folds[0]))

def part2(coords, folds):
  dots = set(coords)
  for fold in folds:
    dots = do_fold(dots, fold)

  for y in range(6):
    print()
    for x in range(40):
      if (x, y) in dots:
        print('#', end='')
      else:
        print(' ', end='')
  
  return len(dots)

if __name__ == "__main__":
  with open('./input/day13.txt') as f:
    coords, folds = f.read().split('\n\n')
    coords = [(int(x), int(y)) for x, y in (c.split(',') for c in coords.split('\n'))]
    folds = [fold.strip('fold along') for fold in folds.split('\n')]

  print('---- Part One ----')
  print(part1(coords, folds)) # 785
  print('---- Part Two ----')
  print(part2(coords, folds)) # FJAHJGAH

