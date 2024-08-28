class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        rows = len(grid1)
        cols = len(grid1[0])
        visited = set()
        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid2[i][j] == 0:
                return True
            if (i,j) in visited:
                return True
            visited.add((i,j))
        
            if grid1[i][j] == 0:
                res = False
            else:
                res = True
            res = dfs(i-1,j) and res
            res = dfs(i+1,j) and res
            res = dfs(i,j-1) and res
            res = dfs(i,j+1) and res

            return res
        
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] and (i,j) not in visited and dfs(i,j):
                    res += 1
        
        return res