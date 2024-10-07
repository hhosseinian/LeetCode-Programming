class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, o = len(s1), len(s2), len(s3)
        if m+n != o:
            return False
        dp =[[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(n+1):
            for j in range(m+1):
                if i>0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if j>0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]

        return dp[n][m]

