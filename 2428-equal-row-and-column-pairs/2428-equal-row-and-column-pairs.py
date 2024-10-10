from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n =len(grid)
        if n ==1:
            return 1
        total_pairs = 0
        hash_map = defaultdict(int)
        for row in grid:
            hash_map[tuple(row)] += 1
        for col in range(n):
            column = []
            for row in range(n):
                column.append(grid[row][col])
            total_pairs +=hash_map[tuple(column)]
        return total_pairs
            


        