class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        circles = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'X'):
                return
            circles.add((r,c))
            dfs(r+1, c) if (r+1, c) not in circles else None
            dfs(r-1, c) if (r-1, c) not in circles else None
            dfs(r, c-1) if (r, c-1) not in circles else None
            dfs(r, c+1) if (r, c+1) not in circles else None
        for i in range(cols):
            dfs(0, i) if board[0][i] == 'O' else None
            dfs(rows-1, i) if board[rows-1][i] == 'O' else None
            
        for i in range(rows):
            dfs(i, 0) if board[i][0] == 'O' else None
            dfs(i, cols-1) if board[i][cols-1] == 'O' else None
          
        for i in range(rows):
            for j in range(cols):
                if (i,j) in circles:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
    