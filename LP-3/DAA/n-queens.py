    # # Check the left side of this row
    # for i in range(col):
    #     if board[row][i] == 1:
    #         return False

def is_safe(board, row, col, n):
    # Check the left side of the current column
    for i in range(n):
        if col != i and board[row][i] == 1:
            return False
        
    # Check the vertical side of the current column
    for i in range(n):
        if i != row and board[i][col] == 1:
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

def solve_n_queens(board, col, n, alreadyi, alreadyj):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens(board, col + 1, n, alreadyi, alreadyj):
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
    if solve_n_queens(board, 0, n, i, j):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()

# def is_safe(board, row, col, n):
#     # Check the left side of this row
#     for i in range(col):
#         if board[row][i] == 1:
#             return False

#     # Check upper diagonal on the left side
#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     # Check lower diagonal on the left side
#     for i, j in zip(range(row, n, 1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     return True

# def print_board(board):
#     for row in board:
#         print(" ".join(["Q" if x else "." for x in row]))

# def main():
#     n = int(input("Enter the value of N: "))
#     board = [[0 for _ in range(n)] for _ in range(n)]

#     i = int(input("Enter the row (0 to {}): ".format(n - 1)))
#     j = int(input("Enter the column (0 to {}): ".format(n - 1)))

#     if i < 0 or i >= n or j < 0 or j >= n:
#         print("Invalid starting position.")
#         return

#     def solve_n_queens_modified(board, col, n, i, j):
#         if col >= n:
#             return True

#         for k in range(i, n):
#             for l in range(j, n):
#                 if k == i and l == j:
#                     continue
#                 if is_safe(board, k, l, n):
#                     board[k][l] = 1

#                     if solve_n_queens_modified(board, col + 1, n, i, j):
#                         return True

#                     board[k][l] = 0

#         return False

#     if solve_n_queens_modified(board, 0, n, i, j):
#         print("Solution found:")
#         print_board(board)
#     else:
#         print("No solution exists.")

# if __name__ == "__main__":
#     main()
