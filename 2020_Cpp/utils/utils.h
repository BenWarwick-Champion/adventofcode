#pragma once

#include <fstream>
#include <sstream>
#include <cassert>

namespace utils
{
    inline std::ifstream open_puzzle_input(int day)
    {
        std::ostringstream name;
        name << "Data/day" << day << ".txt";
        auto result = std::ifstream{ name.str() };
        assert(result.is_open());
        return result;
    }
} // namespace utils
