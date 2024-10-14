class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        n=len(tickets)
        ptr = 0
        while tickets[k]>0:
            if tickets[ptr]>0:
                tickets[ptr]-=1
                result+=1
            ptr = (ptr+1)%n
        return result



