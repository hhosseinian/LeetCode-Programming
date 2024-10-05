import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        odd_digits = []
        even_digits = []
        res = []
        Output =0
        while (num>0):
            temp = num%10
            res.append(temp)
            if temp%2 == 0:
                even_digits.append(-temp)
            else:
                odd_digits.append(-temp)
            num= num//10
        heapq.heapify(odd_digits)
        heapq.heapify(even_digits)
        for r in reversed(res):
            if r%2 ==0:
                Output=Output*10-heapq.heappop(even_digits)
            else:
                Output=Output*10-heapq.heappop(odd_digits)
        return Output


        
        


