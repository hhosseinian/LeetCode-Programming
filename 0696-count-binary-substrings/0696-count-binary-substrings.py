class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        prev_count = 0  # Count of the previous group (0s or 1s)
        curr_count = 1  # Count of the current group
        result = 0

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_count += 1  # Increase count of current group
            else:
                # We've encountered a different character
                result += min(prev_count, curr_count)  # Count valid substrings
                prev_count = curr_count  # Update previous count
                curr_count = 1  # Reset current count

        # Count valid substrings for the last group
        result += min(prev_count, curr_count)

        return result