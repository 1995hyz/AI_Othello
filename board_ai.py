import board
import time

pos_inf = 10000
neg_inf = 10000


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
        """
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
        if disc[0] + disc[1] < 16:
            availability = a_board.get_availability(color=self.color)
            counter_availability = a_board.get_availability(color=self.color * -1)
            return (max_sum + (disc[self.index[0]] - disc[self.index[1]]) * 0.1 + bonus_value) * 0.1 + (len(availability) - len(counter_availability)) * 0.2
        elif 16 <= disc[0] + disc[1] < 32:
            availability = a_board.get_availability(color=self.color)
            counter_availability = a_board.get_availability(color=self.color * -1)
            return (max_sum + (disc[self.index[0]] - disc[self.index[1]]) * 0.1 + bonus_value) * 0.2 + (len(availability) - len(counter_availability)) * 0.05
        else:
            # availability = a_board.get_availability()
            return (max_sum + (disc[self.index[0]] - disc[self.index[1]]) * 0.15 + bonus_value) * 0.2   # + availability * 0.005
        """

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
        if my_disc > opp_disc:
            piece_diff = (100 * my_disc) / (my_disc + opp_disc)
        elif my_disc < opp_disc:
            piece_diff = -(100*opp_disc) / (my_disc + opp_disc)
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



        my_disc = len(a_board.get_availability(color=self.color))
        opp_disc = len(a_board.get_availability(color=self.color*-1))
        if my_disc > opp_disc:
            mobility = (100 * my_disc) / (my_disc + opp_disc)
        elif my_disc < opp_disc:
            mobility = -(100 * opp_disc) / (my_disc + opp_disc)
        else:
            mobility = 0

        return (10 * piece_diff + 802 * corner_occ + 79 * mobility + 75 * frontier + 10 * max_sum) * 0.0001




    def alpha_beta_search(self, current_board, limit, max_time):
        [value, row, col] = self.max_value(current_board, neg_inf, pos_inf, limit, max_time)
        return [value, row, col]

    def max_value(self, current_board, alpha, beta, limit, max_time):
        if max_time < 0.5:
            return [-20000, -1, -1]
        loop_start = time.clock()
        remaining_time = max_time
        result = current_board.ending_test()
        if result == -1:
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

                if limit == 5:
                    print([value_temp, row, col])

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
        if result == -1:
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

            print("*****" + str(value) + "*****")

            end = time.clock()
            remaining_time = remaining_time - (end - start)
            if value == pos_inf or value == neg_inf:
                return [value, row, col, limit]

            if value == -20000:   # max_time / pow(2, (limit - 2)) > (end - start):
                value_temp = value
                row_temp = row
                col_temp = col
                limit = limit + 1
                continue
            else:
                return [value_temp, row_temp, col_temp, limit]
