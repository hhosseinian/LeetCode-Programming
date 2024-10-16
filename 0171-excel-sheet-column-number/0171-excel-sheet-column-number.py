class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result*=26
            result += ord(char)-ord('A')+1
        return result
