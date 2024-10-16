class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        kb_rows = {1:"qwertyuiop",2:"asdfghjkl",3:"zxcvbnm"}
        result =[]
        for word in words:
            for key,val in kb_rows.items():
                if all(char in val for char in word.lower()):
                    result.append(word)
                    break
        return result
