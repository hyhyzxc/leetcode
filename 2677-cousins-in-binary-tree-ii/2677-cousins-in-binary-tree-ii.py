# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        sums = []
        parentMap = []
        while queue:
            levelNodes = []
            parent = {}
            while queue:
                levelNodes.append(queue.pop())
            currLevelMap = {}
            for node in levelNodes:
                queue.append(node.left) if node.left else None
                leftval = node.left.val if node.left else 0
                queue.append(node.right) if node.right else None
                rightval = node.right.val if node.right else 0
                if node.left:
                    parent[node.left] = node
                if node.right:
                    parent[node.right] = node
                currLevelMap[node] = leftval + rightval
            sums.append(currLevelMap)
            parentMap.append(parent)
        #node.val = sum(level) - sums[parent]
        queue = [root]
        level = 0
      
        
        root.val = 0
    
        level = 0
        for levelMap in parentMap:
            currSumMap = sums[level]
            for node in levelMap:
                parent = levelMap[node]
                node.val = sum(currSumMap.values()) - currSumMap[parent]
            level += 1
            
        return root
        