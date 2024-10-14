class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0
        ticket_needed = tickets[k]
        n=len(tickets)
        for i in range(n):
            if i<=k:
                total_time += min(ticket_needed,tickets[i])
            else:
                total_time += min(ticket_needed-1,tickets[i])
        return total_time



