from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_freq = Counter(s)
        result = 0
        has_odd = False
        for count in char_freq.values():
            result += count // 2 * 2  # Add the largest even part
            if count % 2 == 1:
                has_odd = True
        if has_odd:
            result+=1
        return result
