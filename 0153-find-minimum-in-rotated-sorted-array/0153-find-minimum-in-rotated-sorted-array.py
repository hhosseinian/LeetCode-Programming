class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        if nums[left]<=nums[right]:
            return nums[0]
        while left<=right:
            mid = (left+right)//2
            if (mid == 0 or nums[mid]<nums[mid-1]) and (mid == len(nums)-1 or nums[mid]<nums[mid+1]):
                return nums[mid]
            if nums[mid]<nums[0]:
                right = mid-1
            elif nums[mid]>=nums[0]:
                left = mid+1

        return -1