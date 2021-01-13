#include "advent2020.h"

output_t day01(input_t in) {
    int part1 = 0, part2 = 0;

    auto numbers = parse::str_to_vec(in);
    display::print_vec(numbers);

    std::unordered_set<int> set;

    for (int i = 0; i < numbers.size(); i++) {
        set.insert(numbers[i]);
    }

    for (int i = 0; i < numbers.size(); i++) {
        int res = 2020 - numbers[i];
        if (set.find(res) != set.end()) {
            part1 = numbers[i] * res;
            break;
        }
    }

    return { part1, part2 };
}
