# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        queue = [[root]]
        while queue:
            level_nodes = []

            currSum = 0
            currNodes = queue.pop()

            for node in currNodes:
                currSum += node.val
                level_nodes.append(node.left) if node.left else None
                level_nodes.append(node.right) if node.right else None
            
            if level_nodes:
                queue.append(level_nodes)
            
            if len(heap) < k:
                heapq.heappush(heap, currSum)
            else:
                top = heap[0]
                if currSum > top:
                    heapq.heappop(heap)
                    heapq.heappush(heap, currSum)
        return heap[0] if len(heap) == k else -1


