class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, num):
            for x in range(9):
                if board[row][x] == num:
                    return False
            for x in range(9):
                if board[x][col] == num:
                    return False       
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[i+startRow][j+startCol] == num:
                        return False
            return True
        def solver(Board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in '123456789':
                            if isValid(board, r, c, num):
                                board[r][c] = num
                                if solver(board):
                                    return True
                                board[r][c] = '.'
                        return False
            return True
        solver(board)

