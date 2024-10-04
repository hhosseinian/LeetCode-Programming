class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m,n = len(board),len(board[0])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        cp_board = [row[:] for row in board]

        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n:
                        live_neighbors += cp_board[nr][nc]
                if cp_board[r][c] == 1:
                    if live_neighbors<2 or live_neighbors>3:
                        board[r][c] =0
                    else:
                        board[r][c] =1
                else:
                    if live_neighbors==3:
                        board[r][c] =1


                
        