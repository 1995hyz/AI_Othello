//
// Created by yingzhi on 11/1/19.
//

#ifndef AI_OTHELLO_BOARD_H
#define AI_OTHELLO_BOARD_H

#include <vector>

#define NUM_ROW 8
#define NUM_COLUMN 8

using namespace std;

class Board {
private:
    int board_array[NUM_ROW][NUM_COLUMN] = {
            {0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0}
    };
    vector<vector<int>> availability_white;
    vector<vector<int>> availability_black;
    int white_disc;
    int black_disc;
public:
    Board();
    Board(int *board_pointer);
    ~Board();

    bool place_disc(int row, int col, int disc_color, Board *board_temp);
    bool check_disc(int row, int col, int disc_color);
    void display_board();
    int *count_disc();
    vector<vector<int>> get_availability(int disc_color);
    void set_availability();
    int ending_test();
    int get_while_num();
    int get_black_num();
    void set_disc_num();
    int get_board_entry(int row, int col);
    void initializer();
    void set_board_entry(int row, int col, int disc_color);
};

#endif //AI_OTHELLO_BOARD_H
