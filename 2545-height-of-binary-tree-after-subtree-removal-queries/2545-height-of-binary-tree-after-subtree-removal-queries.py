# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max1 = defaultdict(int)
        max2 = defaultdict(int)
        node_levels = {}
        node_height = {}
        def dfs(curr, level):
            left = 0
            right = 0
            if curr.left:
                left = dfs(curr.left, level + 1)
            if curr.right:
                right = dfs(curr.right, level+1)
            
            node_height[curr.val] = max(left, right) + 1
            node_levels[curr.val] = level
            return node_height[curr.val]
        dfs(root, 0)

        for node in node_levels:
            level = node_levels[node]
            height = node_height[node]
            if level not in max1:
                max1[level] = height
            else:
                max1_height = max1[level]
                if height < max1_height:
                    if height > max2[level]:
                        max2[level] = height
                else:
                    max2[level] = max1[level]
                    max1[level] = height
        res = []

        for node in queries:
            level = node_levels[node]
            height = node_height[node]
            max1_height = max1[level]
            max2_height = max2[level] if level in max2 else 0
            if height == max1_height:
                if max2_height > 0:
                    res.append(max2_height + level - 1)
                else:
                    res.append(level - 1)
            else:
                res.append(max1_height + level - 1)
        return res
