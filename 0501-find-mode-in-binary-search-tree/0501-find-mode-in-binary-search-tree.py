# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        count ={}
        self.max_count =0
        def dfs(node:TreeNode):
            if not node:
                return
            count[node.val] = count.get(node.val,0)+1
            if count[node.val]>self.max_count:
                self.max_count = count[node.val]
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return [key for key,value in count.items() if value ==self.max_count]

        