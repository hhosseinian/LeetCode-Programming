"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned_nodes: Dict[int, Node] = {}
        def dfs(current_node: Node) -> Node:
            if current_node.val in cloned_nodes:
                return cloned_nodes[current_node.val]

            clone = Node(current_node.val)
            cloned_nodes[current_node.val]= clone
            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
        