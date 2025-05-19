class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanumeric(l:str)->bool:
            return ('a'<=l<='z') or ('0'<=l<='9')

        n= len(s)
        s = s.lower()
        left,right = 0,n-1
        while left<right:
            while(left<right and not isalphanumeric(s[left])):
                left+=1
                print(left)
            while (left<right and not isalphanumeric(s[right])):
                right-=1
                print(right)
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
