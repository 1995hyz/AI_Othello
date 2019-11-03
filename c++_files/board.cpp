//
// Created by yingzhi on 11/1/19.
//

#include "board.h"
#include "stdio.h"
#include <vector>
#include <iostream>

using namespace std;

Board::Board(int *board_pointer) {
    for ( int i=0; i < NUM_ROW; i++) {
        for ( int j=0; j < NUM_COLUMN; j++) {
            board_array[i][j] = *board_pointer;
            board_pointer ++;
        }
    }
    set_availability();
    set_disc_num();
}

Board::Board() {
    /*for (int i=0; i < NUM_ROW; i++) {
        for (int j = 0; j < NUM_COLUMN; j++) {
            board_array[i][j] = 0;
        }
    }*/
    /*
    board_array[3][3] = -1;
    board_array[4][4] = -1;
    board_array[3][4] = 1;
    board_array[4][3] = 1;
    */
}

Board::~Board() {
}

bool Board::place_disc(int row, int col, int color, Board *board_temp) {
    if (!(8 > row && row >= 0 && 8 > col && col >= 0 && ( color == 1 || color == -1))) {
        return false;
    }
    if (board_array[row][col] != 0) {
        return false;
    }
    /*int row_n[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector <int>> row_n;
    for (int i = row - 1; i >= 0; i--) {
        // row_n[i][0] = i;
        // row_n[i][1] = col;
        vector<int> temp {i, col};
        row_n.push_back(temp);
    }
    /*int row_nw[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector <int>> row_nw;
    for (int i = 0; i < 8; i++) {
        int r_temp = row - i - 1;
        int c_temp = col - i - 1;
        if ( r_temp < 7 || c_temp < 0) {
            break;
        }
        //row_nw[i][0] = r_temp;
        //row_nw[i][1] = c_temp;
        vector<int> temp {r_temp, c_temp};
        row_nw.push_back(temp);
    }
    /*int row_ne[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_ne;
    for (int i = 0; i < 8; i++) {
        int r_temp = row - i - 1;
        int c_temp = col + i + 1;
        if ( r_temp < 0 || c_temp > 7) {
            break;
        }
        //row_ne[i][0] = r_temp;
        //row_ne[i][1] = c_temp;
        vector<int> temp {r_temp, c_temp};
        row_ne.push_back(temp);
    }
    /*int row_w[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_w;
    for (int i = col-1; i >= 0; i--) {
        //row_w[i][0] = row;
        //row_w[i][1] = i;
        vector<int> temp {row, i};
        row_w.push_back(temp);
    }
    /*int row_e[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_e;
    for (int i = 0; i < 7 - col; i++) {
        //row_e[i][0] = row;
        //row_e[i][1] = col + 1 + i;
        vector<int> temp {row, col+1+i};
        row_e.push_back(temp);
    }
    /*int row_s[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_s;
    for (int i = 0; i < 7 - row ; i++) {
        //row_s[i][0] = row + 1 + i;
        //row_s[i][1] = col;
        vector<int> temp { row+1+i, col};
        row_s.push_back(temp);
    }
    /*int row_sw[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_sw;
    for (int i = 0; i < 8; i++) {
        int row_temp = row + 1 + i;
        int col_temp = col - 1 + i;
        if ( row_temp > 7 || col_temp < 0) {
            break;
        }
        //row_sw[i][0] = row_temp;
        //row_sw[i][1] = col_temp;
        vector<int> temp {row_temp, col_temp};
        row_sw.push_back(temp);
    }
    /*int row_se[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_se;
    for (int i = 0; i < 8; i++) {
        int row_temp = row + 1 + i;
        int col_temp = col + 1 + i;
        if ( row_temp > 7 || col_temp > 7) {
            break;
        }
        //row_se[i][0] = row_temp;
        //row_se[i][0] = col_temp;
        vector<int> temp {row_temp, col_temp};
        row_se.push_back(temp);
    }
    vector<vector<vector<int>>> directions {
        row_n, row_nw, row_ne, row_w,
        row_e, row_s, row_sw, row_se
    };
    /*int *direction[8] = {
            &row_n[0][0], &row_nw[0][0], &row_ne[0][0], &row_w[0][0],
            &row_e[0][0], &row_s[0][0], &row_sw[0][0], &row_se[0][0]
    };*/
    int *board_curr = &board_array[0][0];
    // int board_temp[NUM_ROW][NUM_COLUMN];
    for ( int i=0; i < NUM_ROW; i++) {
        for ( int j=0; j < NUM_COLUMN; j++) {
            board_temp->board_array[i][j] = *board_curr;
            board_curr ++;
        }
    }
    bool flipped = false;
    for( int i = 0; i < 8; i++) {
        int count = 0;
        vector<vector<int>> direction = directions[i];
        for(int j = 0; j < direction.size(); j++) {
            //int row_num = *(direction[i] + 2 * j);
            //int col_num = *(direction[i] + 1 + 2 * j);
            int row_num = direction[j][0];
            int col_num = direction[j][1];
            if (board_array[row_num][col_num] == -1*color) {
                count ++;
            }
            else if (board_array[row_num][col_num] == color) {
                break;
            }
            else {
                count = 0;
                break;
            }
        }
        if (count == direction.size()) {
            count = 0;
        }
        if (count > 0) {
            flipped = true;
        }
        for ( int j = 0; j < count; j++) {
            int row_num = direction[j][0];
            int col_num = direction[j][1];
            board_temp->board_array[row_num][col_num] = color;
        }
    }
    if (flipped) {
        board_temp->board_array[row][col] = color;
        return true;
    }
    else {
        return false;
    }
}

