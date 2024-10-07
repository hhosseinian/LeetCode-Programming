class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[float('-inf'),0] for _ in range(k+1)]
        for price in prices:
            for i in range(k,0,-1):
                # find min buy for ith transaction
                dp[i][0]=max(dp[i][0],dp[i-1][1]-price)
                #find max profit for ith transaction
                dp[i][1] = max(dp[i][1],dp[i][0]+price)
        return dp[k][1]