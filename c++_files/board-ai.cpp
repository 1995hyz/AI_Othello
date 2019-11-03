//
// Created by yingzhi on 11/2/19.
//

#include "board-ai.h"
#include <chrono>
#include <iostream>
#include <algorithm>
#include <cmath>

AI::AI(int color) : Player(color) {
    setType(true);
    if (getColor() == 1) {
        this->index[0] = 0;
        this->index[1] = 1;
    } else {
        this->index[0] = 1;
        this->index[1] = 0;
    }
}

float AI::evaluation(Board *a_board) {
    int max_sum = 0;
    int white_num = a_board->get_while_num();
    int black_num = a_board->get_black_num();
    int disc[2] = {white_num, black_num};
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            int color_disc = a_board->get_board_entry(i, j);
            if (color_disc == getColor()) {
                max_sum += position_weight[i][j];
            } else if (color_disc == (getColor() * -1)) {
                max_sum -= position_weight[i][j];
            }
        }
    }
    if ((white_num + black_num) < 40) {
        return float((max_sum + (disc[index[0]] - disc[index[1]]) * 0.1) * 0.1);
    } else {
        return float((max_sum + (disc[index[0]] - disc[index[1]]) * 0.15) * 0.1);
    }
}

struct placement AI::max_value(Board *current_board, float alpha, float beta, int limit) {
    int color = getColor();
    int result = current_board->ending_test();
    if (result == -1) {
        struct placement newReturn = {-1, -1, 100};
        return newReturn;
    } else if (result == 1) {
        struct placement newReturn = {-1, -1, -100};
        return newReturn;
    }
    if (limit == 0) {
        float value = evaluation(current_board);
        struct placement newReturn = {-1, -1, value};
        return newReturn;
    }
    float value = -100;
    int row = -1;
    int col = -1;
    vector<vector<int>> blank_space = current_board->get_availability(color);
    for (int i = 0; i < blank_space.size(); i++) {
        int r = blank_space[i][0];
        int c = blank_space[i][1];
        Board board_temp = Board();
        bool new_board = current_board->place_disc(r, c, color, &board_temp);
        if (! new_board) {
            continue;
        } else {
            struct placement newReturn = min_value(&board_temp, alpha, beta, limit-1);
            if (newReturn.value >= value) {
                value = newReturn.value;
                row = r;
                col = c;
            }
            if (newReturn.value >= beta) {
                struct placement newReturn2 = {row, col, value};
                return newReturn2;
            }
            alpha = max(newReturn.value, alpha);
        }
    }
    struct placement newReturn = {row, col, value};
    return newReturn;
}

struct placement AI::min_value(Board *current_board, float alpha, float beta, int limit) {
    int color = getColor();
    int result = current_board->ending_test();
    if (result == -1) {
        struct placement newReturn = {-1, -1, 100};
        return newReturn;
    } else if (result == 1) {
        struct placement newReturn = {-1, -1, -100};
        return newReturn;
    }
    if (limit == 0) {
        float value = evaluation(current_board);
        struct placement newReturn = {-1, -1, value};
        return newReturn;
    }
    float value = 100;
    int row = -1;
    int col = -1;
    vector<vector<int>> blank_space = current_board->get_availability(color * -1);
    for (int i = 0; i < blank_space.size(); i++) {
        int r = blank_space[i][0];
        int c = blank_space[i][1];
        Board board_temp = Board();
        bool new_board = current_board->place_disc(r, c, color * -1, &board_temp);
        if (! new_board) {
            continue;
        } else {
            struct placement newReturn = max_value(&board_temp, alpha, beta, limit-1);
            if (newReturn.value <= value) {
                value = newReturn.value;
                row = r;
                col = c;
            }
            if (newReturn.value <= alpha) {
                struct placement newReturn2 = {row, col, value};
                return newReturn2;
            }
            beta = min(newReturn.value, beta);
        }
    }
    struct placement newReturn = {row, col, value};
    return newReturn;
}

struct placement AI::alpha_beta_search(Board *current_board, int limit) {
    struct placement newReturn = max_value(current_board, -100, 100, limit);
    return newReturn;
}

struct placement AI::iterative_dls(Board *current_board, int init_limit, int max_time) {
    int limit = init_limit;
    auto start = chrono::high_resolution_clock::now();
    while (true) {
        struct placement newReturn = alpha_beta_search(current_board, limit);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
        cout<<"***Search Time: "<<duration.count()<<endl;
        cout<<"***Limit: "<<limit<<endl;
        if (max_time * 5000 / pow(2, (limit - 2)) > duration.count()) {
            limit = limit + 2;
            continue;
        } else {
            return newReturn;
        }
    }
}