from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        Freq_dict = {}
        for n in nums:
            if n in Freq_dict:
                return n
            else:
                Freq_dict[n] = 1
        return -1

