class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        N =len(self.grid)
        for r in range(N):
            for c in range(N):
                if self.grid[r][c] == value:
                    top = self.grid[r-1][c] if r>0 else 0
                    bottom = self.grid[r+1][c] if r<N-1 else 0
                    left= self.grid[r][c-1] if c>0 else 0
                    right =self.grid[r][c+1] if c<N-1 else 0
                    return top+bottom+left+right

    def diagonalSum(self, value: int) -> int:
        N =len(self.grid)
        for r in range(N):
            for c in range(N):
                if self.grid[r][c] == value:
                    topleft = self.grid[r-1][c-1] if r>0 and c>0 else 0
                    topright = self.grid[r-1][c+1] if r>0 and c<N-1 else 0
                    bottomleft= self.grid[r+1][c-1] if r<N-1 and c>0 else 0
                    bottomright =self.grid[r+1][c+1] if r<N-1 and c<N-1 else 0
                    return topleft+topright+bottomleft+bottomright


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)