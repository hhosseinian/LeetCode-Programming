class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def FindLast(nums,target):
            left,right = 0, len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] <= target:
                    left = mid+1
                else:
                    right = mid-1
            return right
        def FindFirst(nums,target):
            left,right = 0, len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] >= target:
                    right = mid-1
                else:
                    left = mid+1
            return left
        first = FindFirst(nums,target)
        last = FindLast(nums,target)
        if first<=last and nums[first] == target:
            return [first,last]
        return[-1,-1]
                    




