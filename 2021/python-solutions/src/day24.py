# Advent of Code
# Day 24

def solve(blocks):
  model_max = [0] * 14
  model_min = [0] * 14
  stack = []
  for i, block in enumerate(blocks):
    if block[3] == 'div z 1':
      stack.append((i, int(block[14].split(' ')[-1]))) # add y <val>
    elif block[3] == 'div z 26':
      j, x = stack.pop()
      diff = x + int(block[4].split(' ')[-1]) # add x <-val>
      if diff < 0:
        i, j, diff = j, i, -diff
      model_max[i] = 9
      model_max[j] = 9 - diff
      model_min[i] = 1 + diff
      model_min[j] = 1
  return model_max, model_min

if __name__ == '__main__':
  with open('input/day24.txt', 'r') as f:
    blocks = [block.split('\n') for block in f.read().split('inp w\n')[1:]]
  
  part1, part2 = solve(blocks)

  print('---- Part One ----')
  print(''.join(str(n) for n in part1))
  print('---- Part Two ----')
  print(''.join(str(n) for n in part2))
