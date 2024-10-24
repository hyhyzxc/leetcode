# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False

        if root1.val != root2.val:
            return False
        
        if (root1.left and root2.right and root1.left.val == root2.right.val) or (root1.left and not root2.left) or (root1.right and not root2.right):
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        
        else:
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)

        
        
        