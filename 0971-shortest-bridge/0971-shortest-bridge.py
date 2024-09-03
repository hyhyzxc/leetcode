from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or not grid[r][c]:
                return
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        start = None
        for i in range(rows):
            if start:
                break
            for j in range(cols):
                if grid[i][j]:
                    dfs(i,j)
                    start = (i,j)
                    break
        
        startList = list((node[0], node[1], 0) for node in visited)
        q = deque(startList)
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c, level = q.popleft()
            if grid[r][c] and (r,c) not in visited:
                return level
            visited.add((r,c))
            for i, j in neighbors:
                if r + i >= 0 and r + i < rows and c + j >= 0 and c + j < cols and (r+i, c+j) not in visited:
                    if not grid[r+i][c+j]:
                        q.append((r+i, c+j, level+1))
                        visited.add((r+i, c+j))
                    else:
                        return level
        


                    