class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        N = len(s)
        n1 = len(words[0])
        wordcount=len(words)
        total_length = wordcount*n1
        word_freq = Counter(words)
        result = []
        for i in range(N- total_length + 1):
            substring = s[i:i + total_length]
            words_in_substring = [substring[j:j + n1] for j in range(0, total_length, n1)]
            substring_freq = Counter(words_in_substring)
            if substring_freq == word_freq:
                result.append(i)
        return result
            


