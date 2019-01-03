import tkinter as tk
import game
import time


class GameBoard(tk.Frame):

    def __init__(self, parent, rows=8, columns=8, gui_sock=None):
        self.rows = rows
        self.columns = columns
        tk.Frame.__init__(self, parent)
        buttons = {}

        A0 = tk.Button(parent, height=5, width=12, command=lambda: click((0, 0)), bg="DodgerBlue2", anchor="sw")
        A1 = tk.Button(parent, height=5, width=12, command=lambda: click((0, 1)), bg="DodgerBlue3", anchor="sw")
        A2 = tk.Button(parent, height=5, width=12, command=lambda: click((0, 2)), bg="DodgerBlue2", anchor="sw")
        A3 = tk.Button(parent, height=5, width=12, command=lambda: click((0, 3)), bg="DodgerBlue3", anchor="sw")
        A4 = tk.Button(parent, height=5, width=12, command=lambda: click((0, 4)), bg="DodgerBlue2", anchor="sw")
        A5 = tk.Button(parent, height=5, width=12, command=lambda: click((0, 5)), bg="DodgerBlue3", anchor="sw")
        A6 = tk.Button(parent, height=5, width=12, command=lambda: click((0, 6)), bg="DodgerBlue2", anchor="sw")
        A7 = tk.Button(parent, height=5, width=12, command=lambda: click((0, 7)), bg="DodgerBlue3", anchor="sw")
        B0 = tk.Button(parent, height=5, width=12, command=lambda: click((1, 0)), bg="DodgerBlue3", anchor="sw")
        B1 = tk.Button(parent, height=5, width=12, command=lambda: click((1, 1)), bg="DodgerBlue2", anchor="sw")
        B2 = tk.Button(parent, height=5, width=12, command=lambda: click((1, 2)), bg="DodgerBlue3", anchor="sw")
        B3 = tk.Button(parent, height=5, width=12, command=lambda: click((1, 3)), bg="DodgerBlue2", anchor="sw")
        B4 = tk.Button(parent, height=5, width=12, command=lambda: click((1, 4)), bg="DodgerBlue3", anchor="sw")
        B5 = tk.Button(parent, height=5, width=12, command=lambda: click((1, 5)), bg="DodgerBlue2", anchor="sw")
        B6 = tk.Button(parent, height=5, width=12, command=lambda: click((1, 6)), bg="DodgerBlue3", anchor="sw")
        B7 = tk.Button(parent, height=5, width=12, command=lambda: click((1, 7)), bg="DodgerBlue2", anchor="sw")
        C0 = tk.Button(parent, height=5, width=12, command=lambda: click((2, 0)), bg="DodgerBlue2", anchor="sw")
        C1 = tk.Button(parent, height=5, width=12, command=lambda: click((2, 1)), bg="DodgerBlue3", anchor="sw")
        C2 = tk.Button(parent, height=5, width=12, command=lambda: click((2, 2)), bg="DodgerBlue2", anchor="sw")
        C3 = tk.Button(parent, height=5, width=12, command=lambda: click((2, 3)), bg="DodgerBlue3", anchor="sw")
        C4 = tk.Button(parent, height=5, width=12, command=lambda: click((2, 4)), bg="DodgerBlue2", anchor="sw")
        C5 = tk.Button(parent, height=5, width=12, command=lambda: click((2, 5)), bg="DodgerBlue3", anchor="sw")
        C6 = tk.Button(parent, height=5, width=12, command=lambda: click((2, 6)), bg="DodgerBlue2", anchor="sw")
        C7 = tk.Button(parent, height=5, width=12, command=lambda: click((2, 7)), bg="DodgerBlue3", anchor="sw")
        D0 = tk.Button(parent, height=5, width=12, command=lambda: click((3, 0)), bg="DodgerBlue3", anchor="sw")
        D1 = tk.Button(parent, height=5, width=12, command=lambda: click((3, 1)), bg="DodgerBlue2", anchor="sw")
        D2 = tk.Button(parent, height=5, width=12, command=lambda: click((3, 2)), bg="DodgerBlue3", anchor="sw")
        D3 = tk.Button(parent, height=5, width=12, command=lambda: click((3, 3)), bg="white", anchor="sw")
        D4 = tk.Button(parent, height=5, width=12, command=lambda: click((3, 4)), bg="black", anchor="sw")
        D5 = tk.Button(parent, height=5, width=12, command=lambda: click((3, 5)), bg="DodgerBlue2", anchor="sw")
        D6 = tk.Button(parent, height=5, width=12, command=lambda: click((3, 6)), bg="DodgerBlue3", anchor="sw")
        D7 = tk.Button(parent, height=5, width=12, command=lambda: click((3, 7)), bg="DodgerBlue2", anchor="sw")
        E0 = tk.Button(parent, height=5, width=12, command=lambda: click((4, 0)), bg="DodgerBlue2", anchor="sw")
        E1 = tk.Button(parent, height=5, width=12, command=lambda: click((4, 1)), bg="DodgerBlue3", anchor="sw")
        E2 = tk.Button(parent, height=5, width=12, command=lambda: click((4, 2)), bg="DodgerBlue2", anchor="sw")
        E3 = tk.Button(parent, height=5, width=12, command=lambda: click((4, 3)), bg="black", anchor="sw")
        E4 = tk.Button(parent, height=5, width=12, command=lambda: click((4, 4)), bg="white", anchor="sw")
        E5 = tk.Button(parent, height=5, width=12, command=lambda: click((4, 5)), bg="DodgerBlue3", anchor="sw")
        E6 = tk.Button(parent, height=5, width=12, command=lambda: click((4, 6)), bg="DodgerBlue2", anchor="sw")
        E7 = tk.Button(parent, height=5, width=12, command=lambda: click((4, 7)), bg="DodgerBlue3", anchor="sw")
        F0 = tk.Button(parent, height=5, width=12, command=lambda: click((5, 0)), bg="DodgerBlue3", anchor="sw")
        F1 = tk.Button(parent, height=5, width=12, command=lambda: click((5, 1)), bg="DodgerBlue2", anchor="sw")
        F2 = tk.Button(parent, height=5, width=12, command=lambda: click((5, 2)), bg="DodgerBlue3", anchor="sw")
        F3 = tk.Button(parent, height=5, width=12, command=lambda: click((5, 3)), bg="DodgerBlue2", anchor="sw")
        F4 = tk.Button(parent, height=5, width=12, command=lambda: click((5, 4)), bg="DodgerBlue3", anchor="sw")
        F5 = tk.Button(parent, height=5, width=12, command=lambda: click((5, 5)), bg="DodgerBlue2", anchor="sw")
        F6 = tk.Button(parent, height=5, width=12, command=lambda: click((5, 6)), bg="DodgerBlue3", anchor="sw")
        F7 = tk.Button(parent, height=5, width=12, command=lambda: click((5, 7)), bg="DodgerBlue2", anchor="sw")
        G0 = tk.Button(parent, height=5, width=12, command=lambda: click((6, 0)), bg="DodgerBlue2", anchor="sw")
        G1 = tk.Button(parent, height=5, width=12, command=lambda: click((6, 1)), bg="DodgerBlue3", anchor="sw")
        G2 = tk.Button(parent, height=5, width=12, command=lambda: click((6, 2)), bg="DodgerBlue2", anchor="sw")
        G3 = tk.Button(parent, height=5, width=12, command=lambda: click((6, 3)), bg="DodgerBlue3", anchor="sw")
        G4 = tk.Button(parent, height=5, width=12, command=lambda: click((6, 4)), bg="DodgerBlue2", anchor="sw")
        G5 = tk.Button(parent, height=5, width=12, command=lambda: click((6, 5)), bg="DodgerBlue3", anchor="sw")
        G6 = tk.Button(parent, height=5, width=12, command=lambda: click((6, 6)), bg="DodgerBlue2", anchor="sw")
        G7 = tk.Button(parent, height=5, width=12, command=lambda: click((6, 7)), bg="DodgerBlue3", anchor="sw")
        H0 = tk.Button(parent, height=5, width=12, command=lambda: click((7, 0)), bg="DodgerBlue3", anchor="sw")
        H1 = tk.Button(parent, height=5, width=12, command=lambda: click((7, 1)), bg="DodgerBlue2", anchor="sw")
        H2 = tk.Button(parent, height=5, width=12, command=lambda: click((7, 2)), bg="DodgerBlue3", anchor="sw")
        H3 = tk.Button(parent, height=5, width=12, command=lambda: click((7, 3)), bg="DodgerBlue2", anchor="sw")
        H4 = tk.Button(parent, height=5, width=12, command=lambda: click((7, 4)), bg="DodgerBlue3", anchor="sw")
        H5 = tk.Button(parent, height=5, width=12, command=lambda: click((7, 5)), bg="DodgerBlue2", anchor="sw")
        H6 = tk.Button(parent, height=5, width=12, command=lambda: click((7, 6)), bg="DodgerBlue3", anchor="sw")
        H7 = tk.Button(parent, height=5, width=12, command=lambda: click((7, 7)), bg="DodgerBlue2", anchor="sw")
        buttons = {0: A0, 1: A1, 2: A2, 3: A3, 4: A4, 5: A5, 6: A6, 7: A7,
                   8: B0, 9: B1, 10: B2, 11: B3, 12: B4, 13: B5, 14: B6, 15: B7,
                   16: C0, 17: C1, 18: C2, 19: C3, 20: C4, 21: C5, 22: C6, 23: C7,
                   24: D0, 25: D1, 26: D2, 27: D3, 28: D4, 29: D5, 30: D6, 31: D7,
                   32: E0, 33: E1, 34: E2, 35: E3, 36: E4, 37: E5, 38: E6, 39: E7,
                   40: F0, 41: F1, 42: F2, 43: F3, 44: F4, 45: F5, 46: F6, 47: F7,
                   48: G0, 49: G1, 50: G2, 51: G3, 52: G4, 53: G5, 54: G6, 55: G7,
                   56: H0, 57: H1, 58: H2, 59: H3, 60: H4, 61: H5, 62: H6, 63: H7
                   }
        for i in range(len(buttons)):
            r = int(i / 8)
            c = i % 8
            buttons[i].grid(row=r, column=c)
        del buttons[27]
        del buttons[28]
        del buttons[35]
        del buttons[36]

        def click(coordinate):
            user_coordinate = (-1, -1)
            index = coordinate[0] * 8 + coordinate[1]
            print(coordinate)
            if index in buttons:
                gui_sock.send(coordinate)
                user_board = gui_sock.recv()
            if user_coordinate[0] != -3:
                buttons[index].config(bg='white')
                del buttons[index]
                index = user_coordinate[0] * 8 + user_coordinate[1]
                if index in buttons:
                    buttons[index].config(bg='black')
                    del buttons[index]
                else:
                    print('Error: Over-claiming Entry')


def run_gui(gui_sock=None):
    root = tk.Tk()
    board = GameBoard(parent=root, gui_sock=gui_sock)
    root.mainloop()
    gui_sock.send((-2, -2))
    gui_sock.close()


if __name__ == "__main__":
    run_gui()

