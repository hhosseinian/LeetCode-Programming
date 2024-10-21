class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        if m == 1 and n == 1:
            return 1
        row_overlap = float('inf')
        col_overlap = float('inf')
        for  op in ops:
            r,c = op
            row_overlap = min(row_overlap,r)
            col_overlap = min(col_overlap,c)
        return row_overlap*col_overlap

        