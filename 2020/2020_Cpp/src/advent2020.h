#pragma once

#include <string>
#include <vector>
#include <array>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <sstream>
#include <iostream>

struct input_t {
    std::string str;
    ssize_t len;
};

struct output_t {
    std::array<std::string, 2> answer;

    template<typename T1, typename T2>
    output_t(T1 p1, T2 p2) {
        set(0, p1);
        set(1, p2);
    }

    template<typename T>
    void set(int part, T value) {
        std::stringstream ss;
        ss << value;
        answer[part] = ss.str();
    }
};

struct advent_t {
    output_t (*fn)(input_t);
};

output_t day01(input_t);
output_t day02(input_t);

#include "utils.h"
