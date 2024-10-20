# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        inorder_stack = []
        preorder_stack = []
        
        def inorder_travarse(node):
            if not node:
                return
            inorder_travarse(node.left)
            inorder_stack.append(node.val)
            inorder_travarse(node.right)

        def preorder_travarse(node):
            if not node:
                return
            preorder_stack.append(node.val)
            preorder_travarse(node.left)
            preorder_travarse(node.right)
        inorder_travarse(root)
        preorder_travarse(root)
        #print(inorder_stack+preorder_stack)
        return ','.join(str(i) for i in inorder_stack)+';'+','.join(str(i) for i in preorder_stack)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        n = len(data)
        if n == 0:
            return None
        stack = data.split(';')
        preorder_stack = [int(i) for i in stack[1].split(',')]
        inorder_stack = [int(i) for i in stack[0].split(',')]
        #print(inorder_stack+preorder_stack)
        
        def Buildtree(preorder_stack:Optional[TreeNode],inorder_stack:Optional[TreeNode])->Optional[TreeNode]:
            if not preorder_stack or not inorder_stack:
                return None
            root_val = preorder_stack[0]
            root = TreeNode(root_val)
            root_index=inorder_stack.index(root_val)
            root.left = Buildtree(preorder_stack[1:root_index+1],inorder_stack[:root_index])
            root.right = Buildtree(preorder_stack[root_index+1:],inorder_stack[root_index+1:])
            return root

        return Buildtree(preorder_stack,inorder_stack)



        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans