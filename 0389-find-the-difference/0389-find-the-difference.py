class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_t_letter = {}
        for letter in t:
            if letter not in count_t_letter:
                count_t_letter[letter]=1
            else:
                count_t_letter[letter] += 1
        for letter in s:
            count_t_letter[letter]-=1
        for key,value in count_t_letter.items():
            if value == 1:
                return key
