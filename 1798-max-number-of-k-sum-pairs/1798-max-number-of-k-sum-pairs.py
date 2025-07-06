class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
            import collections
            Out = 0
            C = Counter(nums)
            for j,v in C.items():
                k2 = k - j
                if k2 != k:
                    Out += min(C[j],C[k2])
                else:
                    Out += C[j]//2
            return int(Out/2)
                
            
        