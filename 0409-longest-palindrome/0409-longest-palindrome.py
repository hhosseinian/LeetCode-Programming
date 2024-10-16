class Solution:
    def longestPalindrome(self, s: str) -> int:
        N = len(s)
        result = 0
        if N == 1:
            return 1
        char_freq ={}
        for char in s:
            if char not in char_freq:
                char_freq[char] =1
            else:
                char_freq[char] +=1
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




