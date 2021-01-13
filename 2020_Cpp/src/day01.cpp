#include "advent2020.h"

// Day 1: Report Repair

output_t day01(input_t in) {
    int part1 = 0, part2 = 0;
    auto numbers = parse::str_to_vec(in);

    // Add all numbers to an unordered set for faster lookup
    std::unordered_set<int> set;
    for (int i = 0; i < numbers.size(); i++) {
        set.insert(numbers[i]);
    }

    // Sort the vector to take advantage of the unbalanced input
    std::sort(numbers.begin(), numbers.end());

    // Part 1 - using ranges
    for (auto num : numbers) {
        auto res = 2020 - num;
        if (set.find(res) != set.end()) {
            part1 = num * res;
            break;
        }
    }

    // Part 2 - using ranges
    for (auto x : numbers) {
        if (part2 != 0)
            break;
        auto test = 2020 - x;
        for (auto y : numbers) {
            auto z = test - y;
            if (set.find(z) != set.end()) {
                part2 = x * y * z;
                break;
            }
        }
    }

    return { part1, part2 };
}
