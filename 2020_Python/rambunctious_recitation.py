# Advent of Code 2020
# Day 15: Rambunctious Recitation

# [0, 14, 1, 3, 7, 9]
# {0:0, 14:1, 1:2, 3:3, 7:4, 9:5}
# {3:0, 1:1, 2:2}

def g_num(number):
    n = 0
    last_n = 9
    seen = {0:0, 14:1, 1:2, 3:3, 7:4, 9:5}
    for i in range(6, number-1):
        if n in seen:
            last_n = n
            n = i - seen[n]
            seen[last_n] = i
            yield n
        else:
            last_n = n
            n = 0
            seen[last_n] = i
            yield n

if __name__ == "__main__":
    
    part1, part2 = 0, 0
    for i in g_num(2020):
        part1 = i
    print("Part 1 solution:", part1)
    
    for i in g_num(30000000):
        part2 = i
    print("Part 2 solution:", part2)