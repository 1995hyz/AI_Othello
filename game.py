import board
import board_ai
import board_gui
import multiprocessing
import time


def iterative_DLS(current_board, init_limit, max_time):
    start = 0
    end = 0
    limit = init_limit
    while True:
        start = time.clock()
        [value, rol, col] = board_ai.alpha_beta_search(current_board, limit)
        end = time.clock()
        if max_time/pow(2, (limit-2)) > (end - start):
            limit = limit + 2
            if limit > 5:
                return [value, rol, col]
            continue
        else:
            return [value, rol, col]


def game_turn():
    play_board = board.Board()
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
        # AI's Move
        [value, row, col] = iterative_DLS(play_board, 3, 10)     # board_ai.alpha_beta_search(play_board, 3)
        if row == -1:
            [white_counter, black_counter] = play_board.count_disc()
            if white_counter >= black_counter:
                main_sock.send([-4])    # User Wins
            else:
                main_sock.send([-5])    # AI Wins
            main_sock.send(play_board.get_board_all())
        else:
            play_board = play_board.place_disc(row, col, -1)
            availability = play_board.get_availability()
            if availability == 0:
                [white_counter, black_counter] = play_board.count_disc()
                if white_counter >= black_counter:
                    main_sock.send([-4])
                else:
                    main_sock.send([-5])
            main_sock.send(play_board.get_board_all())
    gui_p.join()


if __name__ == '__main__':
    game_turn()
