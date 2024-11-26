class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        T  = len(t);
        S = len(s);
        if s =='': 
            return True;
        ptr = 0;
        j = 0;
        for i in range(T):
            if j == S-1 and t[i] == s[j]:
                return True;
            if j < S-1 and t[i] == s[j]:
                j += 1;
        return False;

                


        