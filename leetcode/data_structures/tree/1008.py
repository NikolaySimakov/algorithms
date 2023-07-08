from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder.pop(0))

        def gen(node, v):
            if not node.left and node.val > v:
                node.left = TreeNode(v)
            elif node.left and node.val > v:
                gen(node.left, v)
            if not node.right and node.val < v:
                node.right = TreeNode(v)
            elif node.right and node.val < v:
                gen(node.right, v)
        
        while len(preorder):
            gen(root, preorder.pop(0))

        return root