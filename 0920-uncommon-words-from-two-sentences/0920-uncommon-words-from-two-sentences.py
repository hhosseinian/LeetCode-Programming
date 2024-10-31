from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words
        s1_words = s1.split()
        s2_words = s2.split()
        
        # Create a Counter for all words in both sentences
        word_count = Counter(s1_words + s2_words)
        
        # Collect words that occur exactly once
        result = [word for word, count in word_count.items() if count == 1]
        
        return result
