# AoC2020 - C++

[Advent of Code 2020](https://adventofcode.com/2020/) C++ solutions.

I have previously only used C for a university project a number of years ago so I am attempting AoC in C++ to learn the language.

## Objectives
I have a few goals:
 - Solutions should actually use C++. I will try and avoid defaulting to standard C.
 - Solutions should run faster than my Python solutions. After all, why go to the extra effort if I'm not getting anything from it.
 - Solutions should be portable. This was a massive pain back when doing that uni project, there always seemed to be issues when moving between my PC and the lab computers so I want to make sure I can write something that just works.

## Notes to self
### Building the project
1. Navigate to ~/AoC2020/2020_Cpp
2. `cmake .`
3. `cmake --build .`
4. `./advent2020`

### References
 - [u/askalski on Reddit](https://www.reddit.com/r/adventofcode/comments/kkq6r3/2020_optimized_solutions_in_c_291_ms_total/)
 - [CMake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)

 ### Daily Notes
 #### Day 1
  - Remember to build for release when testing performance.
  - Remember to exit ALL loops when the result is found.
 