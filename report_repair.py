# Advent of Code 2020
# Day 1: Report Repair

# Part 1 function
def report_repair(input_data, sum_num):

    check_set = set()
    for val in input_data:
        check_set.add(int(val))
    
    for num in input_data:
        check_val = sum_num - int(num)
        if check_val in check_set:
            return int(num) * check_val

    return 'Not Found'


# Part 2 function
def report_repair_part2(input_data, sum_num):

    check_set = set()
    for val in input_data:
        check_set.add(int(val))

    for num in input_data:
        check_val = sum_num - int(num)
        for num2 in input_data:
            num3 = check_val - int(num2)
            if num3 in check_set:
                return int(num) * int(num2) * num3
    return 'Not Found'


if __name__ == "__main__":
    input_file = open("Data/report_repair_input.txt", "r")
    input_data = input_file.readlines()
    input_file.close()

    print("Part 1 solution is: ", report_repair(input_data, 2020))
    print("Part 2 solution is: ", report_repair_part2(input_data, 2020))