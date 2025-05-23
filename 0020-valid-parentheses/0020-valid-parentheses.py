class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            if l in '([{':
                stack.append(l)
            else:
                if stack and ((l == ')' and stack[-1] =='(') or (l == ']' and stack[-1] =='[') or (l == '}' and stack[-1] =='{')):
                    stack.pop()
                else:
                    return False
        return not stack

        