bool Board::check_disc(int row, int col, int color) {
    if (!(8 > row && row >= 0 && 8 > col && col >= 0 && ( color == 1 || color == -1))) {
        return false;
    }
    if (board_array[row][col] != 0) {
        return false;
    }
    /*int row_n[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector <int>> row_n;
    for (int i = row - 1; i >= 0; i--) {
        // row_n[i][0] = i;
        // row_n[i][1] = col;
        vector<int> temp {i, col};
        row_n.push_back(temp);
    }
    /*int row_nw[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector <int>> row_nw;
    for (int i = 0; i < 8; i++) {
        int r_temp = row - i - 1;
        int c_temp = col - i - 1;
        if ( r_temp < 0 || c_temp < 0) {
            break;
        }
        //row_nw[i][0] = r_temp;
        //row_nw[i][1] = c_temp;
        vector<int> temp {r_temp, c_temp};
        row_nw.push_back(temp);
    }
    /*int row_ne[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_ne;
    for (int i = 0; i < 8; i++) {
        int r_temp = row - i - 1;
        int c_temp = col + i + 1;
        if ( r_temp < 0 || c_temp > 7) {
            break;
        }
        //row_ne[i][0] = r_temp;
        //row_ne[i][1] = c_temp;
        vector<int> temp {r_temp, c_temp};
        row_ne.push_back(temp);
    }
    /*int row_w[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_w;
    for (int i = col - 1; i >= 0; i--) {
        //row_w[i][0] = row;
        //row_w[i][1] = i;
        vector<int> temp {row, i};
        row_w.push_back(temp);
    }
    /*int row_e[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_e;
    for (int i = 0; i < 7 - col; i++) {
        //row_e[i][0] = row;
        //row_e[i][1] = col + 1 + i;
        vector<int> temp {row, col+1+i};
        row_e.push_back(temp);
    }
    /*int row_s[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_s;
    for (int i = 0; i < 7 - row ; i++) {
        //row_s[i][0] = row + 1 + i;
        //row_s[i][1] = col;
        vector<int> temp { row+1+i, col};
        row_s.push_back(temp);
    }
    /*int row_sw[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_sw;
    for (int i = 0; i < 8; i++) {
        int row_temp = row + 1 + i;
        int col_temp = col - 1 - i;
        if ( row_temp > 7 || col_temp < 0) {
            break;
        }
        //row_sw[i][0] = row_temp;
        //row_sw[i][1] = col_temp;
        vector<int> temp {row_temp, col_temp};
        row_sw.push_back(temp);
    }
    /*int row_se[8][2] = {
            {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}, {-1, -1}
    };*/
    vector<vector<int>> row_se;
    for (int i = 0; i < 8; i++) {
        int row_temp = row + 1 + i;
        int col_temp = col + 1 + i;
        if ( row_temp > 7 || col_temp > 7) {
            break;
        }
        //row_se[i][0] = row_temp;
        //row_se[i][0] = col_temp;
        vector<int> temp {row_temp, col_temp};
        row_se.push_back(temp);
    }
    vector<vector<vector<int>>> directions {
            row_n, row_nw, row_ne, row_w,
            row_e, row_s, row_sw, row_se
    };
    /*int *direction[8] = {
            &row_n[0][0], &row_nw[0][0], &row_ne[0][0], &row_w[0][0],
            &row_e[0][0], &row_s[0][0], &row_sw[0][0], &row_se[0][0]
    };*/
    for( int i = 0; i < 8; i++) {
        int count = 0;
        vector<vector<int>> direction = directions[i];
        for(int j = 0; j < direction.size(); j++) {
            //int row_num = *(direction[i] + 2 * j);
            //int col_num = *(direction[i] + 1 + 2 * j);
            int row_num = direction[j][0];
            int col_num = direction[j][1];
            if (board_array[row_num][col_num] == -1*color) {
                count ++;
            }
            else if (board_array[row_num][col_num] == color) {
                break;
            }
            else {
                count = 0;
                break;
            }
        }
        if (count == direction.size()) {
            count = 0;
        }
        if (count > 0) {
            return true;
        }
    }
    return false;
}

