import heapq
class MedianFinder:

    def __init__(self):
        #upper half
        self.min_heap = []
        #lower half
        self.max_heap = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        if self.max_heap and self.min_heap and (-self.max_heap[0]>self.min_heap[0]):
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)
        if len(self.max_heap) > len(self.min_heap) + 1:
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)
        elif len(self.min_heap) > len(self.max_heap):
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0]-self.max_heap[0])/2
        else:
            return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()