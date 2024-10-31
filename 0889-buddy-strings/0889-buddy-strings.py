from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s))<len(s)
        diff_index = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_index.append(i)
        if len(diff_index) ==2:
            return s[diff_index[0]] == goal[diff_index[1]] and s[diff_index[1]] == goal[diff_index[0]]
        return False

