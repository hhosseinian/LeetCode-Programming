class Solution:
    def reverseWords(self, s: str) -> str:
        words =[]
        n = len(s)
        i = 0
        while(i<n):
            word = ''
            while i<n and s[i]== ' ':
                i+=1
            while i<n and s[i]!= ' ':
                word+=s[i]
                i+=1
            if word:
                words.append(word)
        return ' '.join(reversed(words))
                

