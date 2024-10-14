class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        n=len(tickets)
        ptr = 0
        while tickets[k]!=0:
            if tickets[ptr%n]!=0:
                tickets[ptr%n]-=1
                result+=1
            ptr+=1
        return result



