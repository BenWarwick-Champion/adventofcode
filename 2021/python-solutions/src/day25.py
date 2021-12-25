# Advent of Code
# Day 25

import itertools

def solve(cucumbers):
  w, h = len(cucumbers[0]), len(cucumbers)
  east = set((r, c) for r, ln in enumerate(cucumbers) for c, cucumber in enumerate(ln) if cucumber == '>')
  south = set((r, c) for r, ln in enumerate(cucumbers) for c, cucumber in enumerate(ln) if cucumber == 'v')

  for step in itertools.count(1):
    occupied = frozenset(east | south)
    _east = set()
    for r, c in east:
      if (r, (c + 1) % w) in occupied:
        _east.add((r, c))
      else:
        _east.add((r, (c + 1) % w))

    occupied = frozenset(_east | south)
    _south = set()
    for r, c in south:
      if ((r + 1) % h, c) in occupied:
        _south.add((r, c))
      else:
        _south.add(((r + 1) % h, c))

    if (east == _east) and (south == _south):
      return step
      
    east = _east
    south = _south


if __name__ == '__main__':
  with open('input/day25.txt', 'r') as f:
    cucumbers = [list(line.strip()) for line in f.readlines()]

  print('----- Part 1 -----')
  print(solve(cucumbers))
  print('----- Part 2 -----')
  print('Remotely start the sleigh!')
