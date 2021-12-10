# Advent of Code 2021
# Day 10:

opening_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
closing_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}

def score_char(char):
  char_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
  return char_scores[char]

def score_ending(ending):
  char_scores = {')': 1, ']': 2, '}': 3, '>': 4}
  score = 0
  for char in ending:
    score *= 5
    score += char_scores[char]
  return score

def is_corrupted(chunk):
  stack = []
  for char in chunk:
    if char in '<{([':
      stack.append(char)
    else:
      last = stack.pop()
      if closing_pairs[char] != last:
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
    ending.append(opening_pairs[char])
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
  print(part1(data)) # 265527
  print('---- Part Two ----')
  print(part2(data)) # 3969823589
