class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        S = len(s)
        G = len(g)
        g.sort()
        s.sort()
        g_ptr,s_ptr = 0,0
        while s_ptr<S and g_ptr<G:
            if s[s_ptr]>=g[g_ptr]:
                g_ptr+=1
            s_ptr +=1
        return g_ptr