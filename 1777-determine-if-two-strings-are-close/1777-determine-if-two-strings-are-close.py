from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # Use Counter to count frequencies directly
        freq_counter1 = Counter(word1)
        freq_counter2 = Counter(word2)
        
        # Compare the unique characters and their frequencies
        return (freq_counter1.keys() == freq_counter2.keys() and 
                sorted(freq_counter1.values()) == sorted(freq_counter2.values()))
