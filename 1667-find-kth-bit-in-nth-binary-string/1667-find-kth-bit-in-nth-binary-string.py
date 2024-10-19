class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dp = {1: '0'}
        for i in range(2, n+1):
            x = bin(int(dp[i-1], 2) ^ int("1" * len(dp[i-1]), 2))[2:][::-1]
            dp[i] = dp[i-1] + "1" + str(x)
            #print(x)
        return dp[n][k-1]