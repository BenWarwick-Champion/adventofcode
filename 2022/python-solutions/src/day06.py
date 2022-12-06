# Advent of Code 2022
# Day 06

def find_marker(buffer, window=4):
    for i in range(len(buffer)):
        if i < 2:
            continue
        marker = set(buffer[i-window:i])
        if len(marker) == window:
            return i
    return 0


if __name__ == "__main__":
    with open("input/day06.txt") as f:
        data = f.read().strip()

    print('---- Part One ----')
    print(find_marker(data))  # 1655

    print('---- Part Two ----')
    print(find_marker(data, 14))  # 2665
