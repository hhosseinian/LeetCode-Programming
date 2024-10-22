from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_freq = Counter(nums)
        degree = max([freq for freq in num_freq.values()])
        top_degree_digits = []
        for k,v in num_freq.items():
            if v == degree:
                top_degree_digits.append(k)
        min_length = len(nums)
        print(top_degree_digits)
        for digit in top_degree_digits:
            left = nums.index(digit)
            right = len(nums)-1
            while left<=right and nums[right]!=digit:
                right-=1
            min_length =min(min_length,right-left+1)
        return min_length

