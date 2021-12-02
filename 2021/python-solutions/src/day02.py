# Advent of Code 2021
# Day 02: 

def part1(moves, start_position=0):
  for move in moves:
    direction, distance = move.split()
    distance = int(distance)
    if direction == 'forward':
      start_position += distance
    elif direction == 'up':
      start_position -= distance * 1j
    elif direction == 'down':
      start_position += distance * 1j
  return int(start_position.real * start_position.imag)

def part2(moves, start_position=0):
  aim = 0
  for move in moves:
    direction, distance = move.split()
    distance = int(distance)
    if direction == 'forward':
      start_position += distance + (aim * distance)*1j
    elif direction == 'up':
      aim -= distance
    elif direction == 'down':
      aim += distance
  return int(start_position.real * start_position.imag)

if __name__ == "__main__":
  with open('./input/day02.txt') as f:
    data = [line.strip() for line in f.readlines()]
    print('---- Part One ----')
    print(part1(data)) # 2187380
    print('---- Part Two ----')
    print(part2(data)) # 2086357770
