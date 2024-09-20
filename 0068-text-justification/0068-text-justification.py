class Solution:
    def fullJustify(self,words, maxWidth):
        result = []
        current_line = []
        num_of_letters = 0
    
        for word in words:
            # Check if we can add the word to the current line
            if num_of_letters + len(word) + len(current_line) > maxWidth:
                # Justify the current line
                for i in range(maxWidth - num_of_letters):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                current_line = []
                num_of_letters = 0
        
            # Add the word to the current line
            current_line.append(word)
            num_of_letters += len(word)
    
        # Handle the last line
        result.append(' '.join(current_line).ljust(maxWidth))
    
        return result