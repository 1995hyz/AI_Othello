import board
import time

pos_inf = 10000
neg_inf = -10000


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

    def evaluation(self, a_board):
        max_sum = 0
        my_disc = 0
        opp_disc = 0
        x = 0
        y = 0
        my_front_tiles = 0
        opp_front_tiles = 0
        x1 = [-1, -1, 0, 1, 1, 1, 0, -1]
        y1 = [0, 1, 1, 1, 0, -1, -1, -1]
        v = [[20, -3, 11, 8, 8, 11, -3, 20],
             [-3, -7, -4, 1, 1, -4, -7, -3],
             [11, -4, 2, 2, 2, 2, -4, 11],
             [8, 1, 2, -3, -3, 2, 1, 8],
             [8, 1, 2, -3, -3, 2, 1, 8],
             [11, -4, 2, 2, 2, 2, -4, 11],
             [-3, -7, -4, 1, 1, -4, -7, -3],
             [20, -3, 11, 8, 8, 11, -3, 20]]
        for i in range(8):
            for j in range(8):
                color = a_board.get_board_entry(i, j)
                if color == self.color:
                    max_sum += v[i][j]
                    my_disc += 1
                elif color == self.color * -1:
                    max_sum -= v[i][j]
                if color != 0:
                    for k in range(8):
                        x = i + x1[k]
                        y = j + y1[k]
                        if 8 > x >= 0 and 8 > y >= 0 and (a_board.get_board_entry(x, y) == 0):
                            if color == self.color:
                                my_front_tiles += 1
                            else:
                                opp_front_tiles += 1
                            break
        total_disc = my_disc + opp_disc
        if my_disc > opp_disc:
            piece_diff = (100 * my_disc) / total_disc
        elif my_disc < opp_disc:
            piece_diff = -(100*opp_disc) / total_disc
        else:
            piece_diff = 0
        if my_front_tiles > opp_front_tiles:
            frontier = -(100 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
        elif my_front_tiles < opp_front_tiles:
            frontier = (100 * opp_front_tiles) / (my_front_tiles + opp_front_tiles)
        else:
            frontier = 0

        my_disc = opp_disc = 0
        color_00 = a_board.get_board_entry(0, 0)
        if color_00 == self.color:
            my_disc += 1
        elif color_00 == self.color * -1:
            opp_disc += 1
        color_07 = a_board.get_board_entry(0, 7)
        if color_07 == self.color:
            my_disc += 1
        elif color_07 == self.color * -1:
            opp_disc += 1
        color_70 = a_board.get_board_entry(7, 0)
        if color_70 == self.color:
            my_disc += 1
        elif color_70 == self.color * -1:
            opp_disc += 1
        color_77 = a_board.get_board_entry(7, 7)
        if color_77 == self.color:
            my_disc += 1
        elif color_77 == self.color * -1:
            opp_disc += 1
        corner_occ = 25 * (my_disc - opp_disc)

        my_disc = opp_disc = 0
        if color_00 == 0:
            color = a_board.get_board_entry(0, 1)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
            color = a_board.get_board_entry(1, 1)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
            color = a_board.get_board_entry(1, 0)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
        if color_07 == 0:
            color = a_board.get_board_entry(0, 6)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
            color = a_board.get_board_entry(1, 6)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
            color = a_board.get_board_entry(1, 7)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
        if color_70 == 0:
            color = a_board.get_board_entry(7, 1)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
            color = a_board.get_board_entry(6, 1)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
            color = a_board.get_board_entry(6, 0)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
        if color_77 == 0:
            color = a_board.get_board_entry(6, 7)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
            color = a_board.get_board_entry(6, 6)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
            color = a_board.get_board_entry(7, 6)
            if color == self.color:
                my_disc += 1
            elif color == self.color * -1:
                opp_disc += 1
        corner_close = -12.5 * (my_disc - opp_disc)

        my_disc = len(a_board.get_availability(color=self.color))
        opp_disc = len(a_board.get_availability(color=self.color*-1))
        if my_disc > opp_disc:
            mobility = (100 * my_disc) / (my_disc + opp_disc)
        elif my_disc < opp_disc:
            mobility = -(100 * opp_disc) / (my_disc + opp_disc)
        else:
            mobility = 0

        if total_disc < 50:
            return (10 * piece_diff + 802 * corner_occ + 382*corner_close + 79 * mobility + 75 * frontier + 10 * max_sum) * 0.00001
        else:
            return (200 * piece_diff + 802 * corner_occ + 382*corner_close + 79 * mobility + 75 * frontier + 10 * max_sum) * 0.00001

    def alpha_beta_search(self, current_board, limit, max_time):
        [value, row, col] = self.max_value(current_board, neg_inf, pos_inf, limit, max_time)
        return [value, row, col]

    def max_value(self, current_board, alpha, beta, limit, max_time):
        if max_time < 0.5:
            return [-20000, -1, -1]
        loop_start = time.clock()
        remaining_time = max_time
        result = current_board.ending_test()
        if result == -1 or result == -2:
            return [pos_inf, -1, -1]
        elif result == 1:
            return [neg_inf, -1, -1]
        if limit == 0:
            return [self.evaluation(current_board), -1, -1]
        value = neg_inf
        row = -1
        col = -1
        blank_space = current_board.get_availability(self.color)
        loop_end = time.clock()
        remaining_time = remaining_time - (loop_end - loop_start)
        for (r, c) in blank_space:
            loop_start = time.clock()
            new_board = current_board.place_disc(r, c, self.color)
            if new_board is None:
                continue
            else:
                [value_temp, rol_temp, col_temp] = self.min_value(new_board, alpha, beta, limit-1, remaining_time)
                if value_temp == -20000:
                    return [-20000, -1, -1]
                if value_temp >= value:
                    value = value_temp
                    row = r
                    col = c
                if value_temp >= beta:
                    return [value, row, col]
                alpha = max(value_temp, alpha)
            loop_end = time.clock()
            remaining_time = remaining_time - (loop_end - loop_start)
        return [value, row, col]

    def min_value(self, current_board, alpha, beta, limit, max_time):
        if max_time < 0.5:
            return [-20000, -1, -1]
        loop_start = time.clock()
        remaining_time = max_time
        result = current_board.ending_test()
        if result == -1 or result == -2:
            return [pos_inf, -1, -1]
        elif result == 1:
            return [neg_inf, -1, -1]
        if limit == 0:
            return [self.evaluation(current_board), -1, -1]
        value = pos_inf
        row = -1
        col = -1
        blank_space = current_board.get_availability(self.color * -1)
        loop_end = time.clock()
        remaining_time = remaining_time - (loop_end - loop_start)
        for (r, c) in blank_space:
            loop_start = time.clock()
            new_board = current_board.place_disc(r, c, self.color * -1)
            if new_board is None:
                continue
            else:
                [value_temp, rol_temp, col_temp] = self.max_value(new_board, alpha, beta, limit-1, remaining_time)
                if value_temp == -20000:
                    return [-20000, -1, -1]
                if value_temp <= value:
                    value = value_temp
                    row = r
                    col = c
                if value_temp <= alpha:
                    return [value, row, col]
                beta = min(value_temp, beta)
            loop_end = time.clock()
            remaining_time = remaining_time - (loop_end - loop_start)
        return [value, row, col]

    def iterative_dls(self, current_board, init_limit, max_time):
        limit = init_limit - 1
        value_temp = neg_inf
        row_temp = -1
        col_temp = -1
        remaining_time = max_time
        while True:
            start = time.clock()
            [value, row, col] = self.alpha_beta_search(current_board, limit, remaining_time)
            end = time.clock()
            remaining_time = remaining_time - (end - start)
            if value == pos_inf or value == neg_inf:
                return [value, row, col, limit]
            if value > -10000:   # max_time / pow(2, (limit - 2)) > (end - start):
                value_temp = value
                row_temp = row
                col_temp = col
                limit = limit + 1
                continue
            else:
                return [value_temp, row_temp, col_temp, limit]
