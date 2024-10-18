class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        groups = []
        count = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                print(f'Group: {count}')
                groups.append(count)
                count = 1
        groups.append(count)
        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i - 1], groups[i])
        return result