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
        visited = set()
        i = 0
        while curr:
            x, y = direction[i%4]
            r, c = pos
            print(r, c, dir)
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
            pos = (pos[0] + direction[i%4][0], pos[1] + direction[i%4][1])
                
        return res