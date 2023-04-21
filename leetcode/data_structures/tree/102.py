from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            lvl = []
            for _ in range(len(stack)):
                n = stack.pop(0)
                lvl.append(n.val)
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            res.append(lvl)

        return res
