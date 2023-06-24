from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    # Easy to understand solution
    def rangeSumBST_simple(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def inorder(root):
            if root == None: return []
            arr = []
            arr += inorder(root.left)
            arr.append(root.val)
            arr += inorder(root.right)
            return arr
        
        tree = inorder(root)
        count = 0

        for val in tree:
            if low <= val <= high:
                count += val
        
        return count


    # Fast solution: sort values by interval in inorder traversal
    def rangeSumBST_fast(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def inorder(root):
            if not root: return []
            val = [root.val] if low <= root.val <= high else []
            left = inorder(root.left) if low <= root.val else []
            right = inorder(root.right) if root.val <= high else []
            return left + val + right
        
        return sum(inorder(root))