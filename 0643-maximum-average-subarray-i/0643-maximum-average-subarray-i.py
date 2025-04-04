class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]
        current_sum = sum(nums[0:k])
        max_sum = current_sum
        for i in range(k,n):
            current_sum += (nums[i]-nums[i-k])
            max_sum = max(max_sum,current_sum)
        return max_sum/k
