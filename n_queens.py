class Solution:
    def solveNQueens(self, n: int):
        def f(row):
            if row == n:
                return [["".join(line) for line in board]]
            solutions = []
            for col in range(n):
                if col in columns or row-col in diag1 or row+col in diag2:
                    continue
                board[row][col] = "Q"
                columns.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                solutions.extend(f(row+1))
                board[row][col] = "."
                columns.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
            return solutions
        board = [["."]*n for _ in range(n)]
        columns, diag1, diag2 = set(), set(), set()
        return f(0)