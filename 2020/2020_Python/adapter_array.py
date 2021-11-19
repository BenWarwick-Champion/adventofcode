# Advent of Code 2020
# Day 10: Adapter Array

# Returns permutations from adapter[i]
def permutations_from(i):
    if i == len(adapters) - 1:
        return 1 # base case
    if i in memory:
        return memory[i] # avoid recalculation

    ans = 0
    for j in range(i+1, len(adapters)):
        if adapters[j] - adapters[i] <= 3:
            ans += permutations_from(j)
    memory[i] = ans
    return ans

if __name__ == "__main__":
    with open("Data/day10.txt", "r") as f:
        input_data = [line.rstrip('\n') for line in f.readlines()]
        adapters = [int(line) for line in input_data]

    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    jolt_diff = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]

    part1 = jolt_diff.count(1) * jolt_diff.count(3)
    print("Part 1 solution:", part1)

    memory = {}
    part2 = permutations_from(0)
    print("Part 2 solution:", part2)
