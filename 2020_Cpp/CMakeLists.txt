cmake_minimum_required (VERSION 3.10)
project (advent2020)

set(CMAKE_BUILD_TYPE debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native -std=c++17")

set(CMAKE_C_COMPILER "clang" CACHE STRING "clang compiler" FORCE)
set(CMAKE_CXX_COMPILER "clang++" CACHE STRING "clang++ compiler" FORCE)

add_executable(advent2020
	src/main.cpp
	src/day01.cpp
	src/day02.cpp
	)
target_link_libraries(advent2020 m)