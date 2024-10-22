class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i -stack[-1]-1
                max_area = max(max_area,h*w)
                print((i,h*w,max_area))
            stack.append(i)
        return max_area