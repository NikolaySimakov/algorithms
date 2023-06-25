from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs(node):
            return max(dfs(node.right) if node.right else 0, dfs(node.left) if node.left else 0) + 1
        return dfs(root)
            