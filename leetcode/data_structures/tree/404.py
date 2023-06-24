from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, is_left=False):
            if not node: return 0
            if not node.right and not node.left and is_left:
                return node.val
            
            return dfs(node.right) + dfs(node.left, True)
        
        return dfs(root)