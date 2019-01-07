# AI_Othello
This project is an Othello (Reversi) game.
# (1). Run the Game
The game is designed to run under python 3.6 or later version.
To run the game, run module game.py with command: python game.py (Or python3 game.py  if both python2 and python3 are on the computer)
# (2). Software Architecture of the Game
The game is consisted of four modules, game.py, board.py, board_ai.py and board_gui.py
game.py is for runing the game. board.py provides functionalities of how the Othello board works. board_ai.py provides functionalities of an AI that plays as the opponent of the human player. board_gui.py generates a graphic display of the game.
# (3). AI Mechanism
Every turn, the AI will search for a solution with iterative depth-limited-search algorithm. Maximum searching time is capped at approximately 10 seconds. Alpha-beta pruning is used to improve the searching efficiency. 
