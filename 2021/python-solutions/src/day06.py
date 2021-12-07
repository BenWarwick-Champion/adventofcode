# Advent of Code 2021
# Day 06:

def pass_day(ages):
  ages[9] = ages[0]
  for age in ages:
    if age == 9:
      continue
    ages[age] = ages.get(age + 1, 0)
  ages[6] = ages.get(6, 0) + ages[8]

def part1(age_list, days):
  ages = dict.fromkeys([i for i in range(9)], 0)
  for age in age_list:
    ages[age] = ages.get(age, 0) + 1
  for _ in range(days):
    pass_day(ages)
  return sum(ages.values()) - ages[9]
  

if __name__ == "__main__":
  with open('./input/day06.txt') as f:
    data = [int(num) for num in f.read().split(',')]
    print('---- Part One ----')
    print(part1(data, 80))
    print('---- Part Two ----')
    print(part1(data, 256))