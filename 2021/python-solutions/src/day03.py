# Advent of Code 2021
# Day 03: Binary Diagnostic

def decode(output, length):
  binary_gamma = [int(output[num] > length//2) for num in output]
  binary_epsilon = [int(output[num] <= length//2) for num in output]
  return int(''.join(map(str, binary_gamma)), 2) * int(''.join(map(str, binary_epsilon)), 2)

def get_common_bit(codes, position):
  count = 0
  for code in codes:
    if code[position] == 1:
      count += 1

  if count * 2 == len(codes):
    return 1
  else:
    return int(count * 2 > len(codes))

def get_generator_code(codes):
  generator_codes = list(codes)
  for bit in range(len(codes[0])):
    new_codes = []
    if len(generator_codes) == 1:
      return generator_codes[0]
    most_common_bit = get_common_bit(generator_codes, bit)
    for code in generator_codes:
      if code[bit] == most_common_bit:
        new_codes.append(code)
    generator_codes = list(new_codes)
  return generator_codes[0]

def get_scrubber_code(codes):
  scrubber_codes = list(codes)
  for bit in range(len(codes[0])):
    new_codes = []
    if len(scrubber_codes) == 1:
      return scrubber_codes[0]
    most_common_bit = get_common_bit(scrubber_codes, bit)
    for code in scrubber_codes:
      if code[bit] != most_common_bit:
        new_codes.append(code)
    scrubber_codes = list(new_codes)
  return scrubber_codes[0]

def part1(codes):
  gamma = {}
  for code in codes:
    for index, bit in enumerate(code):
      if index not in gamma:
        gamma[index] = bit
      else:  
        gamma[index] += bit
  return decode(gamma, len(codes))

def part2(codes):
  generator_code = get_generator_code(codes)
  scrubber_code = get_scrubber_code(codes)
  return int(''.join(map(str, generator_code)), 2) * int(''.join(map(str, scrubber_code)), 2)

if __name__ == "__main__":
  with open('./input/day03.txt') as f:
    data = [[int(bit) for bit in list(line.strip())] for line in f.readlines()]
    print('---- Part One ----')
    print(part1(data)) # 841526
    print('---- Part Two ----')
    print(part2(data)) # 4790390
