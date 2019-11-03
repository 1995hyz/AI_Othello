//
// Created by yingzhi on 11/2/19.
//

#include "board-human.h"

Human::Human(int color) : Player(color) {
    setType(false);
}

struct placement Human::get_coordination(vector<vector<int>> available_move) {
    while (true) {
        int row;
        int col;
        cout<<"Enter row of the move (0-7): ";
        cin>>row;
        cout<<"Enter column of move (0-7): ";
        cin>>col;
        for (int i = 0; i < available_move.size(); i++) {
            if (available_move[i][0] == row) {
                if(available_move[i][1] == col) {
                    struct placement newReturn = {row, col, 0};
                    return newReturn;
                }
            }
        }
        cout<<"(" << row << ", " << col << ")" << " is not a legal move."<<endl;
    }
}