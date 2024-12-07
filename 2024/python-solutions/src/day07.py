# Advent of Code 2023
# Day 07

def parse_equations(raw_data):
    lines = raw_data.split('\n')
    equations = []
    for line in lines:
        test_value, nums = line.split(':')
        nums = [int(num) for num in nums.split()]
        test_value = int(test_value)
        equations.append((test_value, nums))
    return equations

def eval_equation(test_value, nums, part2=False):
    if len(nums) == 1:
        return nums[0] == test_value    
    if eval_equation(test_value, [nums[0] + nums[1], *nums[2:]], part2):
        return True
    if eval_equation(test_value, [nums[0] * nums[1], *nums[2:]], part2):
        return True
    if part2 and eval_equation(test_value, [int(''.join([str(nums[0]), str(nums[1])])), *nums[2:]], part2):
        return True
    return False

def part_one(raw_data):
    equations = parse_equations(raw_data)
    result = 0
    for test_value, nums in equations:
        if eval_equation(test_value, nums):
            result += test_value
    return result

def part_two(raw_data):
    equations = parse_equations(raw_data)
    result = 0
    for test_value, nums in equations:
        if eval_equation(test_value, nums, part2=True):
            result += test_value
    return result

if __name__ == "__main__":
    with open("input/day07.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 945512582195

    print('---- Part Two ----')
    print(part_two(raw_data)) # 271691107779347
