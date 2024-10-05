class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        for index,row in enumerate(mat):
            soldiers = sum(row)
            heapq.heappush(min_heap,(soldiers,index))
        weakest_rows = []
        for _ in range(k):
            weakest_rows.append(heapq.heappop(min_heap)[1])
        return weakest_rows

