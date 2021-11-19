# Advent of Code 2020
# Day 5: Binary Boarding


def find_seat(seat_code):
    '''Returns row (0-127) and col (0-7)'''
    row_code, col_code = '', ''
    for char in seat_code[:7]:
        if char == 'F':
            row_code += '0'
        else:
            row_code += '1'
    seat_row = int(row_code, 2)
    for char in seat_code.strip('\n')[-3:]:
        if char == 'L':
            col_code += '0'
        else:
            col_code+= '1'
    seat_col = int(col_code, 2)
    return seat_row, seat_col
        
def find_index(seat_coord):
    return seat_coord[0]*8 + seat_coord[1]

if __name__ == "__main__":
    with open("Data/day5.txt", "r") as f:
        input_data = f.readlines()

    # Part 1 solution
    max_id = 0
    for line in input_data:
        seat_id = find_index(find_seat(line))
        if seat_id > max_id:
            max_id = seat_id
    print(f'The maximum seat index is: {max_id}') # 813

    # Part 2 solution
    seen = []
    for line in input_data:
        seat_id = find_index(find_seat(line))
        seen.append(seat_id)

    seen.sort()
    last_seat = 0
    missing_seats = []
    for seat in seen:
        if seat == last_seat + 2:
            missing_seats.append(seat - 1)
        last_seat = seat
    print(f'List of single missing seats: {missing_seats}')