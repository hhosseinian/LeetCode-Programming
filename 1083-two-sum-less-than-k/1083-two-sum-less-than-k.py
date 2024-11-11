class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1  # Initialize the result to -1, indicating no valid pair found
        n = len(nums)
    
        # Iterate over all pairs (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                current_sum = nums[i] + nums[j]
                if current_sum < k:
                    max_sum = max(max_sum, current_sum)  # Update the max_sum if the condition is met
    
        return max_sum