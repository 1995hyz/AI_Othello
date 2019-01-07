import board


position_weight = [[15, -2, 1, 0.5, 0.5, 1, -2, 15],
                   [-2, -5, -0.2, -0.2, -0.2, -0.2, -5, -2],
                   [1, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, 1],
                   [0.5, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, 0.5],
                   [0.5, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, 0.5],
                   [1, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, 1],
                   [-2, -5, -0.2, -0.2, -0.2, -0.2, -5, -2],
                   [15, -2, 1, 0.5, 0.5, 1, -2, 15]
                   ]
pattern_bonus = {(1, 1): -5, (-1, -1): 5}


def bonus(a_board):
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
        if x in pattern_bonus:
            bonus_value = bonus_value + pattern_bonus[x]
    return bonus_value


def evaluation(a_board):
    max_sum = 0
    [white_count, black_count] = a_board.count_disc()
    for i in range(8):
        for j in range(8):
            color = a_board.get_board_entry(i, j)
            if color == -1:
                max_sum = max_sum + position_weight[i][j]
            elif color == 1:
                max_sum = max_sum - position_weight[i][j]
    bonus_value = bonus(a_board)
    if white_count + black_count < 40:
        return (max_sum + (black_count - white_count) * 0.1 + bonus_value) * 0.1 # + availability * 0.1
    else:
        # availability = a_board.get_availability()
        return (max_sum + (black_count - white_count) * 0.15 + bonus_value) * 0.1 # + availability * 0.005


def alpha_beta_search(current_board, limit):
    [value, row, col] = max_value(current_board, -100, 100, limit)
    return [value, row, col]


def max_value(current_board, alpha, beta, limit):
    result = ending_test(current_board)
    if result == -1:
        return [100, -1, -1]
    elif result == 1:
        return [-100, -1, -1]
    if limit == 0:
        return [evaluation(current_board), -1, -1]
    value = -100
    blank_space = []
    row = -1
    col = -1
    for i in range(8):
        for j in range(8):
            if current_board.get_board_entry(i, j) == 0:
                blank_space.append((i, j))
    for (r, c) in blank_space:
        new_board = current_board.place_disc(r, c, -1)
        if new_board is None:
            continue
        else:
            [value_temp, rol_temp, col_temp] = min_value(new_board, alpha, beta, limit-1)
            if value_temp >= value:
                value = value_temp
                row = r
                col = c
            if value_temp >= beta:
                return [value, row, col]
            alpha = max(value_temp, alpha)
    return [value, row, col]


def min_value(current_board, alpha, beta, limit):
    result = ending_test(current_board)
    if result == -1:
        return [100, -1, -1]
    elif result == 1:
        return [-100, -1, -1]
    if limit == 0:
        return [evaluation(current_board), -1, -1]
    value = 100
    blank_space = []
    row = -1
    col = -1
    for i in range(8):
        for j in range(8):
            if current_board.get_board_entry(i, j) == 0:
                blank_space.append((i, j))
    for (r, c) in blank_space:
        new_board = current_board.place_disc(r, c, 1)
        if new_board is None:
            continue
        else:
            [value_temp, rol_temp, col_temp] = max_value(new_board, alpha, beta, limit-1)
            if value_temp <= value:
                value = value_temp
                row = r
                col = c
            if value_temp <= alpha:
                return [value, row, col]
            beta = min(value_temp, beta)
    return [value, row, col]


def ending_test(current_board):
    [white_counter, black_counter] = current_board.count_disc()
    if white_counter + black_counter == 64:
        if white_counter >= black_counter:
            return 1
        else:
            return -1
    else:
        return 0
