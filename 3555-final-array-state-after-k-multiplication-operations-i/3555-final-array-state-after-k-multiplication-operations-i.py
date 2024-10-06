import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap =[]
        for i,v in enumerate(nums):
            heapq.heappush(min_heap,(v,i))
        for _ in range(k):
            (x,inx)= heapq.heappop(min_heap)
            heapq.heappush(min_heap,(x*multiplier,inx))
            nums[inx] *=multiplier
        #results = [0]*len(nums)
        #while min_heap:
        #    (x,inx)= heapq.heappop(min_heap)
        #    results[inx] = x
        return nums
        