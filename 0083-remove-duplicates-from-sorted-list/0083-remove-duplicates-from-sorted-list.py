# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        while curr != None:
            if curr.val == prev.val:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        prev.next = None
        return head