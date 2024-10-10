from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n =len(grid)
        total_pairs = 0
        hash_map = defaultdict(int)
        for row in grid:
            hash_map[tuple(row)] += 1
        for col in range(n):
            column =tuple(grid[row][col]for row in range(n))
            total_pairs +=hash_map[tuple(column)]
        return total_pairs
            


        