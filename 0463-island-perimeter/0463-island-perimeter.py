class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows>=1 else 0
        perimeter = 0
        def dfs(i,j):
            nonlocal perimeter
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr,dc in directions:
                nr,nc = i+dr,j+dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc] ==0:
                    perimeter+=1
                elif grid[nr][nc] ==1:
                    grid[nr][nc] =2
                    dfs(nr,nc)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1:
                    grid[i][j] =2
                    dfs(i,j)
                    return perimeter
        return perimeter
                



        