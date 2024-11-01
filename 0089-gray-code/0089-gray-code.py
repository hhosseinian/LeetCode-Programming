class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        visited = set()
        def backtrack(code):
            if len(result) == (1<<n):
                return
            result.append(code)
            visited.add(code)
            for i in range(n):  # Try to flip each bit
                next_code = code ^ (1 << i)  # Flip the i-th bit
                if next_code not in visited:  # Ensure we haven't visited this code
                    backtrack(next_code) 
        backtrack(0)
        return result