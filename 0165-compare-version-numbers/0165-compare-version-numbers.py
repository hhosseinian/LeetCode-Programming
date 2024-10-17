class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        digits1 = list(map(int, version1.split('.')))
        digits2 = list(map(int, version2.split('.')))
        n1 = len(digits1)
        n2 = len(digits2)
        max_lenghs = max(n1,n2)
        i=0
        for i in range(max_lenghs):
            v1 = digits1[i] if i<n1 else 0
            v2 = digits2[i] if i<n2 else 0
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
            i+=1
        return 0

