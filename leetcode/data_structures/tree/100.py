from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    # Easy to understand
    def isSameTree_easy(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    # 2 lines
    def isSameTree_2_lines(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q: return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    # using stack
    def isSameTree_stack(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # TODO
        pass