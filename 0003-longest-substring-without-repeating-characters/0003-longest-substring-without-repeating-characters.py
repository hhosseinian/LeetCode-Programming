class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        if n<=1:
            return n
        slow,fast = 0,0
        #seen.add(s[slow])
        maxlength = 1 # initial fast-slow+1
        while fast<n and (n-slow>maxlength):
            if s[fast] not in seen:
                maxlength = max(maxlength,fast-slow+1)
                seen.add(s[fast])
                fast+=1
            else:
                seen.remove(s[slow])
                slow+=1
        return maxlength
