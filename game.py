import board
import board_ai
import board_gui
import multiprocessing


def game_turn():
    play_board = board.Board()
    play_board.display_board()
    main_sock, gui_sock = multiprocessing.Pipe()
    gui_p = multiprocessing.Process(target=board_gui.run_gui, args=(gui_sock,))
    gui_p.start()
    while True:
        (row, col) = main_sock.recv()
        print(row, end=' ')
        print(col)
        if row == -2 and col == -2:         # Pipe closing message
            main_sock.close()
            break
        play_temp = play_board.place_disc(row, col, 1)
        if play_temp is None:
            print('Invalid Placement')
            main_sock.send((-3, -3))
        else:
            play_board = play_temp
            play_board.display_board()
        print('AI\'s Move')
        [value, row, col] = board_ai.alpha_beta_search(play_board, 3)
        if row == -1:
            print('AI Fail to Find Any Move')
            main_sock.send((-2, -2))
        else:
            play_board = play_board.place_disc(row, col, -1)
            play_board.display_board()
            main_sock.send((row, col))
    gui_p.join()


def test():
    play_board = board.Board()
    play_board.display_board()
    while True:
        if not int(input('Do you want to continue? 0/1: ')):
            break
        argument = input('disc argument: ').split(',')
        play_temp = play_board.place_disc(int(argument[0]), int(argument[1]), int(argument[2]))
        if play_temp is None:
            print('Invalid Placement')
            continue
        else:
            play_board = play_temp
            play_board.display_board()
        print('AI\'s Move')
        [value, row, col] = board_ai.alpha_beta_search(play_board, 3)
        if row == -1:
            print('AI Fail to Find Any Move')
        else:
            play_board = play_board.place_disc(row, col, -1)
            play_board.display_board()


if __name__ == '__main__':
    game_turn()
   # test()