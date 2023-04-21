from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        while root:
            if root.val == val:
                return root
            else:
                if root.val > val:
                    root = root.left
                else:
                    root = root.right

        return None
