class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[float('-inf'),0] for _ in range(3)]
        for price in prices:
            for i in range(2,0,-1):
                # find min buy for ith transaction
                dp[i][0]=max(dp[i][0],dp[i-1][1]-price)
                #find max profit for ith transaction
                dp[i][1] = max(dp[i][1],dp[i][0]+price)
        return dp[2][1]
        ''' first day (outter loop): price1
        iteration i=2 inner loop:
            dp[2] = [-price1,0]
            dp[1] = [-inf,0]
            dp[0] = [-inf,0]
            iteration i=1 inner loop:
            dp[2] = [-price1,0]
            dp[1] = [-price1,0]
            dp[0] = [-inf,0]
        2nd day (outter loop): price2
        iteration i=2 inner loop:
            dp[2] = [max(-price1,-price2),max(-price1,-price2)+price2]
            dp[1] = [-price1,0]
            dp[0] = [-inf,0]
            iteration i=1 inner loop:
            dp[2] = [max(-price1,-price2),max(0,max(-price1,-price2)+price2)]
            dp[1] = [max(-price1,-price2),max(0,max(-price1,-price2)+price2)]
            dp[0] = [-inf,0]
        '''