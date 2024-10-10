class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_3Sum =float('inf')
        n = len(nums)
        result = 0
        for i in range(n):
            left,right = i+1,n-1
            while left<right:
                current_sum = nums[i]+nums[left]+nums[right]
                if abs(closest_3Sum-target)>abs(current_sum-target):
                    closest_3Sum = current_sum
                if current_sum<target:
                    left+=1
                elif current_sum>target:
                    right-=1
                else:
                    return current_sum
        return closest_3Sum

