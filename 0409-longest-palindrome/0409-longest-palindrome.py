from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        char_freq = Counter(s)
        has_odd = False
        for key,val in char_freq.items():
            if val%2 == 0:
                result+=val
            elif val%2 == 1:
                result+=val-1
                has_odd = True
        if has_odd:
            result+= 1
        return result




