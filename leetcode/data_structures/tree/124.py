from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:

    max_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def max_gain(node):
            if not node: return 0

            val = node.val
            right = max(max_gain(node.right), 0)
            left = max(max_gain(node.left), 0)

            path_sum = val + right + left
            self.max_sum = max(self.max_sum, path_sum)

            return val + max(right, left)

        max_gain(root)
        return self.max_sum