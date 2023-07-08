from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # dfs recursion solution
    def bstFromPreorderDFS(self, preorder: List[int]) -> Optional[TreeNode]:
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
    
    
    # recursion solution
    def bstFromPreorderRecursion(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None

        root = TreeNode(preorder[0])
        i = 1

        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        
        root.left = self.bstFromPreorderRecursion(preorder[1:i])
        root.right = self.bstFromPreorderRecursion(preorder[i:])
        return root
    
    
    # stack solution
    def bstFromPreorderStack(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        parent = root
        stack = [parent]

        for val in preorder[1:]:
            node = TreeNode(val)
            if stack and val < parent.val:
                parent.left = node
                stack.append(node)
            else:
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node
                stack.append(node)
            
            parent = node
        
        return root