def print_matrix(mx):
    for r in mx:
        print(r)


def place_player_choice(mx, rows, col, player_n):
    for r_idx in range(rows - 1, -1, -1):
        if mx[r_idx][col - 1] == 0:
            mx[r_idx][col - 1] = player_n
            return r_idx, col


def is_column_full(mx, rows, col):
    is_available = False
    for r_idx in range(rows - 1, -1, -1):
        if mx[r_idx][col - 1] == 0:
            is_available = True
            break
    return is_available


def validate_idx(mx, mx_r, mx_c, row, col, player_n):
    if row < 0 or col < 0 or row >= mx_r or col >= mx_c:
        return False
    if mx[row][col] == player_n:
        return True


def horizontal_line(mx, mx_r, mx_c, row, col, player_n, slots_count=4):
    right_side = [validate_idx(mx, mx_r, mx_c, row, col + i, player_n) == player_n for i in range(slots_count)].count(
        True)
    left_side = [validate_idx(mx, mx_r, mx_c, row, col - 1 - i, player_n) == player_n for i in
                 range(slots_count)].count(True)
    return right_side + left_side >= 4


def vertical_line(mx, mx_r, mx_c, row, col, player_n, slots_count=4):
    up = [validate_idx(mx, mx_r, mx_c, row - i, col, player_n) == player_n for i in range(slots_count)].count(True)
    down = [validate_idx(mx, mx_r, mx_c, row + i, col, player_n) == player_n for i in range(1, slots_count + 1)].count(
        True)
    return up + down >= 4


def primary_diagonal(mx, mx_r, mx_c, row, col, player_n, slots_count=4):
    left_right_line = [validate_idx(mx, mx_r, mx_c, row + i, col + i, player_n) == player_n for i in
                       range(slots_count)].count(True)
    right_left_line = [validate_idx(mx, mx_r, mx_c, row - i, col - i, player_n) == player_n for i in
                       range(1, slots_count + 1)].count(True)
    return right_left_line + left_right_line >= 4


def secondary_diagonal(mx, mx_r, mx_c, row, col, player_n, slots_count=4):
    left_right_line = [validate_idx(mx, mx_r, mx_c, row - i, col + i, player_n) == player_n for i in
                       range(slots_count)].count(True)
    right_left_line = [validate_idx(mx, mx_r, mx_c, row + i, col - i, player_n) == player_n for i in
                       range(1, slots_count + 1)].count(True)
    return right_left_line + left_right_line >= 4


def check_result(mx, mx_r, mx_c, row, col, player_n, slots_count=4):
    is_horizontal = horizontal_line(mx, mx_r, mx_c, row, col, player_n, slots_count=4)
    is_vertical = vertical_line(mx, mx_r, mx_c, row, col, player_n, slots_count=4)
    is_primary_diagonal = (primary_diagonal(mx, mx_r, mx_c, row, col, player_n, slots_count=4))
    is_secondary_diagonal = (secondary_diagonal(mx, mx_r, mx_c, row, col, player_n, slots_count=4))
    return any([is_horizontal, is_vertical, is_primary_diagonal, is_secondary_diagonal])
