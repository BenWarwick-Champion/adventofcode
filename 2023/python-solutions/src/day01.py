# Advent of Code 2023
# Day 01:

import re
from pprint import pprint

translations = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_calibration_numbers(calibration_line: str):
    numbers = [i for i in list(calibration_line) if i.isdigit()]
    # print(int(numbers[0] + numbers[-1]))
    return int(numbers[0] + numbers[-1])
    
def get_calibration_numbers_and_words(calibration_line: str):
    positions = {}
    for key in translations.keys():
        for i in re.finditer(key, calibration_line):
            positions[i.start()] = key

    # print(calibration_line)
    new_line = calibration_line
    keys = [sorted(list(positions))[k] for k in [0, -1] if sorted(list(positions))]
    for index in keys:
        new_line = new_line.replace(positions[index], translations[positions[index]])
        
    # print(new_line)
    return get_calibration_numbers(new_line)

def get_calibration_numbers_and_words_simple(line: str):
    line = (line.replace("one", "o1e")
    .replace("two", "t2o")
    .replace("three", "t3e")
    .replace("four", "f4r")
    .replace("five", "f5e")
    .replace("six", "s6x")
    .replace("seven", "s7n")
    .replace("eight", "e8t")
    .replace("nine", "n9e"))
    return get_calibration_numbers(line)

if __name__ == "__main__":
    with open('./input/day01.txt') as f:
        calibration_lines = f.readlines()

    print('---- Part One ----') # 55090
    print(sum([get_calibration_numbers(line.strip()) for line in calibration_lines]))


    print('---- Part Two ----') # 54845
    print(sum([get_calibration_numbers_and_words_simple(line.strip()) for line in calibration_lines]))

