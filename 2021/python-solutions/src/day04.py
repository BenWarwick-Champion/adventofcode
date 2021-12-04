# Advent of Code 2021
# Day 04: 

def init_marks(num_of_boards, board_size):
  marks = []
  for i in range(num_of_boards):
    marks.append([[False for _ in range(board_size)] for _ in range(board_size)])
  return marks

def mark_number_for_board(board, board_index, number, marks):
  for r, row in enumerate(board):
    for c, col in enumerate(row):
      if col == number:
        marks[board_index][r][c] = True

def check_winning_boards(marks, winning_boards = set()):
  new_winners = []
  for board_index, board in enumerate(marks):
    for row in board:
      if all(row) and board_index not in winning_boards:
        new_winners.append(board_index)
    for col in range(len(board)):
      if all(row[col] for row in board) and board_index not in winning_boards:
        new_winners.append(board_index)
  if len(new_winners) == 0:
    return -1
  return new_winners

def score_board(board, marked):
  score = 0
  for r, row in enumerate(board):
    for c, col in enumerate(row):
      if not marked[r][c]:
        score += col
  return score

def part1(numbers, boards, marks):
  for number in numbers:
    for board_index in range(len(boards)):
      mark_number_for_board(boards[board_index], board_index, number, marks)
    winning_boards = check_winning_boards(marks)
    if winning_boards != -1:
      return score_board(boards[winning_boards[0]], marks[winning_boards[0]]) * number
  return -1

def part2(numbers, boards, marks):
  winning_boards = set()
  for number in numbers:
    for board_index in range(len(boards)):
      mark_number_for_board(boards[board_index], board_index, number, marks)
    new_winners = check_winning_boards(marks, winning_boards)
    if new_winners != -1:
      for winner in new_winners:
        winning_boards.add(winner)
      if (len(winning_boards) == len(boards)):
        index = new_winners[-1]
        return score_board(boards[index], marks[index]) * number
  return -1

if __name__ == "__main__":
  with open('./input/day04.txt') as f:
    numbers, *boards = f.read().split('\n\n')
    numbers = [int(num) for num in numbers.split(',')]
    boards = [[[int(num) for num in row.split()] for row in board.split('\n')] for board in boards]
    print('---- Part One ----')
    print(part1(numbers, boards, init_marks(len(boards), len(boards[0])))) # 72770
    print('---- Part Two ----')
    print(part2(numbers, boards, init_marks(len(boards), len(boards[0])))) # 13912
