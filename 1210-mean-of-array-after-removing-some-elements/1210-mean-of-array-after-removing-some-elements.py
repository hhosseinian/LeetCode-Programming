class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        cut_index = n*5//100
        return sum(arr[cut_index:-cut_index])/(n-2*cut_index)