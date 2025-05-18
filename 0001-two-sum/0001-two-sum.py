class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_dict = {}
        for i,n in enumerate(nums):
            if target-n in checked_dict:
                return [checked_dict[target-n],i]
            else:
                checked_dict[n] = i
            