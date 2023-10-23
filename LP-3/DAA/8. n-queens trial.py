class Solution:
    def isSafe1(self, row, col, board, n):
        # check upper element
        duprow = row
        dupcol = col
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        return True

    def solve(self, col, board, ans, n, p, q):
        if col == n:
            if(board[p][q] == 'Q'):
                ans.append(list(board))
            return

        for row in range(n):
            if self.isSafe1(row, col, board, n):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solve(col+1, board, ans, n, p, q)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    def solveNQueens(self, n, i, j):
        ans = []
        board = ['.'*n for _ in range(n)]
        self.solve(0, board, ans, n, i, j)
        return ans


print("Enter n for constructing n * x matrix")
n = int(input())
print("Enter p for placing queen")
p = int(input())
print("Enter q for placing queen")
q = int(input())
if p < 0 or p >= n or q < 0 or q >= n:
    print("Invalid starting position.")
else:
    obj = Solution()
    ans = obj.solveNQueens(n, p, q)
    for i in range(len(ans)):
        print(f"Arrangement {i+1}")
        for j in range(len(ans[0])):
            print(ans[i][j])
        print()
