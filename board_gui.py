import tkinter as tk
import game
import time


class GameBoard(tk.Frame):

    def __init__(self, parent, rows=8, columns=8, gui_sock=None):
        self.rows = rows
        self.columns = columns
        tk.Frame.__init__(self, parent)
        buttons = {}
        winner = tk.Label(parent, text='', font='Helvetica 12 bold', height=3, width=20)
        winner.grid(row=8, column=0, columnspan=8)
        A0 = tk.Button(parent, height=3, width=8, command=lambda: click((0, 0)), bg="DodgerBlue2", anchor="sw")
        A1 = tk.Button(parent, height=3, width=8, command=lambda: click((0, 1)), bg="DodgerBlue3", anchor="sw")
        A2 = tk.Button(parent, height=3, width=8, command=lambda: click((0, 2)), bg="DodgerBlue2", anchor="sw")
        A3 = tk.Button(parent, height=3, width=8, command=lambda: click((0, 3)), bg="DodgerBlue3", anchor="sw")
        A4 = tk.Button(parent, height=3, width=8, command=lambda: click((0, 4)), bg="DodgerBlue2", anchor="sw")
        A5 = tk.Button(parent, height=3, width=8, command=lambda: click((0, 5)), bg="DodgerBlue3", anchor="sw")
        A6 = tk.Button(parent, height=3, width=8, command=lambda: click((0, 6)), bg="DodgerBlue2", anchor="sw")
        A7 = tk.Button(parent, height=3, width=8, command=lambda: click((0, 7)), bg="DodgerBlue3", anchor="sw")
        B0 = tk.Button(parent, height=3, width=8, command=lambda: click((1, 0)), bg="DodgerBlue3", anchor="sw")
        B1 = tk.Button(parent, height=3, width=8, command=lambda: click((1, 1)), bg="DodgerBlue2", anchor="sw")
        B2 = tk.Button(parent, height=3, width=8, command=lambda: click((1, 2)), bg="DodgerBlue3", anchor="sw")
        B3 = tk.Button(parent, height=3, width=8, command=lambda: click((1, 3)), bg="DodgerBlue2", anchor="sw")
        B4 = tk.Button(parent, height=3, width=8, command=lambda: click((1, 4)), bg="DodgerBlue3", anchor="sw")
        B5 = tk.Button(parent, height=3, width=8, command=lambda: click((1, 5)), bg="DodgerBlue2", anchor="sw")
        B6 = tk.Button(parent, height=3, width=8, command=lambda: click((1, 6)), bg="DodgerBlue3", anchor="sw")
        B7 = tk.Button(parent, height=3, width=8, command=lambda: click((1, 7)), bg="DodgerBlue2", anchor="sw")
        C0 = tk.Button(parent, height=3, width=8, command=lambda: click((2, 0)), bg="DodgerBlue2", anchor="sw")
        C1 = tk.Button(parent, height=3, width=8, command=lambda: click((2, 1)), bg="DodgerBlue3", anchor="sw")
        C2 = tk.Button(parent, height=3, width=8, command=lambda: click((2, 2)), bg="DodgerBlue2", anchor="sw")
        C3 = tk.Button(parent, height=3, width=8, command=lambda: click((2, 3)), bg="DodgerBlue3", anchor="sw")
        C4 = tk.Button(parent, height=3, width=8, command=lambda: click((2, 4)), bg="DodgerBlue2", anchor="sw")
        C5 = tk.Button(parent, height=3, width=8, command=lambda: click((2, 5)), bg="DodgerBlue3", anchor="sw")
        C6 = tk.Button(parent, height=3, width=8, command=lambda: click((2, 6)), bg="DodgerBlue2", anchor="sw")
        C7 = tk.Button(parent, height=3, width=8, command=lambda: click((2, 7)), bg="DodgerBlue3", anchor="sw")
        D0 = tk.Button(parent, height=3, width=8, command=lambda: click((3, 0)), bg="DodgerBlue3", anchor="sw")
        D1 = tk.Button(parent, height=3, width=8, command=lambda: click((3, 1)), bg="DodgerBlue2", anchor="sw")
        D2 = tk.Button(parent, height=3, width=8, command=lambda: click((3, 2)), bg="DodgerBlue3", anchor="sw")
        D3 = tk.Button(parent, height=3, width=8, command=lambda: click((3, 3)), bg="white", anchor="sw")
        D4 = tk.Button(parent, height=3, width=8, command=lambda: click((3, 4)), bg="black", anchor="sw")
        D5 = tk.Button(parent, height=3, width=8, command=lambda: click((3, 5)), bg="DodgerBlue2", anchor="sw")
        D6 = tk.Button(parent, height=3, width=8, command=lambda: click((3, 6)), bg="DodgerBlue3", anchor="sw")
        D7 = tk.Button(parent, height=3, width=8, command=lambda: click((3, 7)), bg="DodgerBlue2", anchor="sw")
        E0 = tk.Button(parent, height=3, width=8, command=lambda: click((4, 0)), bg="DodgerBlue2", anchor="sw")
        E1 = tk.Button(parent, height=3, width=8, command=lambda: click((4, 1)), bg="DodgerBlue3", anchor="sw")
        E2 = tk.Button(parent, height=3, width=8, command=lambda: click((4, 2)), bg="DodgerBlue2", anchor="sw")
        E3 = tk.Button(parent, height=3, width=8, command=lambda: click((4, 3)), bg="black", anchor="sw")
        E4 = tk.Button(parent, height=3, width=8, command=lambda: click((4, 4)), bg="white", anchor="sw")
        E5 = tk.Button(parent, height=3, width=8, command=lambda: click((4, 5)), bg="DodgerBlue3", anchor="sw")
        E6 = tk.Button(parent, height=3, width=8, command=lambda: click((4, 6)), bg="DodgerBlue2", anchor="sw")
        E7 = tk.Button(parent, height=3, width=8, command=lambda: click((4, 7)), bg="DodgerBlue3", anchor="sw")
        F0 = tk.Button(parent, height=3, width=8, command=lambda: click((5, 0)), bg="DodgerBlue3", anchor="sw")
        F1 = tk.Button(parent, height=3, width=8, command=lambda: click((5, 1)), bg="DodgerBlue2", anchor="sw")
        F2 = tk.Button(parent, height=3, width=8, command=lambda: click((5, 2)), bg="DodgerBlue3", anchor="sw")
        F3 = tk.Button(parent, height=3, width=8, command=lambda: click((5, 3)), bg="DodgerBlue2", anchor="sw")
        F4 = tk.Button(parent, height=3, width=8, command=lambda: click((5, 4)), bg="DodgerBlue3", anchor="sw")
        F5 = tk.Button(parent, height=3, width=8, command=lambda: click((5, 5)), bg="DodgerBlue2", anchor="sw")
        F6 = tk.Button(parent, height=3, width=8, command=lambda: click((5, 6)), bg="DodgerBlue3", anchor="sw")
        F7 = tk.Button(parent, height=3, width=8, command=lambda: click((5, 7)), bg="DodgerBlue2", anchor="sw")
        G0 = tk.Button(parent, height=3, width=8, command=lambda: click((6, 0)), bg="DodgerBlue2", anchor="sw")
        G1 = tk.Button(parent, height=3, width=8, command=lambda: click((6, 1)), bg="DodgerBlue3", anchor="sw")
        G2 = tk.Button(parent, height=3, width=8, command=lambda: click((6, 2)), bg="DodgerBlue2", anchor="sw")
        G3 = tk.Button(parent, height=3, width=8, command=lambda: click((6, 3)), bg="DodgerBlue3", anchor="sw")
        G4 = tk.Button(parent, height=3, width=8, command=lambda: click((6, 4)), bg="DodgerBlue2", anchor="sw")
        G5 = tk.Button(parent, height=3, width=8, command=lambda: click((6, 5)), bg="DodgerBlue3", anchor="sw")
        G6 = tk.Button(parent, height=3, width=8, command=lambda: click((6, 6)), bg="DodgerBlue2", anchor="sw")
        G7 = tk.Button(parent, height=3, width=8, command=lambda: click((6, 7)), bg="DodgerBlue3", anchor="sw")
        H0 = tk.Button(parent, height=3, width=8, command=lambda: click((7, 0)), bg="DodgerBlue3", anchor="sw")
        H1 = tk.Button(parent, height=3, width=8, command=lambda: click((7, 1)), bg="DodgerBlue2", anchor="sw")
        H2 = tk.Button(parent, height=3, width=8, command=lambda: click((7, 2)), bg="DodgerBlue3", anchor="sw")
        H3 = tk.Button(parent, height=3, width=8, command=lambda: click((7, 3)), bg="DodgerBlue2", anchor="sw")
        H4 = tk.Button(parent, height=3, width=8, command=lambda: click((7, 4)), bg="DodgerBlue3", anchor="sw")
        H5 = tk.Button(parent, height=3, width=8, command=lambda: click((7, 5)), bg="DodgerBlue2", anchor="sw")
        H6 = tk.Button(parent, height=3, width=8, command=lambda: click((7, 6)), bg="DodgerBlue3", anchor="sw")
        H7 = tk.Button(parent, height=3, width=8, command=lambda: click((7, 7)), bg="DodgerBlue2", anchor="sw")
        buttons = {0: [A0, 0], 1: [A1, 0], 2: [A2, 0], 3: [A3, 0], 4: [A4, 0], 5: [A5, 0], 6: [A6, 0], 7: [A7, 0],
                   8: [B0, 0], 9: [B1, 0], 10: [B2, 0], 11: [B3, 0],  12: [B4, 0], 13: [B5, 0], 14: [B6, 0], 15: [B7, 0],
                   16: [C0, 0], 17: [C1, 0], 18: [C2, 0], 19: [C3, 0], 20: [C4, 0], 21: [C5, 0], 22: [C6, 0], 23: [C7, 0],
                   24: [D0, 0], 25: [D1, 0], 26: [D2, 0], 27: [D3, 0], 28: [D4, 0], 29: [D5, 0], 30: [D6, 0], 31: [D7, 0],
                   32: [E0, 0], 33: [E1, 0], 34: [E2, 0], 35: [E3, 0], 36: [E4, 0], 37: [E5, 0], 38: [E6, 0], 39: [E7, 0],
                   40: [F0, 0], 41: [F1, 0], 42: [F2, 0], 43: [F3, 0], 44: [F4, 0], 45: [F5, 0], 46: [F6, 0], 47: [F7, 0],
                   48: [G0, 0], 49: [G1, 0], 50: [G2, 0], 51: [G3, 0], 52: [G4, 0], 53: [G5, 0], 54: [G6, 0], 55: [G7, 0],
                   56: [H0, 0], 57: [H1, 0], 58: [H2, 0], 59: [H3, 0], 60: [H4, 0], 61: [H5, 0], 62: [H6, 0], 63: [H7, 0],
                   }
        for i in range(len(buttons)):
            r = int(i / 8)
            c = i % 8
            buttons[i][0].grid(row=r, column=c)
        buttons[27][1] = 1
        buttons[28][1] = 1
        buttons[35][1] = 1
        buttons[36][1] = 1

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
            time.sleep(1)
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


def run_gui(gui_sock=None):
    root = tk.Tk()
    board = GameBoard(parent=root, gui_sock=gui_sock)
    root.mainloop()
    gui_sock.send((-2, -2))
    gui_sock.close()


if __name__ == "__main__":
    run_gui()

