class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        if arr[-1]<0:
            return -1
        for i in range(len(arr)):
            if arr[i]==i:
                return i
        return -1