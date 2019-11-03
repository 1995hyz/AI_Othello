//
// Created by yingzhi on 11/2/19.
//

#ifndef AI_OTHELLO_BOARD_HUMAN_H
#define AI_OTHELLO_BOARD_HUMAN_H

#include "board.h"
#include "board-ai.h"
#include "player.h"
#include <vector>
#include <iostream>

using namespace std;

class Human : public Player{
private:
    ;

public:
    Human(int color);
    struct placement get_coordination(vector<vector<int>> available_move);
};

#endif //AI_OTHELLO_BOARD_HUMAN_H
