import copy


class Board:

    def __init__(self, array=None):
        """ Initialize the board entries. """
        if array is None:
            self.board_array = [[0]*8 for x in range(8)]
            self.board_array[3][3] = 1
            self.board_array[4][4] = 1
            self.board_array[3][4] = -1
            self.board_array[4][3] = -1
        else:
            self.board_array = array

    def place_disc(self, row, col, color):
        """ This function change the entries of the board. """
        if not (8 > row >= 0 and 8 > col >= 0 and (color == 1 or color == -1)):
            return None
        if self.board_array[row][col] != 0:
            return None
        row_up = range(row + 1, 8)
        row_down = range(row - 1, -1, -1)
        row_self = [row for i in range(8)]
        col_up = range(col + 1, 8)
        col_down = range(col - 1, -1, -1)
        col_self = [col for i in range(8)]
        directions = [list(zip(row_up, col_down)), list(zip(row_up, col_self)), list(zip(row_up, col_up)),
                      list(zip(row_down, col_down)), list(zip(row_self, col_down)), list(zip(row_self, col_up)),
                      list(zip(row_down, col_self)), list(zip(row_down, col_up))]
        board_temp = copy.deepcopy(self.board_array)
        flipped = False
        for direction in directions:
            count = 0
            for (row_num, col_num) in direction:
                if self.board_array[row_num][col_num] == -1 * color:
                    count = count + 1
                elif board_temp[row_num][col_num] == color:
                    break
                else:
                    count = 0
                    break
            if count == len(direction):
                count = 0
            if count > 0:
                flipped = True
            for i in range(count):
                (row_num, col_num) = direction[i]
                board_temp[row_num][col_num] = color
        if flipped:
            board_temp[row][col] = color
            return Board(board_temp)
        else:
            return None

    def display_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board_array[i][j], end='  ')
            print('')

    def count_disc(self):
        white_counter = 0
        black_counter = 0
        for i in range(8):
            for j in range(8):
                if self.board_array[i][j] == 1:
                    white_counter = white_counter + 1
                elif self.board_array[i][j] == -1:
                    black_counter = black_counter + 1
        return [white_counter, black_counter]

    def get_board_entry(self, row, col):
        return self.board_array[row][col]

    def get_board_all(self):
        board_entries = []
        for i in range(8):
            for j in range(8):
                board_entries.append(self.board_array[i][j])
        return board_entries

    def get_availability(self):
        available_entry = 0
        for i in range(8):
            for j in range(8):
                if self.get_board_entry(i, j) == 0:
                    test_board = self.place_disc(i, j, 1)
                    if test_board is not None:
                        available_entry = available_entry + 1
        return available_entry
