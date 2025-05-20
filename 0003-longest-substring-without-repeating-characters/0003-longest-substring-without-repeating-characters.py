class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n<=1:
            return n
        slow,fast = 0,1
        maxlength = 1 # initial fast-slow+1
        while fast<n:
            if s[fast] not in s[slow:fast]:
                maxlength = max(maxlength,fast-slow+1)
                fast+=1
            else:
                slow+=1
            if n-slow<=maxlength:
                break
        return maxlength
