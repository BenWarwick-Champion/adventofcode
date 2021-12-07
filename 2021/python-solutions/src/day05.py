# Advent of Code 2021
# Day 05: 

import pprint

def part1(coords):
  visited = {}
  for coord in coords:
    start, finish = coord
    if start.real != finish.real and start.imag != finish.imag:
      # Diagonal line
      continue
    if start.real == finish.real:
      # Vertical line
      steps = int(abs(start.imag - finish.imag) + 1)
      if start.imag > finish.imag:
        for i in range(steps):
          x = int(start.real)
          y = int(start.imag - i)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      else:
        for i in range(steps):
          x = int(start.real)
          y = int(start.imag + i)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      continue
    if start.imag == finish.imag:
      # Horizontal line
      steps = int(abs(start.real - finish.real) + 1)
      if start.real > finish.real:
        for i in range(steps):
          x = int(start.real - i)
          y = int(start.imag)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      else:
        for i in range(steps):
          x = int(start.real + i)
          y = int(start.imag)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      continue
    print('No line')
  return len([num for num in visited if visited[num] > 1])
    

def part2(coords):
  visited = {}
  for coord in coords:
    start, finish = coord
    if start.real != finish.real and start.imag != finish.imag:
      # Diagonal line
      steps = int(abs(start.real - finish.real) + 1)
      bltr = start.real < finish.real and start.imag < finish.imag
      trbl = start.real > finish.real and start.imag > finish.imag
      brtl = start.real > finish.real and start.imag < finish.imag
      tlbr = start.real < finish.real and start.imag > finish.imag
      if bltr:
        for i in range(steps):
          x = int(start.real + i)
          y = int(start.imag + i)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      elif trbl:
        for i in range(steps):
          x = int(start.real - i)
          y = int(start.imag - i)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      elif brtl:
        for i in range(steps):
          x = int(start.real - i)
          y = int(start.imag + i)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      elif tlbr:
        for i in range(steps):
          x = int(start.real + i)
          y = int(start.imag - i)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      continue
    if start.real == finish.real:
      # Vertical line
      steps = int(abs(start.imag - finish.imag) + 1)
      if start.imag > finish.imag:
        for i in range(steps):
          x = int(start.real)
          y = int(start.imag - i)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      else:
        for i in range(steps):
          x = int(start.real)
          y = int(start.imag + i)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      continue
    if start.imag == finish.imag:
      # Horizontal line
      steps = int(abs(start.real - finish.real) + 1)
      if start.real > finish.real:
        for i in range(steps):
          x = int(start.real - i)
          y = int(start.imag)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      else:
        for i in range(steps):
          x = int(start.real + i)
          y = int(start.imag)
          visited[f'{x},{y}'] = visited.get(f'{x},{y}', 0) + 1
      continue
    print('No line')
  return len([num for num in visited if visited[num] > 1])
    
if __name__ == "__main__":
  with open('./input/day05.txt') as f:
    input = [line.strip().split(' -> ') for line in f.readlines()]
    coords = []
    for raw_coords in input:
      old = [int(num) for num in raw_coords[0].split(',')]
      new = [int(num) for num in raw_coords[1].split(',')]
      old_coord = old[0] + old[1]*1j
      new_coord = new[0] + new[1]*1j
      coords.append([old_coord, new_coord])
    print('---- Part One ----')
    print(part1(coords))
    print('---- Part Two ----')
    print(part2(coords)) # 14113 too low
