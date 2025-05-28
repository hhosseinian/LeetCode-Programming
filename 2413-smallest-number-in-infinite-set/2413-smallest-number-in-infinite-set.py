class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.addedback = []
        self.addedset = set()

    def popSmallest(self) -> int:
        if self.addedback:
            smallest = heapq.heappop(self.addedback)
            self.addedset.remove(smallest)
            return smallest
        else:
            smallest = self.current
            self.current+=1
            return smallest

    def addBack(self, num: int) -> None:
        if num<self.current and num not in self.addedset:
            heapq.heappush(self.addedback,num)
            self.addedset.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)