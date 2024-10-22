class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        if n == 0:
            return True
        if m == 1 and flowerbed[0] ==1:
            return False
        for i in range(0,m):
            if flowerbed[i] == 0 and(i == 0 or flowerbed[i-1] == 0)and(i == m-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n-=1
        return n<=0
