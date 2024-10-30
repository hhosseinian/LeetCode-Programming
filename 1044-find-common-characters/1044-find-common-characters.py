from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        common_count = Counter(words[0])
        for w in words[1:]:
            curr_count = Counter(w)
            for char in common_count:
                if char in curr_count:
                    common_count[char] = min(common_count[char],curr_count[char])
                else:
                    common_count[char] = 0 
        for k,v in common_count.items():
            for i in range(v):
                result.append(k)
        return result
            



        