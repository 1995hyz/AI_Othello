import tkinter as tk
import game
import time


class GameBoard:

    def __init__(self, rows=8, columns=8, gui_sock=None):
        self.rows = rows
        self.columns = columns
        self.grid = []
        for i in range(8):
            self.grid.append([0]*8)
        self.grid[3][3] = 1
        self.grid[3][4] = -1
        self.grid[4][3] = -1
        self.grid[4][4] = 1


        """
        def click(coordinate):
            user_board = [-3]
            index = coordinate[0] * 8 + coordinate[1]
            ending_flag = True
            white_win = False
            black_win = False
            if buttons[index][1] == 0:
                gui_sock.send(coordinate)
                user_board = gui_sock.recv()
            else:
                print('Error: Over-claiming Entry')
                return False
            if user_board[0] == -4:
                white_win = True
                user_board = gui_sock.recv()
            elif user_board[0] == -5:
                black_win = True
                user_board = gui_sock.recv()
            if user_board[0] != -3:
                for index in range(len(user_board)):
                    if user_board[index] == 1:
                        buttons[index][0].config(bg='white')
                        buttons[index][1] = 1
                    elif user_board[index] == -1:
                        buttons[index][0].config(bg='black')
                        buttons[index][1] = 1
                    else:
                        ending_flag = False
            else:
                print('Error: Invalid Placement')
            if black_win or white_win:
                ending_flag = True
            if ending_flag and user_board[0] != -3:
                if white_win:
                    winner.config(text='Winner is the user!')
                elif black_win:
                    winner.config(text='Winner is the AI!')
                else:
                    white_counter = 0
                    black_counter = 0
                    for index in range(len(user_board)):
                        if user_board[index] == 1:
                            white_counter = white_counter + 1
                        if user_board[index] == -1:
                            black_counter = black_counter + 1
                    if white_counter >= black_counter:
                        winner.config(text='Winner is the user!')
                    else:
                        winner.config(text='Winner is the AI!')
                for key in buttons:
                    buttons[key][1] = 1     # Winner has been generated. Terminate all buttons.
                return True
                """


def run_gui(gui_sock=None):
    board = GameBoard()
    board.print_board()
    # gui_sock.send((-2, -2))
    # gui_sock.close()


if __name__ == "__main__":
    run_gui()
