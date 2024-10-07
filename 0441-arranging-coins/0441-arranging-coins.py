class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        total_coins = 0
        while total_coins + (k+1) <=n:
            k+=1
            total_coins+= k
        return k