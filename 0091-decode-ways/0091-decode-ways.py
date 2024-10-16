class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0 or s[0] == '0':
            return 0
        dp = [0]*(N+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,N+1):
            if '1'<=s[i-1] <='9':
                dp[i] += dp[i-1]
            if '10'<=s[i-2:i] <='26':
                dp[i] += dp[i-2]
        return dp[N]

