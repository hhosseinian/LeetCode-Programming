class Solution:
    def reorderSpaces(self, text: str) -> str:
        N_spaces = text.count(' ')
        words =text.split()
        M = len(words)
        result =''
        if M == 0:
            return ' '*N_spaces
        if M == 1:
            return words[0]+ ' '*N_spaces
        Equal_Spaces = ' '*(N_spaces//(M-1))
        remaining_Spaces = ' '*(N_spaces%(M-1))
        result=Equal_Spaces.join(words)+remaining_Spaces
        return result






