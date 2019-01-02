import board
import board_ai

if __name__ == '__main__':
    play_board = board.Board()
    while True:
        play_board.display_board()
        if not int(input('Do you want to continue? 0/1: ')):
            break
        argument = input('disc argument: ').split(',')
        play_temp = play_board.place_disc(int(argument[0]), int(argument[1]), int(argument[2]))
        if play_temp is None:
            print('Invalid Placement')
        else:
            play_board = play_temp

