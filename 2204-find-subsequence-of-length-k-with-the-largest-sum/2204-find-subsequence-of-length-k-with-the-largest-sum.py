import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        max_heap =[]
        for i in range(len(nums)):
            heapq.heappush(max_heap,(-nums[i],i))
        res = []
        for _ in range(k):
            v,inx = heapq.heappop(max_heap)
            res.append(inx)
        res.sort()
        return [nums[k] for k in res]