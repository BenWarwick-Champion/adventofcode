# Advent of Code 2020
# Day 9: Encoding Error

def sliding_window(data, preamble):
    for ind in range(preamble + 1, len(data)):
        window = data[ind - preamble - 1 : ind - 1]
        if not check_sums(window, data[ind-1]):
            return data[ind-1], ind - 1

def sliding_window_part2(data, preamble, ans):
    for ind in range(preamble + 1, len(data)):
        window = data[ind - preamble - 1 : ind - 1]
        if sum(window) == ans:
            return min(window) + max(window)

def check_sums(window, num):
    for num1 in window:
        for num2 in window:
            if (num1 != num2) and (num == num1 + num2):
                return True
    return False


if __name__ == "__main__":
    with open("Data/day9.txt", "r") as f:
        input_data = [int(line.strip('\n')) for line in f.readlines()]

    answer, index = sliding_window(input_data, 25)
    print("The solution to Part 1 is:", answer) # 507622668

    part2_data = input_data[:index]
    part2 = [x for x in (sliding_window_part2(part2_data, i, answer) for i in range(len(part2_data))) if x is not None]
    print("The solution to Part 2 is:", *part2) # 76688505
