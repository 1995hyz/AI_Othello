import board
import board_ai
import board_human
import board_gui
import multiprocessing
import time

init_limit = 6
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
                start = time.clock()
                [value, row, col, depth] = player_one.iterative_dls(play_board, init_limit, max_time)
                end = time.clock()
                print("Searching time " + str(end-start) + " sec")
                print("Completed search on depth " + str(depth))
                print("The chosen move is (" + str(row) + ", " + str(col) + ")")
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
                start = time.clock()
                [value, row, col, depth] = player_two.iterative_dls(play_board, init_limit, max_time)
                end = time.clock()
                print("Searching time " + str(end-start) + " sec")
                print("Completed search on depth " + str(depth))
                print("The chosen move is (" + str(row) + ", " + str(col) + ")")
            play_board = play_board.place_disc(row, col, player_two.color)
            play_board.display_board()
            counter += 1
            if counter == 60:
                result = play_board.ending_test()
                print(result)
                break
        save_opt = input("Would you like to save the board? (Y/N) ")
        if save_opt == 'Y':
            play_board.save_board("board.txt")


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
    if history == 'Y':
        board_path = input("Please input the path of the board file: ")
        board_load = board.Board.load_board(board_path)
        game_turn(player_1, player_2, board_load=board_load)
    else:
        game_turn(player_1, player_2)
