# Advent of Code 2020
# Day 11: Seating System

import copy

with open('Data/day11.txt', 'r') as f:
    seats = [line.strip('\n') for line in f.readlines()]


for i in range(len(seats)):
    seats[i] = '.' + seats[i] + '.'
padding = len(seats[0]) * '.'
seats.insert(0, padding)
seats.append(padding)
s_arr = []
for line in seats:
    s_list = []
    for char in line:
        s_list.append(char)
    s_arr.append(s_list)


def create_kernel(r, c, s):
    window = [ [s[r-1][c-1], s[r-1][c], s[r-1][c+1]],
            [s[r][c-1], s[r][c], s[r][c+1]],
            [s[r+1][c-1], s[r+1][c], s[r+1][c+1]] ]
    return window


def calc_occupied(window):
    count = 0
    for r, row in enumerate(window):
        for c in range(len(row)):
            if window[r][c] == '#' and (r, c) != (1, 1):
                count += 1
    return count
    

next_seats = copy.deepcopy(s_arr)
seats_changed = True
while seats_changed:
    seats_changed = False
    last_seats = copy.deepcopy(next_seats)
    for r in range(1, len(last_seats[:-1])):
        for c in range(1, len(last_seats[0][:-1])):
            if last_seats[r][c] == '#' and calc_occupied(create_kernel(r, c, last_seats)) > 3:
                next_seats[r][c] = 'L'
                seats_changed = True
            if last_seats[r][c] == 'L' and calc_occupied(create_kernel(r, c, last_seats)) == 0:
                next_seats[r][c] = '#'
                seats_changed = True

occupied = 0
for line in next_seats:
    occupied += line.count('#')

print("Part 1 solution is:", occupied)

output = []
for line in next_seats:
    line = ''.join(line)
    output.append(line + '\n')

with open("Test/day11.txt", "w") as f:
    f.writelines(output)
