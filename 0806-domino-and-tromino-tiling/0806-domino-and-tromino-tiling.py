class Solution:
    def numTilings(self, n: int) -> int:
        dp = {}
        def solve(i, previousGap):
            if i > n:
                return 0
            if i == n:
                return 1 if not previousGap else 0
            if (i, previousGap) in dp:
                return dp[(i, previousGap)]
            if previousGap:
                dp[(i, previousGap)] = solve(i+1, False) + solve(i+1, True)
                return dp[(i, previousGap)]
            else:
                dp[(i, previousGap)] = solve(i+1, False) + 2*solve(i+2, True) + solve(i+2, False)
                return dp[(i, previousGap)]
        return solve(0, False) % 1000000007