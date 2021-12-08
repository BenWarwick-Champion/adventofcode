# Advent of Code 2021
# Day 08:


def decode_line(line):
  signals, outputs = [codes.split() for codes in line.split(' | ')]

  # Eliminate unique signals {len: number}
  unique_signals = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
  }
  decoded = {}

  for signal in signals:
    if len(signal) in unique_signals:
      decoded[unique_signals[len(signal)]] = signal

  for signal in signals:
    segs = set(signal)
    if len(signal) == 5:
      # 2, 3, 5
      if set(decoded[1]) <= segs:
        decoded[3] = signal
      elif len(set(decoded[4]) & segs) == 3:
        decoded[5] = signal
      else:
        decoded[2] = signal

    if len(signal) == 6:
      # 0, 6, 9
      if set(decoded[1]) <= segs:
        if len(set(decoded[4]) & segs) == 4:
          decoded[9] = signal
        else:
          decoded[0] = signal
      else:
        decoded[6] = signal

  result = []
  for output in outputs:
    for key in decoded:
      if len(set(decoded[key]) ^ set(output)) == 0:
        result.append(str(key))
        break

  return ''.join(result)

def part1(notes):
  unique_signals = set([2, 3, 4, 7])
  instances = 0
  for line in notes:
    outputs = [codes for codes in line.split(' | ')[1].split()]
    for code in outputs:
      if len(code) in unique_signals:
        instances += 1
  return instances

def part2(notes):
  return sum(int(decode_line(line)) for line in notes)


if __name__ == "__main__":
  with open('./input/day08.txt') as f:
    notes = f.readlines()

  print('---- Part One ----')
  print(part1(notes))
  print('---- Part Two ----')
  print(part2(notes))
