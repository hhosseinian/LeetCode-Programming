class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split();
        Out = ""
        for i in range(len(words)-1,-1,-1):
            Out += words[i];
            if  i!=0:
                Out += ' ';
        return Out;

        