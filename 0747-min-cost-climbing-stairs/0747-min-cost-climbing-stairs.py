class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n,prev1,prev2=len(cost),cost[1],cost[0]
        for i in range(2,n):
            curr = cost[i]+min(prev1,prev2)
            prev2,prev1 = prev1,curr
        return min(prev1,prev2)

