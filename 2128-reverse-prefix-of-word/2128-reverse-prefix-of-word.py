class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        result = ''
        toggle = True
        for char in word:
            stack.append(char)
            if stack and toggle and char == ch:
                while stack:
                    result+=stack[-1]
                    stack.pop()
                toggle = False
        result+=''.join(stack)
        return result
