class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col = len(board), len(board[0])
        if row<=2 or col<=2:
            return board
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def iterative_dfs(start_r,start_c):
            stack = [(start_r,start_c)]
            while stack:
                r,c =stack.pop()
                board[r][c]='M'
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<row and 0<=nc<col and board[nr][nc] =='O':
                        stack.append((nr,nc))
        for r in range(row):
            for c in range(col):
                if (r ==0 or r==row-1 or c ==0 or c==col-1) and board[r][c] =='O':
                    iterative_dfs(r, c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'M':
                    board[r][c] = 'O'


        