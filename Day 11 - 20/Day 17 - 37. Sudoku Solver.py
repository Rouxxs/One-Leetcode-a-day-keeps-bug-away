class Solution:
    def possible(self, r: int, c: int, num, board) -> bool:
        for i in range(9):
            if (board[r][i] == num):
                return False
            if (board[i][c] == num): 
                return False
        r0 = (r//3) * 3
        c0 = (c//3) * 3

        for i in range(3):
            for j in range(3):
                if (board[r0 + i][c0 + j] == num):
                    return False
        return True

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in range(9):
                        n = chr(ord('1')+num)
                        if self.possible(r, c, n, board):
                            board[r][c] = n
                            if self.solve(board): return True
                            board[r][c] = "."
                    return False
        return True
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        return

        
        