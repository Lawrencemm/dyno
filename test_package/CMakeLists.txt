cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(dyno REQUIRED)

add_executable(test_executable test_main.cpp)
target_link_libraries(test_executable dyno::dyno)
