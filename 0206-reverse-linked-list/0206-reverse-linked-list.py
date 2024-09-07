# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head, prev):
            if not head:
                return head
            if not head.next:
                head.next = prev
                return head
            next = head.next
            head.next = prev
            return reverse(next, head)
        return reverse(head, None)
