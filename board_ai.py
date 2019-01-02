import board


def evaluation(a_board):
    [white_count, black_count] = a_board.count_disc()
    return black_count * 0.1


def alpha_beta_search(current_board, limit):
    [value, row, col] = max_value(current_board, -100, 100, limit)
    return [value, row, col]


def max_value(current_board, alpha, beta, limit):
    if limit == 0:
        return evaluation(current_board)
    value = -100
    blank_space = []
    row = -1
    col = -1
    for i in range(8):
        for j in range(8):
            if current_board[i][j] == 0:
                blank_space.append((i, j))
    for (r, c) in blank_space:
        new_board = current_board.place_disc(r, c, -1)
        if new_board is None:
            continue
        else:
            [value_temp, rol_temp, col_temp] = min_value(new_board, alpha, beta, limit-1)
            if value_temp > value:
                value = value_temp
                row = r
                col = c
        if value >= beta:
            return [value, row, col]
        alpha = max(value, alpha)
    return [value, row, col]


def min_value(current_board, alpha, beta, limit):
    if limit == 0:
        return evaluation(current_board)
    value = 100
    blank_space = []
    row = -1
    col = -1
    for i in range(8):
        for j in range(8):
            if current_board[i][j] == 0:
                blank_space.append((i, j))
    for (r, c) in blank_space:
        new_board = current_board.place_disc(r, c, 1)
        if new_board is None:
            continue
        else:
            [value_temp, rol_temp, col_temp] = max_value(new_board, alpha, beta, limit-1)
            if value_temp < value:
                value = value_temp
                row = r
                col = c
        if value <= alpha:
            return [value, row, col]
        beta = min(value, beta)
    return [value, row, col]
