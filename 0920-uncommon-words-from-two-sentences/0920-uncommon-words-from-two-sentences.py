from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        s1_words = s1.split(' ')
        s2_words = s2.split(' ')
        s1_counter = Counter(s1_words)
        for word in s2_words:
            if word in s1_counter:
                s1_counter[word]+= 1
            else:
                s1_counter[word] = 1
        for k,v in s1_counter.items():
            if v ==1:
                result.append(k)
        return result

        