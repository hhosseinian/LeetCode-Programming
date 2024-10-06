import heapq
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_heap = list(set(nums))
        heapq.heapify(min_heap)
        Output = 0
        while min_heap:
            smallest = heapq.heappop(min_heap)
            if smallest ==0:
                continue
            Output+=1
            new_heap = []
            while min_heap:
                ext_elem = heapq.heappop(min_heap) - smallest
                if ext_elem>0:
                    new_heap.append(ext_elem)
            for num in new_heap:
                heapq.heappush(min_heap, num)
        return Output