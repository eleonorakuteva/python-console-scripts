def print_board(board):
    for line in board:
        print(*line)
    print()


def can_place_queen(row: int, col: int, rows: set[int], cols: set[int], left_diagonal: set[int], right_diagonal: set[int]):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diagonal:
        return False
    if (row + col) in right_diagonal:
        return False
    return True


def set_queen(row, col, rows, cols, left_diagonals, right_diagonals, board):
    # mark cell (set queen)
    board[row][col] = "Q"
    # add to all sets
    rows.add(row)
    cols.add(col)
    left_diagonals.add((row - col))
    right_diagonals.add((row + col))


def remove_queen(row, col, rows, cols, left_diagonals, right_diagonals, board):
    # unmark the queen
    board[row][col] = "-"
    # remove from all sets
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove((row - col))
    right_diagonals.remove((row + col))


def put_queens(row:int, board: list[list], rows: set[int], cols: set[int], left_diagonal: set[int], right_diagonal: set[int]):
    # base of recursion
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diagonal, right_diagonal):

            # pre-action (backtrack - mark up)
            set_queen(row, col, rows, cols, left_diagonal, right_diagonal, board)

            # recursion
            put_queens(row + 1, board, rows, cols, left_diagonal, right_diagonal)

            # post-action (backtrack - unmark)
            remove_queen(row, col, rows, cols, left_diagonal, right_diagonal, board)


empty_board = [["-"] * 8 for _ in range(8)]

put_queens(0, empty_board, set(), set(), set(), set())


