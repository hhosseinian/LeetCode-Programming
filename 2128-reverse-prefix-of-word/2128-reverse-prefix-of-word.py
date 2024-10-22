class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        if n==1 or ch not in word:
            return word
        word_list = list(word)
        left, right = 0,0
        i = 0
        while right<n and word[right]!=ch:
            right+=1
        while left<right:
            word_list[left],word_list[right]=word[right],word_list[left]
            left+=1
            right-=1
        return "".join(word_list)
