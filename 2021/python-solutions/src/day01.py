# Advent of Code 2021
# Day 01: 

def count_increased(readings):
  return sum([reading > readings[index-1] for index, reading in enumerate(readings)])

def count_window_increased(readings, window):
  last_window_sum, count = 0, 0
  for index in range(len(readings)):
    window_sum = sum([readings[index + delta] for delta in range(window) if index + delta < len(readings)])
    if (window_sum > last_window_sum):
      count += 1
    last_window_sum = window_sum
  return count - 1

def part2_one_liner(readings, window):
  return sum([reading > readings[i-window] for i, reading in enumerate(readings) if i - window >= 0])

if __name__ == "__main__":
  with open('./input/day01.txt') as f:
    data = [int(line.strip()) for line in f.readlines()]
    print('---- Part One ----')
    print(count_increased(data)) # 1759
    print('---- Part Two ----')
    print(count_window_increased(data, 3)) # 1805
    print(part2_one_liner(data, 3)) # 1805
