import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = []
        Output = 0
        for a in amount:
            heapq.heappush(max_heap,-a)
        while len(max_heap) > 1:
            first_largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)
            if first_largest == 0:
                return 0
            Output+=1
            if first_largest>1:
                heapq.heappush(max_heap,-(first_largest-1))
            if second_largest>1:
                heapq.heappush(max_heap,-(second_largest-1))
        if max_heap:
            Output-=max_heap[0]
        return Output


        
        