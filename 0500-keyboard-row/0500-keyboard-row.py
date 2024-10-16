class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        kb_rows = {1:set("qwertyuiop"),2:set("asdfghjkl"),3:set("zxcvbnm")}
        result =[]
        for word in words:
            lower_word = word.lower()
            for key,val in kb_rows.items():
                if all(char in val for char in lower_word):
                    result.append(word)
                    break
        return result
