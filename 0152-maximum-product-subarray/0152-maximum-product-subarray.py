class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        left = 1
        right = 1
        for i in range(n):
            left *= nums[i]
            right *= nums[n-1-i]
            result = max(result,left,right)
            if left ==0:
                left = 1
            if right ==0:
                right =1
        return result