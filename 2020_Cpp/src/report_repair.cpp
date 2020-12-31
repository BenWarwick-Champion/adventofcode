#include "../utils/utils.h"

#include <iostream>
#include <string>


int main(void)
{
    auto data = utils::open_puzzle_input(1);
    char c = data.get();
    while (data.good()) {
        std::cout << c;
        c = data.get();
    }
    data.close();
    std::cout << std::endl << "EoF" << std::endl;
    return 0;
}
