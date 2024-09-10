# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findGCD(a, b):
            start = min(a, b)
            for num in range(start, 0, -1):
                if a % num == 0 and b % num == 0:
                    return num
        
        curr = head
        while curr.next:
            next = curr.next
            gcd = findGCD(curr.val, next.val)
            newNode = ListNode(val = gcd, next = next)
            curr.next = newNode
            curr = next
        return head