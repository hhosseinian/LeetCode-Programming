class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        result = prices[:]
        for i in range(n-1,-1,-1):
            while stack and prices[i] < stack[-1]:
                stack.pop()
            if stack:
                result[i]=prices[i]-stack[-1]
            stack.append(prices[i])
        return result
                
