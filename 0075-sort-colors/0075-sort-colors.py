class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0:0,1:0,2:0}
        for n in nums:
            count[n]+=1
        nums[0:count[0]]=[0]*(count[0])
        nums[count[0]:count[0]+count[1]]=[1]*(count[1])
        nums[count[0]+count[1]:len(nums)]=[2]*(count[2])
        