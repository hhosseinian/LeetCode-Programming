class Solution:
    def countSegments(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        result = 0
        i = 0
        segment = ''
        while i <n:
            if s[i] == ' ' and segment!='':
                result+=1
                segment = ''
            elif s[i] != ' ':
                segment+=s[i]
            i+=1
        if segment!='':
            result+=1
        return result
