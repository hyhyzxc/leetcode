class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = {}
        moves = [(-1, 1), (0, 1), (1,1)]
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(r, c):
            if (r,c) in dp:
                return dp[(r,c)]
            currVal = grid[r][c]
            newMoves = 0
            for delta_r, delta_c in moves:
                new_r, new_c = r + delta_r, c + delta_c
                if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and grid[new_r][new_c] > currVal:
                    newMoves = max(newMoves, 1+ dfs(new_r, new_c))
            dp[(r,c)] = newMoves
            return newMoves
        
       
        for c in range(rows):
            res = max(res, dfs(c, 0))     
        return res
                

            