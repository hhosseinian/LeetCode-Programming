from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        current_num = 0
        current_str = ""
        for char in s:
            if char.isdigit():
                current_num = 10*current_num + int(char)
            elif char == '[':
                stack.append((current_str,current_num))
                current_num = 0
                current_str = ""
            elif char == ']':
                last_str,last_num =stack.pop()
                current_str = last_str + current_str*last_num
            else:
                current_str+=char
        return current_str



