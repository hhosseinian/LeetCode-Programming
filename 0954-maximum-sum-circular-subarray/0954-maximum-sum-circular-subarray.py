class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_sum = current_sum = nums[0]
            for num in nums[1:]:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum

        total_sum = sum(nums)
        max_kadane = kadane(nums)  # Maximum subarray sum (non-circular)
        min_kadane = kadane([-num for num in nums])  # Maximum negative sum => Minimum positive sum
        max_circular = total_sum + min_kadane  # Circular subarray sum
    
        # If all elements are negative, max_circular should not be considered
        if max_circular == 0:  # This occurs if all numbers are negative
            return max_kadane
    
        return max(max_kadane, max_circular)