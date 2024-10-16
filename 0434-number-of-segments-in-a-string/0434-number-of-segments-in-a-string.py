class Solution:
    def countSegments(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        result = 0
        i = 0
        in_segment = False
        for i in range(n):
            if s[i] != ' ':
                if not in_segment:
                    result+=1
                    in_segment = True
            else:
                in_segment = False
        return result
