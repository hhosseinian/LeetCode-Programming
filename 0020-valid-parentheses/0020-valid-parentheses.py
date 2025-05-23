class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match ={')':'(',']':'[','}':'{'}
        for l in s:
            if l in '([{':
                stack.append(l)
            else:
                if stack and stack[-1] == match[l]:
                    stack.pop()
                else:
                    return False
        return not stack

        