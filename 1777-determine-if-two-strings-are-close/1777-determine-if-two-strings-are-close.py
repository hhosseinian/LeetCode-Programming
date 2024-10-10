from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) !=len(word2):
            return False
        freq_hashmap1 = defaultdict(int)
        freq_hashmap2 = defaultdict(int)
        for letter1 in word1:
            freq_hashmap1[letter1]+=1
        for letter2 in word2:
            freq_hashmap2[letter2]+=1
        return set(freq_hashmap1.keys()) == set(freq_hashmap2.keys()) and (sorted(freq_hashmap1.values())==sorted(freq_hashmap2.values()))