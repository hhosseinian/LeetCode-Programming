class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        checked = {}
        wordset = set(wordDict)
        def backtrack(start):
            if start in checked:
                return checked[start]
            if start == len(s):
                return [""]
            results = []
            for end in range(start+1,len(s)+1):
                word = s[start:end]
                if word in wordset:
                    for sub_sentence in backtrack(end):
                        if sub_sentence:
                            results.append(word+" "+sub_sentence)
                        else:
                            results.append(word)
            checked[start] = results
            return results
        return backtrack(0)


