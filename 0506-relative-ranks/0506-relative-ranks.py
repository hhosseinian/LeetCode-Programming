import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        max_heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(max_heap)
        Output = [""]*n
        for rank in range(1,n+1):
            score_value, index = heapq.heappop(max_heap)
            if rank == 1:
                Output[index] = "Gold Medal"
            elif rank == 2:
                Output[index] = "Silver Medal"
            elif rank == 3:
                Output[index] = "Bronze Medal"
            else:
                Output[index] = str(rank)
        return Output
