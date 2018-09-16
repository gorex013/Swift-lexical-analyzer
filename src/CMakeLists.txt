cmake_minimum_required(VERSION 3.12)
project(Swift_Lexical_Analyzer)

set(CMAKE_CXX_STANDARD 17)

add_executable(Source main_source.cpp VariableDeclaration/VariableDeclaration.cpp)