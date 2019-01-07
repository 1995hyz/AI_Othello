import board
import board_ai

array = [[0,  0,  0,  0,  0,  0,  0,  0],
         [1, 0,  1,  1,  1,  0,  0,  0],
         [-1, -1,  -1,  1,  1,  -1,  0,  0],
         [-1, 0,  1,  1,  1,  1,  0,  0],
         [-1,  1,  -1,  1,  1,  1,  0,  0],
         [-1,  -1,  1,  1,  1,  1,  1,  1],
         [-1, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, -1, 0, 1, 1, 1, 0]]

current_board = board.Board(array=array)
blank_space = []
board_ai.evaluation(current_board)

"""for i in range(8):
    for j in range(8):
        if current_board.get_board_entry(i, j) == 0:
            blank_space.append((i, j))
for (r, c) in blank_space:
    new_board = current_board.place_disc(r, c, 1)
    if new_board is None:
        continue
    else:
        print(r, end='')
        print(c)"""
