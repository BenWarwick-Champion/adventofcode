# Advent of Code 2020
# Day 6: Custom Customs (Attempt 2)
# This was done with help from the r/adventofcode subreddit
# Depressingly compact in comparison to my own attempt

if __name__ == "__main__":
    with open("Data/day6.txt", "r") as f:
        groups = f.read().strip().split('\n\n')

    part1 = sum(len(set.union(*map(set, g.split('\n')))) for g in groups)
    part2 = sum(len(set.intersection(*map(set, g.split('\n')))) for g in groups)

    print("Solution to Part 1 is:", part1) #6703
    print("Solution to Part 2 is:", part2) #3430
