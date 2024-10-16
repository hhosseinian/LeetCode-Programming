class Solution:
    def checkRecord(self, s: str) -> bool:
        count_absence = 0
        cons_late  = 0
        for char in s:
            if char == 'A':
                count_absence+=1
                if count_absence>1:
                    return False
            if char == 'L':
                    cons_late +=1
                    if cons_late>2:
                        return False
            else:
                cons_late = 0
        return True


            