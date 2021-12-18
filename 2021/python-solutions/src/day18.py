# Advent of Code
# Day 18

import math
import ast
import itertools

def split(x):
  if type(x) == int:
    if x > 9:
      return True, [x // 2, math.ceil(x / 2)]
    return False, x
  a, b = x
  changed, a = split(a)
  if changed:
    return True, [a, b]
  changed, b = split(b)
  return changed, [a, b]
  
def add_left(x, n):
  if n is None:
    return x
  if isinstance(x, int):
    return x + n
  return [add_left(x[0], n), x[1]]


def add_right(x, n):
  if n is None:
    return x
  if isinstance(x, int):
    return x + n
  return [x[0], add_right(x[1], n)]


def explode(x, n=4):
  if isinstance(x, int):
    return False, None, x, None
  if n == 0:
    return True, x[0], 0, x[1]
  a, b = x
  exp, left, a, right = explode(a, n - 1)
  if exp:
    return True, left, [a, add_left(b, right)], None
  exp, left, b, right = explode(b, n - 1)
  if exp:
    return True, None, [add_right(a, left), b], right
  return False, None, x, None

def add(a, b):
  x = [a, b]
  while True:
    change, _, x, _ = explode(x)
    if change:
      continue
    change, x = split(x)
    if not change:
      break
  return x

def magnitude(snail_num):
  if type(snail_num) == int:
    return snail_num
  return 3 * magnitude(snail_num[0]) + 2 * magnitude(snail_num[1])

def part1(nums):
  result = nums[0]
  for num in nums[1:]:
    result = add(result, num)
  return magnitude(result)

if __name__ == '__main__':
  with open('input/day18.txt', 'r') as f:
    nums = [ast.literal_eval(line) for line in f.readlines()]

  print('---- Part One ----')
  print(part1(nums)) # 4145
  print('---- Part Two ----')
  print(max(magnitude(add(a, b)) for a, b in itertools.permutations(nums, 2))) #4855

