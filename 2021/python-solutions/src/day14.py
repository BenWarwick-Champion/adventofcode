# Advent of Code
# Day 14: Extended Polymerization

from collections import Counter

def simulate_steps(rules, pairs, chars, steps):
  for _ in range(steps):
    for (a,b), count in pairs.copy().items():
      x = rules[a+b]
      pairs[a+b] -= count
      pairs[a+x] += count
      pairs[x+b] += count
      chars[x] += count
  return max(chars.values()) - min(chars.values())


if __name__ == "__main__":
  with open('./input/day14.txt') as f:
    template, _, *rules = f.read().split('\n')

  rules = dict(r.split(' -> ') for r in rules)
  pairs = Counter(map(str.__add__, template, template[1:]))
  chars = Counter(template)

  print('---- Part One ----')
  print(simulate_steps(rules, pairs.copy(), chars.copy(), 10))
  print('---- Part Two ----')
  print(simulate_steps(rules, pairs.copy(), chars.copy(), 40))
