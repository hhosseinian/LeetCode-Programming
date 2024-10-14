from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        if n == 1:
            return "Dire" if senate == 'D' else "Radiant"
        Dqueue = deque()
        Rqueue = deque()
        for index,party in enumerate(senate):
            if party == 'R':
                Rqueue.append(index)
            else:
                Dqueue.append(index)
        while Dqueue and Rqueue:
            R_index = Rqueue.popleft()
            D_index = Dqueue.popleft()
            if R_index<D_index:
                Rqueue.append(R_index+n)
            else:
                Dqueue.append(R_index+n)
        return "Dire" if Dqueue else "Radiant" 
