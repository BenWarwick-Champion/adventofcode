# Advent of Code 2020
# Day 11: Seating System

import copy
import time

def count_occupied(r, c, s):
    occupied = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0: continue
            k_r = r + dr
            k_c = c + dc

            # skip over the floor
            while 0 <= k_r < len(s) and 0 <= k_c < len(s[0]) and s[k_r][k_c] == '.':
                k_r += dr
                k_c += dc

            # now we have reached a seat, check if it's filled
            if 0 <= k_r < len(s) and 0 <= k_c < len(s[0]) and s[k_r][k_c] == '#':
                occupied += 1
    return occupied
                
            
if __name__ == "__main__":

    tic = time.perf_counter()
    with open('Data/day11.txt', 'r') as f:
        seats = [line.strip('\n') for line in f.readlines()]

    # Adding padding and creating array
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

    # Calculate for every value in the array and insert into new array
    next_seats = copy.deepcopy(s_arr)
    seats_changed = True
    while seats_changed:
        seats_changed = False
        last_seats = copy.deepcopy(next_seats)
        for r in range(1, len(last_seats[:-1])):
            for c in range(1, len(last_seats[0][:-1])):
                if last_seats[r][c] == '#' and count_occupied(r, c, last_seats) > 4:
                    next_seats[r][c] = 'L'
                    seats_changed = True
                if last_seats[r][c] == 'L' and count_occupied(r, c, last_seats) == 0:
                    next_seats[r][c] = '#'
                    seats_changed = True

    # Count and print the number of occupied seats
    answer = 0
    for line in next_seats:
        answer += line.count('#')
    print("Part 2 solution is:", answer)

    toc = time.perf_counter()
    print("Time taken:", toc-tic)
