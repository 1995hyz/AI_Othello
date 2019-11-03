#include <iostream>
#include <vector>
#include "player.h"
#include "board-human.h"
#include "board-ai.h"

using namespace std;

int init_limit = 16;
int max_time = 5;

void print_legal_move(vector<vector<int>> available_move) {
    if (! available_move.empty()) {
        cout<<"The legal moves are:"<<endl;
        for (int i = 0; i < available_move.size(); i++) {
            cout<<"Move: " << "(" << available_move[i][0] << ", "<< available_move[i][1] << ")"<<endl;
        }
    } else {
        cout<<"No legal moves available."<<endl;
    }
}

void game_turn(Player *player1, Player *player2, Board *play_board) {
    int counter = 0;
    play_board->display_board();
    while(true) {
        vector<vector<int>> available_move = play_board->get_availability(player1->getColor());
        cout<<"Player1 to move."<<endl;
        print_legal_move(available_move);
        int row, col;
        float value;
        if(! available_move.empty()) {
            if (!player1->getType()) {
                auto *player_one = dynamic_cast<Human *>(player1);
                struct placement place = player_one->get_coordination(available_move);
                row = place.row;
                col = place.col;
                value = place.value;
            } else {
                auto *player_one = dynamic_cast<AI *>(player1);
                struct placement place = player_one->iterative_dls(play_board, init_limit, max_time);
                row = place.row;
                col = place.col;
                value = place.value;
                cout<<"Searching Time "<<endl;
                cout<<"Completed search on depth "<<endl;
                cout<<"The chosen move is (" << place.row << ", " << place.col << ")" << endl;
            }
            Board temp_board = Board();
            play_board->place_disc(row, col, player1->getColor(), play_board);
            //play_board = &temp_board;
            play_board->set_availability();
            play_board->set_disc_num();
            play_board->display_board();
            counter ++;
            if (counter == 60) {
                int result = play_board->ending_test();
                cout<<result<<endl;
                break;
            }
        }
        vector<vector<int>> available_move_2 = play_board->get_availability(player2->getColor());
        cout<<"Player2 to move."<<endl;
        print_legal_move(available_move_2);
        if(! available_move_2.empty()) {
            if (!player2->getType()) {
                auto *player_two = dynamic_cast<Human *>(player2);
                struct placement place = player_two->get_coordination(available_move_2);
                row = place.row;
                col = place.col;
                value = place.value;
            } else {
                auto *player_two = dynamic_cast<AI *>(player2);
                struct placement place = player_two->iterative_dls(play_board, init_limit, max_time);
                row = place.row;
                col = place.col;
                value = place.value;
                cout<<"Searching Time "<<endl;
                cout<<"Completed search on depth "<<endl;
                cout<<"The chosen move is (" << place.row << ", " << place.col << ")" << endl;
            }
            Board board_temp = Board();
            play_board->place_disc(row, col, player2->getColor(), play_board);
            //play_board = &board_temp;
            play_board->set_availability();
            play_board->set_disc_num();
            play_board->display_board();
            counter ++;
            if (counter == 60) {
                int result = play_board->ending_test();
                cout<<result<<endl;
                break;
            }
        }
    }
}

int main() {
    string select_1;
    string select_2;
    string history;
    cout<<"Will player1 be a computer? (Y/N)"<<endl;
    cin>>select_1;
    cout<<"Will player2 be a computer? (Y/N)"<<endl;
    cin>>select_2;
    cout<<"Do you want to load a board from a file? (Y/N)"<<endl;
    Player *player_1, *player_2;
    if (select_1 == "Y") {
        static AI player_ai = AI(1);
        player_1 = &player_ai;
    } else {
        static Human player_human = Human(1);
        player_1 = &player_human;
    }
    if (select_2 == "Y") {
        static AI player_ai = AI(-1);
        player_2 = &player_ai;
    } else {
        static Human player_human = Human(-1);
        player_2 = &player_human;
    }
    Board play_board = Board();
    play_board.initializer();
    game_turn(player_1, player_2, &play_board);
    return 0;
}