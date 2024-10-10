class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        N = len(s)

        left,right =0,N-1
        while left<right:
            if not s_list[left].isalpha():
                left+=1
            if not s_list[right].isalpha():
                right-=1
            if s_list[left].isalpha() and s_list[right].isalpha():
                s_list[left],s_list[right]=s_list[right],s_list[left]
                left+=1
                right-=1
        return ''.join(s_list)

            
