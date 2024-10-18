class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        averages = set()
        for i in range(n//2):
            averages.add((nums[i]+nums[n-1-i])/2)
            
        return min(averages)