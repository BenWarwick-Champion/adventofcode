# Advent of Code 2020
# Day 3: Toboggan Trajectory

# Part 1: Count all the trees you hit when traversing down the slope
# 3 to the right and 1 down.

# Part 2: The multiply together the number of trees from different slopes
# 1 across, 1 down
# 3 across, 1 down
# 5 across, 1 down
# 7 across, 1 down
# 1 across, 2 down

def tree_counter(toboggan_slope, y_increment, x_increment=1):
    tree_count = 0
    y_pos = 0
    for row in range(0, len(toboggan_slope), x_increment):
        if toboggan_slope[row][y_pos] == '#':
            tree_count += 1
        y_pos += y_increment
    return tree_count

def  create_slope(input_data, n):
    return [line.strip('\n')*n for line in input_data]

if __name__ == "__main__":
    with open("Data/day3.txt", "r") as input_file:
        input_data = input_file.readlines()

    # part 1 solution
    toboggan_slope = create_slope(input_data, 100)
    print(tree_counter(toboggan_slope, 3))

    # part 2 solution
    answer = (
        tree_counter(toboggan_slope, 1) * 
        tree_counter(toboggan_slope, 3) * 
        tree_counter(toboggan_slope, 5) *
        tree_counter(toboggan_slope, 7) *
        tree_counter(toboggan_slope, 1, 2))
    print(f'The total is: {answer}')
