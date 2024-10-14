from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D_count = senate.count('D')
        R_count = senate.count('R')
        n = len(senate)
        R_ptr=0
        skipped = 0
        while D_count>0 and R_count>0:
            while R_ptr<n and senate[R_ptr] == 'X':
                R_ptr+=1
            if R_ptr == n:
                R_ptr = 0
            if senate[R_ptr] == 'R':
                D_count -= 1
                banned = (R_ptr+1)%n
                while senate[banned]!='D':
                    banned=(banned+1)%n
                senate =senate[:banned]+'X'+senate[banned+1:]
            elif senate[R_ptr] == 'D':
                R_count -= 1
                banned = (R_ptr+1)%n
                while senate[banned]!='R':
                    banned=(banned+1)%n
                senate =senate[:banned]+'X'+senate[banned+1:]
            R_ptr+=1
        return "Radiant" if R_count>0 else "Dire"

                

