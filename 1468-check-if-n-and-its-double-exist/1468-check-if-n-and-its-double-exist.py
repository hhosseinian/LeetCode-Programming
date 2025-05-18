class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}
        for a in arr:
            if 2*a in seen or (a%2==0 and a/2 in seen):
                return True
            else:
                seen[a] = True
        return False
                