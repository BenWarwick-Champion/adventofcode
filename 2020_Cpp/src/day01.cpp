#include "advent2020.h"

output_t day01(input_t in) {
    int part1 = 0, part2 = 0;
    auto numbers = parse::str_to_vec(in);

    // Add all numbers to an unordered set for faster lookup
    std::unordered_set<int> set;
    for (int i = 0; i < numbers.size(); i++) {
        set.insert(numbers[i]);
    }

    // Part 1
    for (int i = 0; i < numbers.size(); i++) {
        int res = 2020 - numbers[i];
        if (set.find(res) != set.end()) {
            part1 = numbers[i] * res;
            break;
        }
    }

    // Part 2
    for (int i = 0; i < numbers.size(); i++) {
        int test = 2020 - numbers[i];
        for (int j = 0; j < numbers.size(); j++) {
            int res = test - numbers[j];
            if (set.find(res) != set.end()) {
                part2 = numbers[j] * numbers[i] * res;
                break;
            }
        }
    }

    return { part1, part2 };
}
