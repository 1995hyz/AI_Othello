import board
import board_ai
import board_human
import board_gui
import multiprocessing
import time

init_limit = 3
max_time = 5


def print_legal_move(available_move):
    if available_move:
        print("The legal moves are:")
        for move in available_move:
            print("Move: " + "(" + str(move[0]) + ", " + str(move[1]) + ")")
    else:
        print("No legal moves available.")


def game_turn(player_one, player_two, board_load=None):
    counter = 0
    if board_load:
        play_board = board_load
    else:
        play_board = board.Board()
    play_board.display_board()
    while True:
        available_move = play_board.get_availability(player_1.color)
        print("Player1 to move.")
        print_legal_move(available_move)
        if available_move:
            if player_one.type == "human":
                [value, row, col] = player_one.get_coordination(available_move)
            else:
                [value, row, col] = player_one.iterative_dls(play_board, init_limit, max_time)
            play_board = play_board.place_disc(row, col, player_one.color)
            play_board.display_board()
            counter += 1
            if counter == 60:
                result = play_board.ending_test()
                print(result)
                break
        available_move = play_board.get_availability(player_2.color)
        print("Player2 to move.")
        print_legal_move(available_move)
        if available_move:
            if player_two.type == "human":
                [value, row, col] = player_two.get_coordination(available_move)
            else:
                [value, row, col] = player_two.iterative_dls(play_board, init_limit, max_time)
            play_board = play_board.place_disc(row, col, player_two.color)
            play_board.display_board()
            counter += 1
            if counter == 60:
                result = play_board.ending_test()
                print(result)
                break


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
        player_1 = board_ai.AI(color=1)
    else:
        player_1 = board_human.Human(color=1, name="player1")
    if select_2 == 'Y':
        player_2 = board_ai.AI(color=-1)
    else:
        player_2 = board_human.Human(color=-1, name="player2")
    game_turn(player_1, player_2)
