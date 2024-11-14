class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        N=len(candies)
        Mx=max(candies)
        Out=[True]*N
        for i in range(N):
            Out[i]= (candies[i]+extraCandies>=Mx)
        return Out
            
            