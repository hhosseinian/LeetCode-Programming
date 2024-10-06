import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        min_heap = nums
        heapq.heapify(min_heap)
        arr =[]
        while min_heap:
            Alice = heapq.heappop(min_heap)
            Bob = heapq.heappop(min_heap)
            arr.append(Bob)
            arr.append(Alice)
        return arr

        