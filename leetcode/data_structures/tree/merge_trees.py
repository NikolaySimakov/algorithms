from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(r1, r2):
            if r1 == None and r2 == None:
                return None

            if r1 == None:
                return r2
            elif r2 == None:
                return r1
            else:
                node = TreeNode(val=r1.val + r2.val)
                node.left = dfs(r1.left, r2.left)
                node.right = dfs(r1.right, r2.right)
                return node

        return dfs(root1, root2)
