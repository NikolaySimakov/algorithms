from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return None

    def preorder(node):
        res = []
        res.append(node.val)
        if node.left:
            res += preorder(node.left)
        if node.right:
            res += preorder(node.right)
        return res

    return preorder(root)


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return None

    def inorder(node):
        res = []
        if node.left:
            res += inorder(node.left)
        res.append(node.val)
        if node.right:
            res += inorder(node.right)
        return res

    return inorder(root)


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return None

    def postorder(node):
        res = []
        if node.left:
            res += postorder(node.left)
        if node.right:
            res += postorder(node.right)
        res.append(node.val)
        return res

    return postorder(root)
