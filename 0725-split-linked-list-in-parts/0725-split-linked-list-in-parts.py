# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr = []
        count = 0
        curr = head
        while head:
            count += 1
            arr.append(head)
            head = head.next
        groups = []
        
        numMore = max(count % k, 0)
        numEach = count // k
        print(numMore, numEach)
        i = 0
        while curr:
            #print(groups, i)
            groups.append(curr)
            if numMore > 0:
                j = numEach
                while curr and j > 0:
                    curr = curr.next
                    j -= 1
                numMore -= 1
                if not curr:
                    break
                next = curr.next
                curr.next = None
                curr = next
            else:
                j = numEach - 1
                while curr and j > 0:
                    curr = curr.next
                    j -= 1
                if not curr:
                    break
                next = curr.next
                curr.next = None
                curr = next
            i += 1
        while len(groups) < k:
            groups.append(None)
        return groups