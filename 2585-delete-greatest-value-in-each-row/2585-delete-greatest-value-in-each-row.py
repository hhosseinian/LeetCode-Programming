class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        Output = 0
        m,n = len(grid),len(grid[0])
        max_heaps = []
        for row in grid:
            max_heap = [-r for r in row]
            heapq.heapify(max_heap)
            max_heaps.append(max_heap)
        while any(max_heaps):
            max_values = []
            for i in range(len(max_heaps)):
                if max_heaps[i]:
                    max_value =-heapq.heappop(max_heaps[i])
                    max_values.append(max_value)
            if max_values:
                Output+=max(max_values)
        return Output