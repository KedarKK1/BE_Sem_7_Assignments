    # # Check the left side of this row
    # for i in range(col):
    #     if board[row][i] == 1:
    #         return False

def is_safe(board, row, col, n):
    # Check the left side of the current column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the right side
    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            board[i][col] = 0
            print("I ", i, col)
    return False

def print_board(board):
    for row in board:
        print(" ".join(["Q" if x else "." for x in row]))

def main():
    n = int(input("Enter the value of N: "))
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Get the user's choice of starting position (i, j)
    i = int(input("Enter the row (0 to {}): ".format(n-1)))
    j = int(input("Enter the column (0 to {}): ".format(n-1)))

    if i < 0 or i >= n or j < 0 or j >= n:
        print("Invalid starting position.")
        return

    board[i][j] = 1

    # if solve_n_queens(board, j + 1, n):
    if solve_n_queens(board, 0, n):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
