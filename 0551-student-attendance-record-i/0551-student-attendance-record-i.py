class Solution:
    def checkRecord(self, s: str) -> bool:
        count_absence = 0
        cons_late  = 0
        for char in s:
            if char == 'A':
                count_absence+=1
            if char == 'L':
                    cons_late +=1
            else:
                cons_late = 0
            if count_absence>1 or cons_late>2:
                return False
        return True