# Advent of Code 2021
# Day 10:

def score_char(char):
  match char:
    case ')': return 3
    case ']': return 57
    case '}': return 1197
    case '>': return 25137
  print('Unknown char:', char)
  return 0

def score_ending(ending):
  score = 0
  for char in ending:
    score *= 5
    if char == ')':
      score += 1
    elif char == ']':
      score += 2
    elif char == '}':
      score += 3
    elif char == '>':
      score += 4
  return score

def is_corrupted(chunk):
  stack = []
  for char in chunk:
    if char in '<{([':
      stack.append(char)
    else:
      last = stack.pop()
      if last == '<' and char != '>':
        return score_char(char)
      if last == '{' and char != '}':
        return score_char(char)
      if last == '[' and char != ']':
        return score_char(char)
      if last == '(' and char != ')':
        return score_char(char)
  return False

def finish_chunk(chunk):
  stack = []
  for char in chunk:
    if char in '<{([':
      stack.append(char)
    else:
      stack.pop()

  ending = []
  for char in stack[::-1]:
    if char == '<':
      ending.append('>')
    elif char == '{':
      ending.append('}')
    elif char == '[':
      ending.append(']')
    elif char == '(':
      ending.append(')')
  
  return score_ending(ending)


def part1(chunks):
  return sum(is_corrupted(chunk) for chunk in chunks)

def part2(chunks):
  valid_chunks = [chunk for chunk in chunks if not is_corrupted(chunk)]
  scores = [finish_chunk(chunk) for chunk in valid_chunks]
  scores.sort()
  return scores[len(scores) // 2]


if __name__ == "__main__":
  with open('./input/day10.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]

  print('---- Part One ----')
  print(part1(data))
  print('---- Part Two ----')
  print(part2(data))
