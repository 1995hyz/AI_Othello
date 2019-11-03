import board
import time


class AI:
    def __init__(self, color):
        self.position_weight = [[4, -3, 2, 2, 2, 2, -3, 4],
                                [-3, -4, -1, -1, -1, -1, -4, -3],
                                [2, -1, 1, 0, 0, 1, -1, 2],
                                [2, -1, 0, 1, 1, 0, -1, 2],
                                [2, -1, 0, 1, 1, 0, -1, 2],
                                [2, -1, 1, 0, 0, 1, -1, 2],
                                [-3, -4, -1, -1, -1, -1, -4, -3],
                                [4, -3, 2, 2, 2, 2, -3, 4]
                                ]

        self.pattern_bonus = {(1, 1): -5, (-1, -1): 5}
        self.type = "ai"
        self.color = color
        if color == 1:
            self.index = [0, 1]
        else:
            self.index = [1, 0]

    """
    def bonus(self, a_board):
        bonus_value = 0
        pattern0 = (a_board.get_board_entry(0, 0), a_board.get_board_entry(0, 1))
        pattern1 = (a_board.get_board_entry(0, 0), a_board.get_board_entry(1, 0))
        pattern2 = (a_board.get_board_entry(7, 7), a_board.get_board_entry(7, 6))
        pattern3 = (a_board.get_board_entry(7, 7), a_board.get_board_entry(6, 7))
        pattern4 = (a_board.get_board_entry(7, 0), a_board.get_board_entry(7, 1))
        pattern5 = (a_board.get_board_entry(7, 0), a_board.get_board_entry(6, 0))
        pattern6 = (a_board.get_board_entry(0, 7), a_board.get_board_entry(0, 6))
        pattern7 = (a_board.get_board_entry(0, 7), a_board.get_board_entry(1, 7))
        pattern8 = (a_board.get_board_entry(0, 0), a_board.get_board_entry(1, 1))
        pattern9 = (a_board.get_board_entry(0, 7), a_board.get_board_entry(1, 6))
        pattern10 = (a_board.get_board_entry(7, 7), a_board.get_board_entry(6, 6))
        pattern11 = (a_board.get_board_entry(7, 0), a_board.get_board_entry(6, 1))
        patterns = [pattern0, pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7,
                    pattern8, pattern9, pattern10, pattern11]
        for x in patterns:
            if x in self.pattern_bonus:
                bonus_value = bonus_value + self.pattern_bonus[x]
        return bonus_value
        """

    def evaluation(self, a_board):
        max_sum = 0
        # [white_count, black_count] = a_board.count_disc()
        disc = a_board.count_disc()
        for i in range(8):
            for j in range(8):
                color = a_board.get_board_entry(i, j)
                if color == self.color:
                    max_sum = max_sum + self.position_weight[i][j]
                elif color == self.color * -1:
                    max_sum = max_sum - self.position_weight[i][j]
        # bonus_value = self.bonus(a_board)
        bonus_value = 0
        if disc[0] + disc[1] < 40:
            availability = a_board.get_availability(color=self.color)
            return (max_sum + (disc[self.index[0]] - disc[self.index[1]]) * 0.1 + bonus_value) * 0.1 + len(availability) * 0.1
        else:
            # availability = a_board.get_availability()
            return (max_sum + (disc[self.index[0]] - disc[self.index[1]]) * 0.15 + bonus_value) * 0.1   # + availability * 0.005

    def alpha_beta_search(self, current_board, limit):
        [value, row, col] = self.max_value(current_board, -100, 100, limit)
        return [value, row, col]

    def max_value(self, current_board, alpha, beta, limit):
        result = current_board.ending_test()
        if result == -1:
            return [100, -1, -1]
        elif result == 1:
            return [-100, -1, -1]
        if limit == 0:
            return [self.evaluation(current_board), -1, -1]
        value = -100
        row = -1
        col = -1
        blank_space = current_board.get_availability(self.color)
        for (r, c) in blank_space:
            new_board = current_board.place_disc(r, c, self.color)
            if new_board is None:
                continue
            else:
                [value_temp, rol_temp, col_temp] = self.min_value(new_board, alpha, beta, limit-1)
                if value_temp >= value:
                    value = value_temp
                    row = r
                    col = c
                if value_temp >= beta:
                    return [value, row, col]
                alpha = max(value_temp, alpha)
        return [value, row, col]

    def min_value(self, current_board, alpha, beta, limit):
        result = current_board.ending_test()
        if result == -1:
            return [100, -1, -1]
        elif result == 1:
            return [-100, -1, -1]
        if limit == 0:
            return [self.evaluation(current_board), -1, -1]
        value = 100
        row = -1
        col = -1
        blank_space = current_board.get_availability(self.color * -1)
        for (r, c) in blank_space:
            new_board = current_board.place_disc(r, c, self.color * -1)
            if new_board is None:
                continue
            else:
                [value_temp, rol_temp, col_temp] = self.max_value(new_board, alpha, beta, limit-1)
                if value_temp <= value:
                    value = value_temp
                    row = r
                    col = c
                if value_temp <= alpha:
                    return [value, row, col]
                beta = min(value_temp, beta)
        return [value, row, col]

    def iterative_dls(self, current_board, init_limit, max_time):
        limit = init_limit
        while True:
            start = time.clock()
            [value, rol, col] = self.alpha_beta_search(current_board, limit)
            end = time.clock()
            if max_time / pow(2, (limit - 2)) > (end - start):
                limit = limit + 1
                continue
            else:
                return [value, rol, col, limit]
