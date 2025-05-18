class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 1
        n = len(nums)
        
        while ptr2<n:
            while ptr2<n and nums[ptr1] == nums[ptr2]:
                ptr2+=1
            if ptr2<n:
                ptr1+=1
                nums[ptr1]=nums[ptr2]
                ptr2+=1
        return ptr1+1
