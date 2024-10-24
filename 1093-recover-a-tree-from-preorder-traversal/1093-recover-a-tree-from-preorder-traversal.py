# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if traversal == "":
            return []
        n = len(traversal)
        stack = []
        i = 0 
        while i<n:
            depth = 0
            while i<n and traversal[i] == '-':
                depth+=1
                i+=1
            val = ''
            while i<n and traversal[i] != '-':
                val+=traversal[i]
                i+=1
            current_value = int(val)
            curr_node = TreeNode(current_value)
            while len(stack)>depth:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = curr_node
                else:
                    stack[-1].right = curr_node
            stack.append(curr_node)
        return stack[0]
        


