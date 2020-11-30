cmake_minimum_required(VERSION 2.8)
project(large_package CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(large_package large_package.cpp)
