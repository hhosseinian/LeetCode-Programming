class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #count_unique_path = 0
        dp = [[0]*(n) for _ in range(m)]
        dp[0][0] = 0
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1   
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] += dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
