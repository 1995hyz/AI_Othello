//
// Created by yingzhi on 11/2/19.
//

#ifndef AI_OTHELLO_PLAYER_H
#define AI_OTHELLO_PLAYER_H

class Player {
private:
    bool type;
    int color;
public:
    Player(int color);
    virtual ~Player() = default;
    void setType(bool player_type);
    bool getType();
    void setColor(int player_color);
    int getColor();
};

#endif //AI_OTHELLO_PLAYER_H
