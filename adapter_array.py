# Advent of Code 2020
# Day 10: Adapter Array

if __name__ == "__main__":
    with open("Data/day10.txt", "r") as f:
        input_data = [line.rstrip('\n') for line in f.readlines()]
        adapters = [int(line) for line in input_data]

    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    jolt_diff = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]

    part1 = jolt_diff.count(1) * jolt_diff.count(3)
    print(jolt_diff.count(1), jolt_diff.count(3))
    print(part1)
