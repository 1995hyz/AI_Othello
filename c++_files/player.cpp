//
// Created by yingzhi on 11/2/19.
//

#include "player.h"

Player::Player(int color) {
    setColor(color);
}

void Player::setType(bool player_type) {
    this->type = player_type; // True means that the player is an AI. False means that the player is a human.
}

bool Player::getType() {
    return type;
}

void Player::setColor(int player_color) {
    this->color = player_color;
}

int Player::getColor() {
    return color;
}