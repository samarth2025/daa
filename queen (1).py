def print_board(board):
    """Print the chessboard matrix."""
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe."""
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    """Use backtracking to place queens from the given row onwards."""
    if row >= n:
        return True  # All queens are placed successfully

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen

            if solve_nqueens(board, row + 1, n):
                return True  # Recurse for the next row

            board[row][col] = 0  # Backtrack

    return False  # No solution found


def n_queens_with_first_queen(n, first_row, first_col):
    """Initialize the board and place the first queen."""
    board = [[0] * n for _ in range(n)]  # Create an empty n x n board
    board[first_row][first_col] = 1  # Place the first queen

    if solve_nqueens(board, first_row + 1, n):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists for this configuration.")


# User input
n = int(input("Enter the size of the chessboard (n): "))
first_row = int(input("Enter the row index of the first queen (0 to n-1): "))
first_col = int(input("Enter the column index of the first queen (0 to n-1): "))

# Ensure valid input
if 0 <= first_row < n and 0 <= first_col < n:
    n_queens_with_first_queen(n, first_row, first_col)
else:
    print("Invalid position for the first queen.")
