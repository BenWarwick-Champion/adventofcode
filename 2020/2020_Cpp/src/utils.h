#pragma once

namespace parse {

    // String to Vector<int>
    static std::vector<int> str_to_vec(input_t in) {
        std::stringstream iss(in.str);

        int number;
        std::vector<int> vec;
        while (iss >> number) {
            vec.push_back(number);
        }
        return vec;
    }

}

namespace display {

    // Print Vector<int>
    static void print_vec(std::vector<int> vec) {
        std::copy(vec.begin(), vec.end(), std::ostream_iterator<int>(std::cout, " "));
        std::cout << std::endl;
    }

}
