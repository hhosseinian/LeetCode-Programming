class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows,cols = len(matrix),len(matrix[0])
        heights = [0]*cols
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c]+=1
                else:
                    heights[c]=0
            max_area = max(max_area,largestRectangleArea(heights))
        return max_area
def largestRectangleArea(heights):
    heights.append(0)
    stack = []
    max_area = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]]>heights[i]:
            h= heights[stack.pop()]
            w = i if not stack else i -stack[-1]-1
            max_area = max(max_area,h*w)
        stack.append(i)
    return max_area