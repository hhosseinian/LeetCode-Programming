from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        Freq_dict = Counter(nums)
        max_value = max(Freq_dict.values())
        for k, v in Freq_dict.items():
            if v == max_value:
                keys_with_max_value = k
        return keys_with_max_value