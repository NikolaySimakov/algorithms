from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root: return None
        origin = root

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        if left != None:
            root.right = left
            root.left = None
            
            while root.right:
                root = root.right

            if right != None:
                root.right = right

        return origin

