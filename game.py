import board
import board_ai
import board_human
import board_gui
import multiprocessing
import time

init_limit = 3
max_time = 5

def game_turn(player_one, player_two, board_load):
    play_board = board.Board()
    while True:
        if player_1.name == "human":
            [value, row, col] = player_1.get_coordination()
        else:
            [value, row, col] = player_1.iterative_dls(play_board, init_limit, max_time)



    """
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
    gui_p.join()"""


if __name__ == '__main__':
    select_1 = input("Will player1 be a computer? (Y/N)")
    select_2 = input("Will player2 be a computer? (Y/N)")
    history = input("Do you want to load a board from a file? (Y/N)")
    if select_1 == 'Y':
        player_1 = board_ai.AI()
    else:
        player_1 = board_human.Human()
    if select_2 == 'Y':
        player_2 = board_ai.AI()
    else:
        player_2 = board_human.Human()
    game_turn()