void Board::display_board() {
    cout<<"Current Board:"<<endl;
    cout<<"Player 1 is %"<<endl;
    cout<<"Player 2 is $\n"<<endl;
    cout<<"   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 "<<endl;
    for (int i = 0; i < 8; i++) {
        cout<<"----------------------------------"<<endl;
        cout<<"     |   |   |   |   |   |   |   "<<endl;
        cout<<i<<" ";
        for(int j = 0; j < 7; j++) {
            if(board_array[i][j] == 1){
                cout<<" % ";
            } else if (board_array[i][j] == -1){
                cout<< " $ ";
            } else {
                cout<<"   ";
            }
            cout<<"|";
        }
        if(board_array[i][7] == 1) {
            cout << " % " << endl;
        } else if (board_array[i][7] == -1) {
            cout << " $ " <<endl;
        } else {
            cout << "   "<<endl;
        }
        cout<<"     |   |   |   |   |   |   |   "<<endl;
    }
    cout<<"----------------------------------"<<endl;
}

int * Board::count_disc() {
    static int disc_counter[2] = {0, 0};
    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            if (board_array[i][j] == 1) {
                disc_counter[0] ++;
            } else if (board_array[i][j] == -1) {
                disc_counter[1] ++;
            }
        }
    }
    return &disc_counter[0];
}

vector<vector<int>> Board::get_availability(int disc_color) {
    if (disc_color == 1) {
        return availability_white;
    } else {
        return availability_black;
    }
}

void Board::set_availability() {
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (board_array[i][j] == 0) {
                bool test_board_white = check_disc(i, j, 1);
                bool test_board_black = check_disc(i, j, -1);

                bool test_board_white2 = check_disc(4, 5, 1);

                if (test_board_white) {
                    vector <int> avail_while { i, j };
                    availability_white.push_back(avail_while);
                }
                if (test_board_black) {
                    vector <int> avail_black { i, j };
                    availability_black.push_back(avail_black);
                }
            }
        }
    }
}

void Board::set_disc_num() {
    int white_num = 0;
    int black_num = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (board_array[i][j] == 1) {
                white_num ++;
            } else if (board_array[i][j] == -1) {
                black_num ++;
            }
        }
    }
    white_disc = white_num;
    black_disc = black_num;
}

int Board::get_black_num() {
    return white_disc;
}

int Board::get_while_num() {
    return black_disc;
}

int Board::ending_test() {
    int white_num = get_while_num();
    int black_num = get_black_num();
    if ((white_num + black_num) == 64) {
        if (white_num >= black_num) {
            return 1;
        } else {
            return -1;
        }
    } else {
        return 0;
    }
}

int Board::get_board_entry(int row, int col) {
    return board_array[row][col];
}

void Board::set_board_entry(int row, int col, int disc_color) {
    board_array[row][col] = disc_color;
}

void Board::initializer() {
    set_board_entry(3, 3, -1);
    set_board_entry(4, 4, -1);
    set_board_entry(3, 4, 1);
    set_board_entry(4, 3, 1);
    set_availability();
    set_disc_num();
}