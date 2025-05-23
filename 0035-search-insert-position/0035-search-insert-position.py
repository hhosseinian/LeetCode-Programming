class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid =(left+right)//2
            print(left,right,mid)
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
            print('after:',left,right,mid)
        return left