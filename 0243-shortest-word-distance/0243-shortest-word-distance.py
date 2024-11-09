class Solution:
    def shortestDistance(self, wordsDict, word1, word2):
        index1 = index2 = -1  # Initialize indices to -1 (not found yet)
        min_distance = float('inf')  # Set the initial min distance to infinity
    
        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i  # Update index for word1
            elif word == word2:
                index2 = i  # Update index for word2
        
            # If both word1 and word2 have been found, update the minimum distance
            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))
    
        return min_distance