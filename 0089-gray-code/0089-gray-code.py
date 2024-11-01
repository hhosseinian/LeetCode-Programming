class Solution:
    def grayCode(self, n: int) -> List[int]:
        output = []
        for i in range(1<<n):
            output.append((i>>1)^i)
        return output