class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 1
        left = 0
        right = 0
        for right in range(1,n):
            if nums[right]<=nums[right-1]:
                max_length = max(max_length,right-left)
                left = right
        return max(max_length,right-left+1)

