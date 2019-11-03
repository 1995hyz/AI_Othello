import copy
import time

counter = 0


class Board:

    def __init__(self, array=None):
        """ Initialize the board entries. """
        if array is None:
            self.board_array = [[0]*8 for x in range(8)]
            self.board_array[3][3] = -1
            self.board_array[4][4] = -1
            self.board_array[3][4] = 1
            self.board_array[4][3] = 1
        else:
            self.board_array = array
        # self.availability_1 = self.cal_availability(color=1)
        # self.availability_2 = self.cal_availability(color=-1)

    def place_disc(self, row, col, color):
        global counter
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

        # start = time.clock()

        directions = [list(zip(row_up, col_down)), list(zip(row_up, col_self)), list(zip(row_up, col_up)),
                      list(zip(row_down, col_down)), list(zip(row_self, col_down)), list(zip(row_self, col_up)),
                      list(zip(row_down, col_self)), list(zip(row_down, col_up))]

        board_temp = copy.deepcopy(self.board_array)
        # end = time.clock()
        # print(str(counter) + "  " + str(end-start))
        counter += 1
        flipped = False

        start = time.clock()

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

        end = time.clock()
        # print(str(counter) + "  " + str(end - start))

        if flipped:
            board_temp[row][col] = color
            return Board(board_temp)
        else:
            return None

    def check_disc(self, row, col, color):
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

        for direction in directions:
            count = 0
            for (row_num, col_num) in direction:
                if self.board_array[row_num][col_num] == -1 * color:
                    count = count + 1
                elif self.board_array[row_num][col_num] == color:
                    break
                else:
                    count = 0
                    break
            if count == len(direction):
                count = 0
            if count > 0:
                return True
        return False

    def display_board(self):
        print("Current Board:")
        print("Player 1 is %")
        print("Player 2 is $")
        print("\n")
        print("   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 ")
        for i in range(8):
            print("----------------------------------")
            print("     |   |   |   |   |   |   |   ")
            print(str(i) + " ", end='')
            for j in range(7):
                if self.board_array[i][j] == 1:
                    print(' % ', end='')
                elif self.board_array[i][j] == -1:
                    print(' $ ', end='')
                else:
                    print("   ", end='')
                print('|', end='')
            if self.board_array[i][7] == 1:
                print(' % ')
            elif self.board_array[i][7] == -1:
                print(' $ ')
            else:
                print("   ")
            print("     |   |   |   |   |   |   |   ")
        print("----------------------------------")

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

    def get_availability(self, color):
        available_entry = []
        for i in range(8):
            for j in range(8):
                if self.get_board_entry(i, j) == 0:
                    """
                    test_board = self.place_disc(i, j, color)
                    if test_board is not None:
                        available_entry.append((i, j))
                    """
                    test_board = self.check_disc(i, j, color)
                    if test_board:
                        available_entry.append((i, j))
        return available_entry

        """
        if color == 1:
            return self.availability_1
        else:
            return self.availability_2
        """

    def get_tbd(self, color):
        check_list = []
        for i in range(8):
            for j in range(8):
                if self.board_array[i][j] != 0:
                    continue
                if 7 > i > 0 and 7 > j > 0:
                    check_pos = [(i-1, j-1), (i-1, j), (i-1, j+1),
                                 (i, j-1), (i, j+1),
                                 (i+1, j-1), (i+1, j), (i+1, j+1)]
                elif i == 0 and j == 0:
                    check_pos = [(i+1, j+1), (i+1, j), (i, j+1)]
                elif i == 0 and j == 7:
                    check_pos = [(i+1, j), (i, j-1), ]

    def ending_test(self):
        [white_counter, black_counter] = self.count_disc()
        if white_counter + black_counter == 64:
            if white_counter <= black_counter:
                return 1
            else:
                return -1
        else:
            return 0

    @staticmethod
    def load_board(file_path):
        board_load = []
        with open(file_path, mode='r') as file:
            for i in range(8):
                row_str = file.readline()[:-1]
                row = [int(x) for x in row_str.split(',')]
                board_load.append(row)
        return Board(board_load)

    def save_board(self, file_path="board.txt"):
        with open(file_path, mode='w+') as file:
            output_str = ""
            for i in range(8):
                line_str = ""
                for j in range(7):
                    line_str += (str(self.board_array[i][j]) + ",")
                line_str += (str(self.board_array[i][7]) + "\n")
                output_str += line_str
            file.write(output_str)
    """
    def cal_availability(self, color):
        available_entry = []
        for i in range(8):
            for j in range(8):
                if self.get_board_entry(i, j) == 0:
                    test_board = self.place_disc(i, j, color)
                    if test_board is not None:
                        available_entry.append((i, j))
        return available_entry
    """


if __name__ == "__main__":
    board = Board()
    board.display_board()

    board.check_disc(4, 5, 1)
