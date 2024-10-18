class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        if s == 'a'*n or s == 'b'*n:
            return 1
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return 2
        return 1
    