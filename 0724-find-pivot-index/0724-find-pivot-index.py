class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        P =[0]*N
        for i in range(1,N):
            P[i] = P[i-1] + nums[i-1]
        for j in range(N):
            Left = P[j]
            Right = P[-1] - P[j] + nums[-1] - nums[j]
            if Left == Right:
                return j
        return -1
            
        