from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        from_right = True
        res = []
        q = [root]

        while len(q) > 0:
            arr = []
            queue_len = len(q)
            for _ in range(queue_len):
                node = q.pop(0)
                arr.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)

            res.append(list(reversed(arr)) if from_right else arr)
            from_right = not from_right
        
        return res