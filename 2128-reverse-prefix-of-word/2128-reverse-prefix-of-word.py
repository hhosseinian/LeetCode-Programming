class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        result = ''
        #toggle = True
        for char in word:
            stack.append(char)
            #if stack and toggle and char == ch:
            if stack and char == ch:
                while stack:
                    result+=stack.pop()
                #toggle = False
                break
        i = len(result)
        result+=''.join(word[i:])
        return result
