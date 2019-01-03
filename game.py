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
        if row == -2 and col == -2:         # Pipe closing message
            main_sock.close()
            break
        play_temp = play_board.place_disc(row, col, 1)
        if play_temp is None:
            print('Invalid Placement')
            main_sock.send([-3])
            continue
        else:
            play_board = play_temp
            play_board.display_board()
        print('AI\'s Move')
        [value, row, col] = board_ai.alpha_beta_search(play_board, 3)
        if row == -1:
            print('AI Fail to Find Any Move')
            [white_counter, black_counter] = play_board.count_disc()
            if white_counter >= black_counter:
                main_sock.send([-4])
                print('User Wins')
            else:
                main_sock.send([-5])
                print('AI Wins')
            main_sock.send(play_board.get_board_all())
        else:
            play_board = play_board.place_disc(row, col, -1)
            play_board.display_board()
            main_sock.send(play_board.get_board_all())
    gui_p.join()


if __name__ == '__main__':
    game_turn()
