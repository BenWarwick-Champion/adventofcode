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

        std::string filename = "../Data/day" + std::to_string(day) + ".txt";

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
    std::ifstream file (filename.c_str(), std::ifstream::in);
    if (file.is_open()) {
        file.seekg(0, file.end);
        in.len = file.tellg();
        file.seekg(0, file.beg);

        char* buffer = new char[in.len];
        file.read(buffer, in.len);

        if(file)
        {
            std::cout << "All chars read successfully" << std::endl;
        }
        else
        {
            std::cout << "Error: Only " << file.gcount() << " could be read";
        }
        file.close();
        in.str = buffer;
    }
    return in;
}