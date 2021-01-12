#include <fstream>
#include "advent2020.h"

static const std::vector<advent_t> advent2020 = {
    { day01 }, { day02 }
};

static input_t load_input(const std::string &filename);
static void free_input(input_t &input);

int main(void) {
    for (int day = 1; day <= advent2020.size(); day++) {
        auto &A = advent2020[day - 1];
        if (!A.fn) continue;

        char filename[64];
        sprintf(filename, "Data/day%02d.txt", day);

        auto input = load_input(filename);
        auto output = A.fn(input);

        printf("Day %02d: %-16s %-16s\n",
                day, 
                output.answer[0].c_str(),
                output.answer[1].c_str());
    }
    return 0;
}

input_t load_input(const std::string &filename) {
    input_t in;
    std::ifstream file (filename.data(), std::ifstream::in);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            in.str += line;
        }
        in.len = in.str.length();
        file.close();
    }
    return in;
}