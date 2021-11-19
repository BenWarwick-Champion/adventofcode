#include <fstream>
#include <chrono>
#include "advent2020.h"

static const std::vector<advent_t> advent2020 = {
    { day01 }, { day02 }
};

static input_t load_input(const std::string &filename);
static void free_input(input_t &input);

int main(void) {

    double total_time = 0;

    printf("          Time         Part 1           Part 2\n");
	printf("========================================================\n");
    for (int day = 1; day <= advent2020.size(); day++) {
        auto &A = advent2020[day - 1];
        if (!A.fn) continue;

        std::string filename = "../Data/day" + std::to_string(day) + ".txt";

        auto input = load_input(filename);

        auto t0 = std::chrono::steady_clock::now();
        auto output = A.fn(input);
        auto elapsed = std::chrono::steady_clock::now() - t0;

        double t = 1e-3 * std::chrono::duration_cast<std::chrono::nanoseconds>(elapsed).count();
        total_time += t;

        printf("Day %02d: %7.f μs     %-16s %-16s\n",
                day,
                t, 
                output.answer[0].c_str(),
                output.answer[1].c_str());
    }
    printf("========================================================\n");
	printf("Total:  %7.f μs\n", total_time);

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

        if(!file)
        {
            std::cout << "Error: Only " << file.gcount() << " could be read";
        }
        
        file.close();
        in.str = buffer;
    } else {
        std::cout << "Error reading file. You may need to run 'cd build'" << std::endl;
    }
    return in;
}