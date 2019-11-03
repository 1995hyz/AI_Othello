cmake_minimum_required(VERSION 3.15)
project(AI_Othello)

set(CMAKE_CXX_STANDARD 11)

add_executable(AI_Othello main.cpp board.cpp board.h board-ai.cpp board-ai.h board-human.cpp board-human.h player.cpp player.h)