class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        S = len(s)
        G = len(g)
        if S == 0:
            return 0
        g.sort()
        s.sort()
        g_ptr,s_ptr = 0,0
        result = 0
        while s_ptr<S and g_ptr<G:
            if s[s_ptr]>=g[g_ptr]:
                result+=1
                g_ptr+=1
            s_ptr +=1
        return result