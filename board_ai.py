import board


def evaluation(a_board):
    position_weight = [[20, -2, 1, 0.5, 0.5, 1, -2, 20],
                       [-2, -5, -0.2, -0.2, -0.2, -0.2, -5, -2],
                       [1, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, 1],
                       [0.5, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, 0.5],
                       [0.5, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, 0.5],
                       [1, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, 1],
                       [-2, -5, -0.2, -0.2, -0.2, -0.2, -5, -2],
                       [20, -2, 1, 0.5, 0.5, 1, -2, 20]
                       ]
    position_sum = 0
    # [white_count, black_count] = a_board.count_disc()
    # availability = a_board.get_availability()
    for i in range(8):
        for j in range(8):
            color = a_board.get_board_entry(i, j)
            if color == -1:
                position_sum = position_sum + position_weight[i][j]
            elif color == 1:
                position_sum = position_sum - position_weight[i][j]
    return position_sum # + (black_count - white_count) * 0.5 #  + position_sum + availability


def alpha_beta_search(current_board, limit):
    [value, row, col] = max_value(current_board, -100, 100, limit)
    return [value, row, col]


def max_value(current_board, alpha, beta, limit):
    result = ending_test(current_board)
    if result == -1:
        return [-100, -1, -1]
    elif result == 1:
        return [100, -1, -1]
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
            # print('Max test: ' + str(r) + ' ' + str(c))
            [value_temp, rol_temp, col_temp] = min_value(new_board, alpha, beta, limit-1)
            # print('Max value: ' + str(value_temp))
            if value_temp >= value:
                value = value_temp
                row = r
                col = c
        if value >= beta:
            return [value, row, col]
        alpha = max(value, alpha)
    return [value, row, col]


def min_value(current_board, alpha, beta, limit):
    result = ending_test(current_board)
    if result == -1:
        return [-100, -1, -1]
    elif result == 1:
        return [100, -1, -1]
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
            # print('Min test: ' + str(r) + ' ' + str(c))
            [value_temp, rol_temp, col_temp] = max_value(new_board, alpha, beta, limit-1)
            # print('Min value: ' + str(value_temp))
            if value_temp <= value:
                value = value_temp
                row = r
                col = c
        if value <= alpha:
            return [value, row, col]
        beta = min(value, beta)
    return [value, row, col]


def ending_test(current_board):
    [white_counter, black_counter] = current_board.count_disc()
    if white_counter + black_counter == 64:
        if white_counter >= black_counter:
            return 1
        elif black_counter > white_counter:
            return -1
        else:
            return 0
