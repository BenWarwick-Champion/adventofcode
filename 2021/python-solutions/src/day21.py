# Advent of Code
# Day 21

import functools

def roll_die():
  while True:
    for i in range(1, 101):
      yield i

def roll_quantum_die():
  return [
    i + j + k
    for i in (1, 2, 3)
    for j in (1, 2, 3)
    for k in (1, 2, 3)
  ] 

def take_turn(die, pos):
  rolls = 0
  for _ in range(3):
    rolls += next(die)
  
  new_pos = (pos + rolls) % 10
  if new_pos == 0:
    new_pos = 10
  return new_pos

def calc(p1_score, p2_score, moves):
  if p1_score > p2_score:
    return p2_score * moves
  else:
    return p1_score * moves

def play_game(p1_pos, p2_pos):
  p1_score, p2_score, moves = 0, 0, 0
  p1_turn = True
  die = roll_die()
  while p1_score < 1000 and p2_score < 1000:
    moves += 3
    if p1_turn:
      p1_pos = take_turn(die, p1_pos)
      p1_score += p1_pos
      p1_turn = False
    else:
      p2_pos = take_turn(die, p2_pos)
      p2_score += p2_pos
      p1_turn = True
  return calc(p1_score, p2_score, moves)

@functools.lru_cache(maxsize=None)
def play_quantum_game(state):
  score, pos = state[0]
  state = [state[1], None]
  wins = [0, 0]
  for roll in roll_quantum_die():
    newpos = (pos + roll - 1) % 10 + 1
    newscore = score + newpos
    state[1] = (newscore, newpos)
    if newscore >= 21:
      wins[0] += 1
    else:
      myself, other = play_quantum_game(tuple(state))
      wins = [wins[0] + other, wins[1] + myself]
  return wins

if __name__ == '__main__':
  with open('input/day21.txt', 'r') as f:
    p1_start, p2_start = [int(line.strip()[-1]) for line in f.readlines()]

  print('---- Part One ----')
  print(play_game(p1_start, p2_start))

  print('---- Part Two ----')
  print(max(play_quantum_game(((0, p1_start), (0, p2_start)))))

