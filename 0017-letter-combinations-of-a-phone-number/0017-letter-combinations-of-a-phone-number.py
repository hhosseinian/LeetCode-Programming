class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_char = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def backtrack(index,path):
            if index == len(digits):
                combinations.append("".join(path))
                return
            current_digit =digits[index]
            possible_letters =digit_to_char[current_digit]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1,path)
                path.pop()
        combinations = []
        backtrack(0,[])
        return combinations