class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n<=2:
            return 1
        F = [0]*(n+1)
        F[1],F[2] =1,1
        for i in range(n-2):
            F[i+3]=F[i]+F[i+1]+F[i+2]
        return F[n]

        