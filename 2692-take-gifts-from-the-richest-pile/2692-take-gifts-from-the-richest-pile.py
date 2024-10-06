import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        Output = sum(gifts)
        max_heap =[-g for g in gifts]
        heapq.heapify(max_heap)
        while max_heap and k>0:
            max_pile = -heapq.heappop(max_heap)
            res = floor(math.sqrt(max_pile))
            Output = Output +(res-max_pile)
            heapq.heappush(max_heap,-res)
            k-=1
        return Output


