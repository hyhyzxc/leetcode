# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, curr):
            if not head:
                return True
            if not curr:
                return False
            
            if head.val == curr.val:
                if not head.next:
                    return True
                left = False
                right = False
                if curr.left and curr.left.val == head.next.val:
                    left = dfs(head.next, curr.left)
                if curr.right and curr.right.val == head.next.val:
                    right = dfs(head.next, curr.right)
                return left or right
            else:
                return dfs(head, curr.left) or dfs(head, curr.right)
        
        def findStart(curr):
            if not curr:
                return False
            if curr.val == head.val:
                if dfs(head, curr):
                    return True
                else:
                    return findStart(curr.left) or findStart(curr.right)
            else:
                return findStart(curr.left) or findStart(curr.right)
            
        return findStart(root)
