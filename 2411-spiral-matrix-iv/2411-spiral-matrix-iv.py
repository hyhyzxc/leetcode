# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        curr = head
        res = [[-1 for i in range(n)] for j in range(m)]
        pos = (0,0)
        i = 0
        while curr:
            dirIndex = i % 4
            x, y = direction[dirIndex]
            r, c = pos
            #print(r, c, dir)
            while r >= 0 and r < m and c >= 0 and c < n and res[r][c] == -1:
                res[r][c] = curr.val
                curr = curr.next
                if curr is None:
                    return res
                pos = (r+x, c+y)
                r, c = pos
                #print(pos)
            
            pos = (r-x, c-y)
            i += 1
            dirIndex = i % 4
            pos = (pos[0] + direction[dirIndex][0], pos[1] + direction[dirIndex][1])
                
        return res