from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t =Counter(t)
        required = len(dict_t) #num of unique char
        s_t_pair = [(i,char) for i, char in enumerate(s) if char in dict_t]
        l,r = 0,0
        included_chars = 0
        window_counts = defaultdict(int)
        min_window = float("inf"), None, None
        while r<len(s_t_pair):
            character = s_t_pair[r][1]  # Current character
            window_counts[character] += 1
            if window_counts[character] == dict_t[character]:
                included_chars += 1

            while l <= r and included_chars == required:
                character = s_t_pair[l][1]  # Character at the left pointer
                start = s_t_pair[l][0]  # Start index of the current window
                end = s_t_pair[r][0]  # End index of the current window
                
                # Update the minimum window
                if end - start + 1 < min_window[0]:
                    min_window = (end - start + 1, start, end)
                
                # Remove the character from the left
                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    included_chars -= 1
                l += 1 
            r+=1
        if min_window[0] == float("inf"):
            return ""
        else:
            return s[min_window[1]:min_window[2] + 1]
        