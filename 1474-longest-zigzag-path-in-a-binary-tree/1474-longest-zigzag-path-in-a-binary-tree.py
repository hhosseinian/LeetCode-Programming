# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def maxZigZag(node: Optional[TreeNode], is_left:bool,length)->None:
            nonlocal max_length
            if not node:
                return
            max_length = max(max_length, length)
            if is_left:
                maxZigZag(node.left, False,length+1)
                maxZigZag(node.right, True,1)
            else:
                maxZigZag(node.right, True,length+1)
                maxZigZag(node.left, False,1)
        maxZigZag(root, True,0)
        maxZigZag(root, False,0)
            
        return max_length

            