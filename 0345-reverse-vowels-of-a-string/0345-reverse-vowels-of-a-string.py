class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        n = len(s)
        if n == 1:
            return s
        left,right = 0,n-1
        while left<=right:
            while(s[left] not in vowels and left<right):
                left+=1
            while(s[right] not in vowels and left<right):
                right -=1
            if left<right:
                s_list[left],s_list[right]=s_list[right],s_list[left]
            left+=1
            right -=1
        return "".join(s_list)