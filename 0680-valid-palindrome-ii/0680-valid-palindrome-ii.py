class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome_range(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left,right = 0,len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1  
            else:
                return isPalindrome_range(left+1,right) or isPalindrome_range(left,right-1)
        return True


        