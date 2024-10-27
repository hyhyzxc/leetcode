class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        max_sides = min(len(matrix), len(matrix[0]))
        m = len(matrix)
        n = len(matrix[0])
        dp = {}
        res = {}
        dp[1] = matrix.copy()
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    count += 1
        res[1] = count
        for k in range(2, max_sides+1):
            m -= 1
            n -= 1
            prev_matrix = dp[k-1]
            new_matrix = [[-1 for k in range(n)] for j in range(m)]
            count = 0
            for i in range(m):
                for j in range(n):
                    if prev_matrix[i][j] and prev_matrix[i][j+1] and prev_matrix[i+1][j] and prev_matrix[i+1][j+1]:
                        new_matrix[i][j] = 1
                        count += 1
                    else:
                        new_matrix[i][j] = 0
            dp[k] = new_matrix
            res[k] = count
        return sum(list(res.values()))