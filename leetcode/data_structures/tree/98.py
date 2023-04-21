# Validate Binary Search Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        return True if arr == list(sorted(set(arr))) else False
