cmake_minimum_required(VERSION 3.0.0)
project(advent2020 VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(advent2020 
    src/main.cpp
    src/day01.cpp
    src/day02.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
