//
// Created by yingzhi on 11/2/19.
//

#ifndef AI_OTHELLO_BOARD_AI_H
#define AI_OTHELLO_BOARD_AI_H

#include "board.h"
#include "player.h"

using namespace std;

class AI : public Player{
private:
    int position_weight[NUM_ROW][NUM_COLUMN] = {
            {4, -3, 2, 2, 2, 2, -3, 4},
            {-3, -4, -1, -1, -1, -1, -4, -3},
            {2, -1, 1, 0, 0, 1, -1, 2},
            {2, -1, 0, 1, 1, 0, -1, 2},
            {2, -1, 0, 1, 1, 0, -1, 2},
            {2, -1, 1, 0, 0, 1, -1, 2},
            {-3, -4, -1, -1, -1, -1, -4, -3},
            {4, -3, 2, 2, 2, 2, -3, 4}
    };
    int index[2];
public:
    AI(int color);
    float evaluation(Board *a_board);
    struct placement max_value(Board *current_board, float alpha, float beta, int limit);
    struct placement min_value(Board *current_board, float alpha, float beta, int limit);
    struct placement alpha_beta_search(Board *current_board, int limit);
    struct placement iterative_dls(Board *current_board, int init_limit, int max_time);
};

struct placement {
    int row;
    int col;
    float value;
};

#endif //AI_OTHELLO_BOARD_AI_H
