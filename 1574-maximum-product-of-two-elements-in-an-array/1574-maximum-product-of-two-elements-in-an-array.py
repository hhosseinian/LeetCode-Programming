import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap =[]
        for n in nums:
            heapq.heappush(max_heap,-n)
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        return (first-1)*(second-1)
        