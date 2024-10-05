class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row,clm = len(grid),len(grid[0])
        Output = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(row):
            for c in range(clm):
                if grid[r][c] == "1":
                    Output+=1
                    stack = [(r,c)]
                    while stack:
                        x,y = stack.pop()
                        grid[x][y] ="0"
                        for dr,dc in directions:
                            nr, nc = x + dr, y + dc
                            if 0<=nr<row and 0<=nc<clm and grid[nr][nc]=="1":
                                stack.append((nr,nc))
        return Output