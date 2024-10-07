"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def isuniform(x1,y1,x2,y2):
            first_val =grid[x1][y1]
            for i in range(x1,x2):
                for j in range(y1,y2):
                    if grid[i][j] != first_val:
                        return False,None
            return True,first_val
        def Build_tree(x1,y1,x2,y2):
            uniform,value = isuniform(x1,y1,x2,y2)
            if uniform:
                return Node(val =value ==1, isLeaf=True)
            node = Node(val=False, isLeaf=False)
            mid_x =(x1+x2)//2
            mid_y =(y1+y2)//2
            node.topLeft = Build_tree(x1,y1,mid_x,mid_y)
            node.topRight = Build_tree(x1,mid_y,mid_x,y2)
            node.bottomLeft = Build_tree(mid_x,y1,x2,mid_y)
            node.bottomRight = Build_tree(mid_x,mid_y,x2,y2)
            return node
        return Build_tree(0,0,n,n)
