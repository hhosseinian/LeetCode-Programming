class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')  # Remove spaces
        stack = []
        current_number = 0
        sign = 1  # Start with a '+' operation
        n = len(s)
        Output = 0
        for i in range(n):
            char = s[i]
            
            if char.isdigit():
                current_number = current_number * 10 + int(char)  # Build the current number
            
            # If we reach an operator or the end of the string
            elif char in "+-":
                Output += current_number*sign
                current_number = 0
                if char == '+':
                    sign =1
                else:
                    sign =-1
            elif char =='(':
                stack.append(Output)
                stack.append(sign)
                sign = 1
                Output = 0
            elif char == ')':
                Output += current_number*sign
                Output *= stack.pop()
                Output+= stack.pop()
                current_number = 0
        return Output+current_number*sign
